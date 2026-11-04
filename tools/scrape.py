#!/usr/bin/env python3
"""Download the WinDIY build guides (nerdiy.de + hackaday.io) as Markdown with local images."""
import hashlib, os, re, sys, time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
IMG = os.path.join(DOCS, "images")
UA = {"User-Agent": "Mozilla/5.0 (WinDIY-docs-archiver)"}

PAGES = [
    ("00-uebersicht", "https://nerdiy.de/windiy-die-wind-turbine-aus-dem-3d-drucker/"),
    ("01-fluegel", "https://nerdiy.de/howto-windiy-fluegel-der-windturbine-aufbauen/"),
    ("02-windfahne", "https://nerdiy.de/howto-windiy-windfahne-zusammenbauen/"),
    ("03-nabe", "https://nerdiy.de/howto-windiy-nabe-inkl-mechanik-aufbauen/"),
    ("04-drehturm", "https://nerdiy.de/howto-windiy-drehturm-aufbauen/"),
    ("05-hauptachse", "https://nerdiy.de/howto-windiy-montage-der-hauptachse/"),
    ("06-pitch-aktor", "https://nerdiy.de/howto-windiy-pitch-aktor-zusammenbauen/"),
    ("07-zusammenbau", "https://nerdiy.de/howto-windiy-zusammenbau-der-vorbereiteten-komponenten/"),
    ("08-nerdiskerator-generator", "https://nerdiy.de/nerdiskerator-a-generator-from-the-3d-printer/"),
    ("10-hackaday-details", "https://hackaday.io/project/172328-windiy-hawt-wind-turbine/details"),
    ("11-hackaday-instructions", "https://hackaday.io/project/172328/instructions"),
]
HACKADAY_LOGS = "https://hackaday.io/project/172328/logs?sort=oldest&page={}"
IMG_EXT = re.compile(r"\.(jpe?g|png|gif|webp)(\?.*)?$", re.I)

def best_src(img):
    for attr in ("data-orig-file", "data-large-file", "data-src", "data-lazy-src", "src"):
        v = img.get(attr)
        if v and not v.startswith("data:"):
            return v
    srcset = img.get("srcset") or img.get("data-srcset")
    if srcset:
        return srcset.split(",")[-1].strip().split(" ")[0]
    return None

def fetch_image(url, slug):
    url = url.split("?")[0] if "nerdiy.de" in url else url
    name = os.path.basename(urlparse(url).path) or "img"
    name = re.sub(r"[^A-Za-z0-9._-]", "_", name)
    if "." not in name:
        name += ".jpg"
    name = hashlib.sha1(url.encode()).hexdigest()[:6] + "-" + name
    rel = f"images/{slug}/{name}"
    path = os.path.join(DOCS, rel)
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            r = requests.get(url, headers=UA, timeout=60)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
        except Exception as e:
            print("  ! image failed", url, e, file=sys.stderr)
            return url
    return rel

def content_node(soup, url):
    if "hackaday.io" in url:
        for c in soup.select("div.post-content"):
            if "post-comments" not in c.get("class", []):
                return c
        return soup.body
    return soup.select_one("div.entry-content") or soup.select_one("article") or soup.body

def page_body(slug, url):
    """Fetch url, return (title, markdown body) with images localised."""
    print("fetch", url)
    html = requests.get(url, headers=UA, timeout=60).text
    soup = BeautifulSoup(html, "html.parser")
    title = (soup.select_one("h1.entry-title") or soup.find("h1") or soup.title).get_text(" ", strip=True)
    if "hackaday.io" in url:
        title = soup.title.get_text(" ", strip=True).replace(" | Hackaday.io", "")
    node = content_node(soup, url)
    steps = node.select("div.instruction-step")
    if steps:  # hackaday instructions: one <h2> per step instead of one giant nested list
        box = soup.new_tag("div")
        for i, st in enumerate(steps, 1):
            t = st.select_one(".instruction-list-title")
            h = soup.new_tag("h2")
            h.string = f"Schritt {i}: {t.get_text(' ', strip=True) if t else ''}"
            box.append(h)
            c = st.select_one(".instruction-list-item")
            if c:
                for h_ in c.find_all(["h1", "h2", "h3", "h4", "h5"]):
                    h_.name = "h" + str(min(int(h_.name[1]) + 1, 6))
                box.append(c.extract())
        node = box
    for bad in node.select("script, style, noscript, .sharedaddy, .jp-relatedposts, "
                           "#jp-relatedposts, .wpcnt, .ezoic-ad, ins, iframe[src*='ads'], "
                           "a[href*='ko-fi.com'], img[src*='pixel.gif'], img[src*='/impression'], "
                           ".post-author, .author-info, .discussion-list, .description-metainfo, "
                           ".section-buildsort, .pagination, .post-meta, .like-button"):
        bad.decompose()
    # YouTube embeds -> local thumbnail linking to the video (works offline as an image)
    for fr in node.find_all("iframe"):
        m = re.search(r"(?:youtube(?:-nocookie)?\.com/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", fr.get("src", "") + fr.get("data-src", ""))
        if not m:
            fr.decompose(); continue
        vid = m.group(1)
        thumb = None
        for q in ("maxresdefault", "hqdefault"):
            t = fetch_image(f"https://img.youtube.com/vi/{vid}/{q}.jpg", slug)
            if not t.startswith("http"):
                thumb = t; break
        a = soup.new_tag("a", href=f"https://www.youtube.com/watch?v={vid}")
        a.append(soup.new_tag("img", src=thumb or f"https://img.youtube.com/vi/{vid}/hqdefault.jpg",
                              alt=f"YouTube-Video {vid} (Vorschau – klicken zum Abspielen)"))
        p = soup.new_tag("p"); p.append(a)
        fr.replace_with(p)
    for img in node.find_all("img"):
        src = best_src(img)
        if src and src.startswith("images/"):
            continue  # already local (YouTube thumbnail)
        if not src:
            img.decompose(); continue
        img["src"] = fetch_image(urljoin(url, src), slug)
        for a in list(img.attrs):
            if a not in ("src", "alt", "title"):
                del img[a]
    for a in node.find_all("a", href=True):
        a["href"] = urljoin(url, a["href"])
        # gallery links to the full-size photo -> point at the local copy for offline use
        img = a.find("img")
        if img and IMG_EXT.search(a["href"]) and img.get("src", "").startswith("images/"):
            a["href"] = img["src"]
    body = md(str(node), heading_style="ATX", bullets="-", strip=["span", "div", "figure"])
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return title, body

def convert(slug, url):
    title, body = page_body(slug, url)
    out = f"---\ntitle: \"{title}\"\nsource: {url}\nretrieved: {time.strftime('%Y-%m-%d')}\n---\n\n# {title}\n\n{body}\n"
    with open(os.path.join(DOCS, slug + ".md"), "w") as f:
        f.write(out)

def hackaday_logs(slug="12-hackaday-logs"):
    urls = []
    for page in range(1, 10):
        html = requests.get(HACKADAY_LOGS.format(page), headers=UA, timeout=60).text
        found = [u for u in re.findall(r'href="(/project/172328/log/\d+[^"#]*)"', html) if u not in urls]
        if not found:
            break
        urls += list(dict.fromkeys(found))
    parts = ["---", 'title: "WinDIY - Hackaday Build Logs"',
             "source: https://hackaday.io/project/172328/logs", f"retrieved: {time.strftime('%Y-%m-%d')}",
             "---", "", "# WinDIY – Hackaday Build Logs (chronologisch)", ""]
    for u in urls:
        full = urljoin("https://hackaday.io", u)
        title, body = page_body(slug, full)
        body = re.sub(r"^(#+)", r"#\1", body, flags=re.M)  # demote headings below the log title
        parts += [f"## {title.split(' | ')[0]}", "", f"Quelle: <{full}>", "", body, "", "---", ""]
    with open(os.path.join(DOCS, slug + ".md"), "w") as f:
        f.write("\n".join(parts))

if __name__ == "__main__":
    os.makedirs(IMG, exist_ok=True)
    for slug, url in [p for p in PAGES if len(sys.argv) < 2 or p[0] in sys.argv[1:]]:
        convert(slug, url)
    if len(sys.argv) < 2 or "12-hackaday-logs" in sys.argv[1:]:
        hackaday_logs()
