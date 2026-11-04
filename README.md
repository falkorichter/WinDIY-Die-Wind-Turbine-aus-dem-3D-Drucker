# WinDIY – Offline-Archiv & maschinenlesbare Stückliste

Offline-Kopie der Bauanleitung der 3D-gedruckten Windturbine **WinDIY** von nerdiy.de / Hackaday.io,
plus eine maschinenlesbare Stückliste mit AliExpress-Preisschätzung.

- Original: <https://nerdiy.de/windiy-die-wind-turbine-aus-dem-3d-drucker/>
- Hackaday: <https://hackaday.io/project/172328-windiy-hawt-wind-turbine>
- STL-Dateien: <https://github.com/Nerdiyde/WinDIY>

Alle Fotos liegen lokal unter `docs/images/`, der Ordner funktioniert also auch offline.
YouTube-Videos sind als lokales Vorschaubild eingebunden, das auf das Video verlinkt.

## Anleitungen (`docs/`)

| Datei | Inhalt |
|---|---|
| [00-uebersicht.md](docs/00-uebersicht.md) | Projektübersicht, Videos, Elektronik |
| [01-fluegel.md](docs/01-fluegel.md) | Flügel aufbauen (3×) |
| [02-windfahne.md](docs/02-windfahne.md) | Windfahne zusammenbauen ¹ |
| [03-nabe.md](docs/03-nabe.md) | Nabe inkl. Mechanik |
| [04-drehturm.md](docs/04-drehturm.md) | Drehturm |
| [05-hauptachse.md](docs/05-hauptachse.md) | Hauptachse |
| [06-pitch-aktor.md](docs/06-pitch-aktor.md) | Pitch-Aktor |
| [07-zusammenbau.md](docs/07-zusammenbau.md) | Zusammenbau der vorbereiteten Komponenten (Geräteträger, Abdeckungen) ¹ |
| [08-nerdiskerator-generator.md](docs/08-nerdiskerator-generator.md) | Scheibengenerator „Nerdiskerator“ (separates Projekt, keine Materialliste) |
| [10-hackaday-details.md](docs/10-hackaday-details.md) | Hackaday: Projektdetails |
| [11-hackaday-instructions.md](docs/11-hackaday-instructions.md) | Hackaday: alle 8 Anleitungen (EN), inkl. **Bremsaktor** (Schritt 8) |
| [12-hackaday-logs.md](docs/12-hackaday-logs.md) | Hackaday: alle 38 Build-Logs chronologisch |
| [einkaufsliste.md](docs/einkaufsliste.md) | Einkaufsliste mit Preisen & Links (generiert) |

¹ Auf nerdiy.de ist die Materialtabelle dieser Seiten leer. Die Teile stammen aus der Hackaday-Version derselben Anleitung.

## Daten (`data/`)

| Datei | Art | Inhalt |
|---|---|---|
| `stueckliste.csv` | **Quelle**, von Hand gepflegt | Jedes Teil je Baugruppe (inkl. 3D-Druckteile mit STL-Pfad und Werkzeug) |
| `aliexpress.csv` | **Quelle**, von Hand gepflegt | Je `teil_id` ein AliExpress-Angebot: Packungsinhalt, Preis, Link |
| `windiy-teileliste.csv` | generiert | Die große Tabelle: alle Zeilen aus der Stückliste + Gesamtmenge + Shop-Spalten |
| `einkaufsliste.csv` | generiert | Pro Teil aggregiert: Gesamtmenge, benötigte Packungen, geschätzte Kosten |

Spalten in `stueckliste.csv`:
`modul, anleitung, teil_id, bezeichnung, menge_pro_baugruppe, anzahl_baugruppen, einheit, kategorie, stl, hinweis`.
Die Gesamtmenge ist `menge_pro_baugruppe × anzahl_baugruppen` (z. B. Flügel ×3). Längen werden in `mm` angegeben.
`teil_id` ist über alle Baugruppen gleich, z. B. `M3x20-DIN7991` (Senkkopf), `M3x20-DIN912` (Zylinderkopf) oder `KL-603ZZ`.

Hinweise zur Stückliste:
- Wo die Originalliste Muttern auslässt, im Text aber „inkl. Mutter“ steht, sind sie ergänzt und in `hinweis` markiert.
- Generator-Teile (`kategorie=Generator`) sind optional und in der Summe getrennt ausgewiesen.
- Die Preise sind „ab“-Preise von AliExpress-Suchergebnissen ohne Versand, Stand siehe `aliexpress.csv`. Bitte vor dem Kauf die Variante prüfen.

## Neu erzeugen

```sh
python3 -m venv .venv && .venv/bin/pip install requests beautifulsoup4 markdownify
.venv/bin/python tools/scrape.py               # alle Seiten + Bilder neu laden (Bilder werden gecacht)
.venv/bin/python tools/scrape.py 03-nabe       # nur eine Seite
python3 tools/build_bom.py                     # CSVs + docs/einkaufsliste.md neu erzeugen
.venv/bin/python tools/aliexpress_search.py "603zz" "m3 mutter"  > /tmp/ali.json   # Preise recherchieren
```

## Lizenz

Inhalte, Fotos und Designs stammen von Fabian / [nerdiy.de](https://nerdiy.de) und stehen unter
**CC BY-NC-SA 4.0** (siehe <https://nerdiy.de/en/lizenz/>). Dieses Repo ist eine Archivkopie mit Quellenangabe in jeder Datei.
