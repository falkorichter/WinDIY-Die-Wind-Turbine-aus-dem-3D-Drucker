#!/usr/bin/env python3
"""Query de.aliexpress.com search for each term and dump the top results (id, title, from-price EUR, sold).

Usage: aliexpress_search.py "603zz" "m3 mutter edelstahl" ... > results.json
Prices are the listing's *lowest variant* ("ab"-Preis), so check the variant you need.
"""
import json, re, sys, time, urllib.parse, requests

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36", "Accept-Language": "de-DE"}

def search(term, n=12):
    url = "https://de.aliexpress.com/w/wholesale-" + urllib.parse.quote(term.replace(" ", "-")) + ".html"
    html = requests.get(url, headers=UA, timeout=60).text
    out, seen = [], set()
    for chunk in html.split('"productId":')[1:]:
        m = re.match(r'"?(\d{10,})', chunk)
        if not m or m.group(1) in seen:
            continue
        t = re.search(r'"displayTitle":"((?:[^"\\]|\\.)*)"', chunk)
        p = re.search(r'"salePrice":\{[^}]*"minPrice":([\d.]+)', chunk)
        s = re.search(r'"tradeDesc":"([^"]*)"', chunk)
        if not (t and p):
            continue
        seen.add(m.group(1))
        out.append({"id": m.group(1), "title": json.loads('"' + t.group(1) + '"'),
                    "price_eur": float(p.group(1)), "sold": s.group(1) if s else "",
                    "url": f"https://de.aliexpress.com/item/{m.group(1)}.html"})
        if len(out) >= n:
            break
    return url, out

if __name__ == "__main__":
    res = {}
    for term in sys.argv[1:]:
        url, items = search(term)
        res[term] = {"search_url": url, "items": items}
        print(f"{term}: {len(items)}", file=sys.stderr)
        time.sleep(float(__import__("os").environ.get("ALI_SLEEP", "8")))
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
