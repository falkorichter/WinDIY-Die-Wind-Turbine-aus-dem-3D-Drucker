#!/usr/bin/env python3
"""Build the combined WinDIY part tables from the two hand-maintained sources.

  data/stueckliste.csv  – every part per assembly, as given in the build guides
  data/aliexpress.csv   – one shop listing per teil_id (pack size, price, link)

Outputs (generated, do not edit by hand):
  data/windiy-teileliste.csv – the big table: every BOM row + total qty + shop columns
  data/einkaufsliste.csv     – aggregated per teil_id: total qty, packs needed, est. cost
  docs/einkaufsliste.md      – same as the shopping list, readable on GitHub/offline
"""
import csv, math, os
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, *p)
NO_BUY = {"3D-Druck", "Werkzeug"}


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def num(s):
    return float(s) if s not in (None, "") else None


def fmt(x):
    return "" if x is None else (str(int(x)) if float(x).is_integer() else f"{x:.2f}")


def main():
    bom = read(D("data", "stueckliste.csv"))
    shop = {r["teil_id"]: r for r in read(D("data", "aliexpress.csv"))}

    # big table
    shop_cols = ["packung_inhalt", "preis_eur_packung", "ab_preis_eur", "aliexpress_url", "aliexpress_titel",
                 "suche_url", "stand"]
    big = []
    for r in bom:
        total = float(r["menge_pro_baugruppe"]) * float(r["anzahl_baugruppen"])
        s = shop.get(r["teil_id"], {})
        big.append({**r, "menge_gesamt": fmt(total), **{c: s.get(c, "") for c in shop_cols}})
    write(D("data", "windiy-teileliste.csv"), big,
          list(bom[0].keys())[:7] + ["menge_gesamt"] + list(bom[0].keys())[7:] + shop_cols)

    # shopping list
    agg = OrderedDict()
    for r in bom:
        if r["kategorie"] in NO_BUY:
            continue
        a = agg.setdefault(r["teil_id"], {"teil_id": r["teil_id"], "bezeichnung": r["bezeichnung"],
                                          "kategorie": r["kategorie"], "einheit": r["einheit"],
                                          "menge_gesamt": 0.0, "module": []})
        a["menge_gesamt"] += float(r["menge_pro_baugruppe"]) * float(r["anzahl_baugruppen"])
        if r["modul"] not in a["module"]:
            a["module"].append(r["modul"])

    rows, total_cost, missing = [], 0.0, []
    for tid, a in agg.items():
        s = shop.get(tid, {})
        pack, price = num(s.get("packung_inhalt")), num(s.get("preis_eur_packung"))
        packs = math.ceil(a["menge_gesamt"] / pack - 1e-9) if pack else None
        if s.get("packungen_fix"):  # e.g. profile bars: cutting waste needs more than total/length
            packs = int(s["packungen_fix"])
        cost = packs * price if (packs and price is not None) else None
        if cost is None:
            missing.append(tid)
        else:
            total_cost += cost
        rows.append({**a, "menge_gesamt": fmt(a["menge_gesamt"]), "module": " ".join(a["module"]),
                     "packung_inhalt": s.get("packung_inhalt", ""), "packungen": fmt(packs),
                     "preis_eur_packung": s.get("preis_eur_packung", ""),
                     "ab_preis_eur": s.get("ab_preis_eur", ""), "kosten_eur": fmt(cost),
                     "optional": "ja" if a["kategorie"] == "Generator" else "",
                     "aliexpress_url": s.get("aliexpress_url", ""), "aliexpress_titel": s.get("aliexpress_titel", ""),
                     "suche_url": s.get("suche_url", ""), "hinweis_shop": s.get("hinweis", "")})
    fields = ["teil_id", "bezeichnung", "kategorie", "einheit", "menge_gesamt", "module", "packung_inhalt",
              "packungen", "preis_eur_packung", "ab_preis_eur", "kosten_eur", "optional", "aliexpress_url", "aliexpress_titel",
              "suche_url", "hinweis_shop"]
    write(D("data", "einkaufsliste.csv"), rows, fields)

    core = sum(float(r["kosten_eur"]) for r in rows if r["kosten_eur"] and not r["optional"])
    opt = sum(float(r["kosten_eur"]) for r in rows if r["kosten_eur"] and r["optional"])
    stand = next((s.get("stand") for s in shop.values() if s.get("stand")), "")
    md = ["# WinDIY – Einkaufsliste (ohne 3D-Druckteile)", "",
          f"Automatisch erzeugt aus `data/stueckliste.csv` + `data/aliexpress.csv` (`tools/build_bom.py`). "
          f"Preise: AliExpress.de, Stand {stand}, ohne Versand. `€/Pack.` ist eine Schätzung für die benötigte "
          f"Variante, `ab` der niedrigste Variantenpreis des Angebots laut Suche.", "",
          f"**Summe Turbine: ca. {core:.0f} €** · optionaler Generator (Nerdiskerator): ca. {opt:.0f} €", "",
          "| Teil | Menge | Packung | Pack. | €/Pack. | ab € | € | Link |", "|---|---:|---:|---:|---:|---:|---:|---|"]
    for r in rows:
        link = f"[Angebot]({r['aliexpress_url']})" if r["aliexpress_url"] else f"[Suche]({r['suche_url']})"
        name = r["bezeichnung"] + (" *(optional)*" if r["optional"] else "")
        md.append(f"| {name} | {r['menge_gesamt']} {r['einheit']} | {r['packung_inhalt']} | {r['packungen']} | "
                  f"{r['preis_eur_packung']} | {r['ab_preis_eur']} | {r['kosten_eur']} | {link} |")
    with open(D("docs", "einkaufsliste.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"Turbine ≈ {core:.2f} €, Generator optional ≈ {opt:.2f} €")
    if missing:
        print("ohne Preis:", ", ".join(missing))


if __name__ == "__main__":
    main()
