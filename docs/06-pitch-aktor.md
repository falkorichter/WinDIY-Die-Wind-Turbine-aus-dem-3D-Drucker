---
title: "HowTo: WinDIY – Pitch Aktor zusammenbauen"
source: https://nerdiy.de/howto-windiy-pitch-aktor-zusammenbauen/
retrieved: 2026-11-04
---

# HowTo: WinDIY – Pitch Aktor zusammenbauen

Eine Komponente, die WinDIY sicherer machen soll, ist der Pitch-Aktuator.

Dadurch kann der Anstellwinkel des Flügels über eine Schubstange geändert werden. Im Notfall (z. B. wenn die Geschwindigkeit zu hoch ist) kann der Anstellwinkel geändert werden, so dass der Wind nicht mehr genügend Energie auf die Blätter übertragen kann.

Insbesondere bei starkem Wind kann die Geschwindigkeit auf diese Weise effektiv reduziert werden.

Der Aufbau des Pitch-Aktuators wird im folgenden Artikel beschrieben.

---

## Sicherheitshinweise

Ich weiß die folgenden Hinweise sind immer irgendwie lästig und wirken unnötig. Aber leider haben schon viele Menschen die es "besser" wussten aus Leichtsinnigkeit Augen, Finger oder anderes verloren bzw. sich verletzt. Im Vergleich dazu ist ein Datenverlust fast nicht der Rede Wert, aber auch diese können echt ärgerlich sein. Deswegen nehmt Euch bitte fünf Minuten Zeit um die Sicherheitshinweise zu lesen. Denn auch das coolste Projekt ist keine Verletzung oder anderen Ärger wert.  
***<https://www.nerdiy.de/sicherheitshinweise/>***

## Affiliatelinks/Werbelinks

*Die hier in aufgeführten Links zu Online-Shops sind sogenannte Affiliate-Links. Wenn Du auf so einen Affiliate-Link klickst und über diesen Link einkaufst, bekommt Nerdiy.de von dem betreffenden Online-Shop oder Anbieter eine Provision. Für Dich verändert sich der Preis nicht. Falls Du Deine Einkäufe über diese Links tätigst unterstützt Du Nerdiy.de dabei auch in Zukunft weitere nützliche Projekte anbieten zu können. 🙂*

---

## Voraussetzungen

**Hilfreiche Artikel:**  
Für die Montage des Pitch-Aktuators benötigen Sie neben den Teilen und Werkzeugen nur Geduld und ein paar einfache Fähigkeiten. Tipps zu den einzelnen Schritten finden Sie in folgenden Artikeln:  
***[***Mechanik – Innengewinde schneiden***](https://nerdiy.de/howto-mechanik-innengewinde-schneiden/)***

**Notwendige Werkzeuge:**

|  |
| --- |
| Heißklebepistole |
| 3D Drucker |
| Innensechskantschlüssel |
| Lötkolben |
| Lötzinn |

**Erforderliches Material:**

**In der folgenden Liste finden Sie alle Teile, die Sie zur Implementierung dieses Artikels benötigen.**

|  |  |
| --- | --- |
| 1x | mountV |
| 1x | pitchControllBase |
| 1x | gearSmall |
| 1x | shaft |
| 1x | nutCover |
| 4x | M3x50 Senkkopfschraube |
| 6x | M3x25 Senkkopfschraube |
| 2x | M3x16 Senkkopfschraube |
| 15x | M3 Mutter |
| 2x | M3 Madenschraube |
| 1x | 603ZZ Kugellager |
| 1x | 606ZZ Kugellager |
| 1x | M6 Mutter |
| 3x | M3x40 Zylinderkopfschraube |
| 1x | 3-6V Getriebemotor |
| ca. 10cm | Schrumpfschlauch |
| ca. 1m | Leitung (verschiedene Farben) |
| 1x | B103 B10K Ohm Potentiometer 10K 75mm SC6080GH |

---

## Die erforderlichen Teile

[![](images/06-pitch-aktor/8d82cf-www.nerdiy.de-20200805-145525.jpg)](images/06-pitch-aktor/8d82cf-www.nerdiy.de-20200805-145525.jpg)

Auf dem Bild sehen Sie die benötigten Teile.

Die gezeigten Kunststoffteile finden Sie im Nerdiy-GitHub. Hier: ***<https://github.com/Nerdiyde/WinDIY/tree/master/pitch-actuator>***

Ich habe die Teile mit den Folgenden Einstellungen gedruckt.

- Perimeter: 5
- Infill: 30%

**Die Schrauben sollten am besten aus Edelstahl sein, damit sie durch Feuchtigkeit nicht rosten.**

---

## Vorbereitung der einzelnen Komponenten

Bevor Sie mit der Montage der gesamten Pitch-Aktuatoreinheit beginnen können, sollten Sie zunächst einige kleinere Komponenten vorgefertigen. Zum Beispiel das Antriebsrad und sein Träger.

[![](images/06-pitch-aktor/53feb2-www.nerdiy.de-20200805-145707.jpg)](images/06-pitch-aktor/53feb2-www.nerdiy.de-20200805-145707.jpg)

Das Antriebsrad wird einseitig von einem 603ZZ-Kugellager getragen. Auf der anderen Seite ist es an der Motorachse des Antriebsmotors montiert.

Zuerst benötigen Sie die im Bild gezeigten Teile.

[![](images/06-pitch-aktor/ceaacb-www.nerdiy.de-20200805-145729.jpg)](images/06-pitch-aktor/ceaacb-www.nerdiy.de-20200805-145729.jpg)

Setzen Sie dann das Kugellager wie gezeigt in die entsprechende Aussparung auf der Vorderseite des Zahnrads ein.

[![](images/06-pitch-aktor/191a7b-www.nerdiy.de-20200805-145752.jpg)](images/06-pitch-aktor/191a7b-www.nerdiy.de-20200805-145752.jpg)

Stellen Sie sicher, dass das Zahnrad in der Aussparung so eben wie möglich ist.

[![](images/06-pitch-aktor/d8befb-www.nerdiy.de-20200805-145755-1.jpg)](images/06-pitch-aktor/d8befb-www.nerdiy.de-20200805-145755-1.jpg)

Von der Seite gesehen sollte das Kugellager kaum aus dem Zahnrad herausragen.

[![](images/06-pitch-aktor/30a303-www.nerdiy.de-20200805-145830.jpg)](images/06-pitch-aktor/30a303-www.nerdiy.de-20200805-145830.jpg)

Um das Zahnrad später an der Motorachse befestigen zu können, sollten Sie nun die beiden Madenschrauben wie abgebildet einschrauben.

Möglicherweise müssen Sie zuerst ein Gewinde in die Löcher schneiden. Wie Sie dies tun können, ist in folgendem Artikel beschrieben: [***HowTo: Mechanik – Innengewinde schneiden***](https://nerdiy.de/howto-mechanik-innengewinde-schneiden/)

[![](images/06-pitch-aktor/8807a2-www.nerdiy.de-20200805-145853.jpg)](images/06-pitch-aktor/8807a2-www.nerdiy.de-20200805-145853.jpg)

Von oben gesehen sollte dies so aussehen.

[![](images/06-pitch-aktor/8d6aa3-www.nerdiy.de-20200805-145921.jpg)](images/06-pitch-aktor/8d6aa3-www.nerdiy.de-20200805-145921.jpg)

Stellen Sie sicher, dass Sie die Schrauben wie gezeigt einschrauben (nicht zu weit).

[![](images/06-pitch-aktor/6a26c2-www.nerdiy.de-20200805-150020.jpg)](images/06-pitch-aktor/6a26c2-www.nerdiy.de-20200805-150020.jpg)

Nun ist der Getriebeträger vorbereitet. Dazu benötigen Sie die abgebildeten Teile.

[![](images/06-pitch-aktor/dad30e-www.nerdiy.de-20200805-150115.jpg)](images/06-pitch-aktor/dad30e-www.nerdiy.de-20200805-150115.jpg)

Setzen Sie die Schraube wie gezeigt in den Getriebeträger ein.

[![](images/06-pitch-aktor/964611-www.nerdiy.de-20200805-150131.jpg)](images/06-pitch-aktor/964611-www.nerdiy.de-20200805-150131.jpg)

Auf der anderen Seite können Sie dann die Mutter anschrauben.

[![](images/06-pitch-aktor/a33f51-www.nerdiy.de-20200805-150133.jpg)](images/06-pitch-aktor/a33f51-www.nerdiy.de-20200805-150133.jpg)

Nahaufnahme der aufgeschraubten Mutter.

[![](images/06-pitch-aktor/fc6cdd-www.nerdiy.de-20200805-150156.jpg)](images/06-pitch-aktor/fc6cdd-www.nerdiy.de-20200805-150156.jpg)

Für einen ersten Test können Sie die Schraube vollständig einschrauben.

[![](images/06-pitch-aktor/5adbaa-www.nerdiy.de-20200805-150203.jpg)](images/06-pitch-aktor/5adbaa-www.nerdiy.de-20200805-150203.jpg)

Andere Ansicht.

Später müssen Sie die Schraube wieder lösen, um das Zahnrad einzusetzen.

---

## Montage der vorbereiteten Teile

Jetzt können Sie mit der eigentlichen Montage beginnen.

[![](images/06-pitch-aktor/36f057-www.nerdiy.de-20200805-150338.jpg)](images/06-pitch-aktor/36f057-www.nerdiy.de-20200805-150338.jpg)

Für die Endmontage benötigen Sie nun die zuvor vorbereiteten Komponenten und die restlichen gezeigten Teile.

[![](images/06-pitch-aktor/c24cd3-www.nerdiy.de-20200805-150531.jpg)](images/06-pitch-aktor/c24cd3-www.nerdiy.de-20200805-150531.jpg)

Zuerst müssen Sie die M3-Muttern wie gezeigt in die Basis des Pitch-Aktuators einsetzen.

[![](images/06-pitch-aktor/3e3dc4-www.nerdiy.de-20200805-150534.jpg)](images/06-pitch-aktor/3e3dc4-www.nerdiy.de-20200805-150534.jpg)

Nahansicht der eingesetzten M3-Mutter.

[![](images/06-pitch-aktor/d77ec5-www.nerdiy.de-20200805-150537.jpg)](images/06-pitch-aktor/d77ec5-www.nerdiy.de-20200805-150537.jpg)

Weitere Nahansicht der eingesetzten M3-Mutter.

[![](images/06-pitch-aktor/0a4a75-www.nerdiy.de-20200805-150547.jpg)](images/06-pitch-aktor/0a4a75-www.nerdiy.de-20200805-150547.jpg)

Weitere Nahansicht der eingesetzten M3-Mutter.

[![](images/06-pitch-aktor/feb07f-www.nerdiy.de-20200805-150618.jpg)](images/06-pitch-aktor/feb07f-www.nerdiy.de-20200805-150618.jpg)

Als nächstes müssen Sie die M3-Schrauben wie gezeigt in den Getriebeträger einsetzen.

---

[![](images/06-pitch-aktor/f21d9f-www.nerdiy.de-20200805-150650.jpg)](images/06-pitch-aktor/f21d9f-www.nerdiy.de-20200805-150650.jpg)

Bis sie auf der gegenüberliegenden Seite aus dem Getriebeträger schauen.

[![](images/06-pitch-aktor/c39f05-www.nerdiy.de-20200805-150855.jpg)](images/06-pitch-aktor/c39f05-www.nerdiy.de-20200805-150855.jpg)

Sie können dann den Getriebeträger wie gezeigt in die Basis des Pitch-Aktuators einsetzen…

[![](images/06-pitch-aktor/55b30a-www.nerdiy.de-20200805-1509050.jpg)](images/06-pitch-aktor/55b30a-www.nerdiy.de-20200805-1509050.jpg)

… Und mit den zuvor eingesetzten M3-Muttern verschrauben.

[![](images/06-pitch-aktor/a15811-www.nerdiy.de-20200805-151101.jpg)](images/06-pitch-aktor/a15811-www.nerdiy.de-20200805-151101.jpg)

Weitere Ansicht der Schraubverbindungen.

[![](images/06-pitch-aktor/76b422-www.nerdiy.de-20200805-151108.jpg)](images/06-pitch-aktor/76b422-www.nerdiy.de-20200805-151108.jpg)

Fertig geschraubt sollte das Ganze so aussehen.

[![](images/06-pitch-aktor/7c518b-www.nerdiy.de-20200805-151121.jpg)](images/06-pitch-aktor/7c518b-www.nerdiy.de-20200805-151121.jpg)

Jetzt müssen Sie das zuvor vorbereitete Zahnrad in den Träger einsetzen.

[![](images/06-pitch-aktor/ef4ca0-www.nerdiy.de-20200805-151142.jpg)](images/06-pitch-aktor/ef4ca0-www.nerdiy.de-20200805-151142.jpg)

Dazu müssen Sie möglicherweise die Schraube wieder vom Getriebeträger lösen.

[![](images/06-pitch-aktor/e0dd0f-www.nerdiy.de-20200805-151220.jpg)](images/06-pitch-aktor/e0dd0f-www.nerdiy.de-20200805-151220.jpg)

Das Zahnrad kann nun wie gezeigt in die Aussparung eingesetzt werden.

Dann können Sie die Schraube wieder in den Getriebeträger und damit auch in das Loch des Kugellagers im Zahnrad einschrauben.

[![](images/06-pitch-aktor/b4cbd1-www.nerdiy.de-20200805-151243.jpg)](images/06-pitch-aktor/b4cbd1-www.nerdiy.de-20200805-151243.jpg)

Für die Lagerung des Zahnrades auf der anderen Seite benötigen Sie nun die abgebildeten Teile.

[![](images/06-pitch-aktor/12918b-www.nerdiy.de-20200805-151312.jpg)](images/06-pitch-aktor/12918b-www.nerdiy.de-20200805-151312.jpg)

Setzen Sie zuerst das Kugellager wie gezeigt in die Aussparung in der Basis ein.

[![](images/06-pitch-aktor/dd33eb-www.nerdiy.de-20200805-151319.jpg)](images/06-pitch-aktor/dd33eb-www.nerdiy.de-20200805-151319.jpg)

Der abgebildete Achsträger kann dann durch das Kugellager …

[![](images/06-pitch-aktor/846454-www.nerdiy.de-20200805-151342.jpg)](images/06-pitch-aktor/846454-www.nerdiy.de-20200805-151342.jpg)

… ins Zahnrad.

[![](images/06-pitch-aktor/fa48ba-www.nerdiy.de-20200805-151350.jpg)](images/06-pitch-aktor/fa48ba-www.nerdiy.de-20200805-151350.jpg)

Eine andere Ansicht des eingesetzten Achsträgers.

[![](images/06-pitch-aktor/0ff29b-www.nerdiy.de-20200805-151404.jpg)](images/06-pitch-aktor/0ff29b-www.nerdiy.de-20200805-151404.jpg)

Anschließend können Sie den eingesetzten Achsträger mit den vorbereiteten M3-Madenschrauben am Zahnrad festschrauben.

[![](images/06-pitch-aktor/8802b4-www.nerdiy.de-20200805-151417.jpg)](images/06-pitch-aktor/8802b4-www.nerdiy.de-20200805-151417.jpg)

Zusätzliche Ansicht.

---

## Getriebemotor einbauen

Um das Zahnrad später antreiben zu können ist natürlich ein Motor fühlen. Wie dieser Verbaut wird, könnt Ihr im folgenden Absatz sehen.

[![](images/06-pitch-aktor/7138de-www.nerdiy.de-20200805-151511.jpg)](images/06-pitch-aktor/7138de-www.nerdiy.de-20200805-151511.jpg)

Dafür benötigt Ihr zunächst die abgebildeten Teile.

[![](images/06-pitch-aktor/023e4b-www.nerdiy.de-20200805-151525.jpg)](images/06-pitch-aktor/023e4b-www.nerdiy.de-20200805-151525.jpg)

Steckt nun zunächst die Achse des Getriebemotors in den Achsträger.

[![](images/06-pitch-aktor/10116f-www.nerdiy.de-20200805-151536.jpg)](images/06-pitch-aktor/10116f-www.nerdiy.de-20200805-151536.jpg)

Der Motor sollte dann wie abgebildet in der Basis stecken.

[![](images/06-pitch-aktor/aa5202-www.nerdiy.de-20200805-151547.jpg)](images/06-pitch-aktor/aa5202-www.nerdiy.de-20200805-151547.jpg)

Damit dieser auch an Ort und Stelle bleibt könnt Ihr ihn nun mit den abgebildeten Schrauben in der Basis verschrauben.

[![](images/06-pitch-aktor/e779ac-www.nerdiy.de-20200805-151556.jpg)](images/06-pitch-aktor/e779ac-www.nerdiy.de-20200805-151556.jpg)

Steckt die Schrauben dazu bis zum Anschlag in das Motorgehäuse.

[![](images/06-pitch-aktor/cabfe0-www.nerdiy.de-20200805-151727.jpg)](images/06-pitch-aktor/cabfe0-www.nerdiy.de-20200805-151727.jpg)

Verschraubt werden die Schrauben auf der Rückseite mit den eingelegten M3 Muttern.

[![](images/06-pitch-aktor/a55a63-www.nerdiy.de-20200805-152023.jpg)](images/06-pitch-aktor/a55a63-www.nerdiy.de-20200805-152023.jpg)

Fertig montiert sollte das Ganze nun so aussehen.

[![](images/06-pitch-aktor/0c29b3-www.nerdiy.de-20200805-152202.jpg)](images/06-pitch-aktor/0c29b3-www.nerdiy.de-20200805-152202.jpg)

Um einen Ankerpunkt für die Welle zur Einstellung des Pitch-Winkels zu haben, müsst Ihr nun noch eine M6 Mutter in der Basis fixieren.

Dazu benötigt Ihr die abgebildeten Teile.

[![](images/06-pitch-aktor/453bb7-www.nerdiy.de-20200805-152301.jpg)](images/06-pitch-aktor/453bb7-www.nerdiy.de-20200805-152301.jpg)

Setzt zunächst drei M3 Muttern wie abgebildet in die Basis ein.

[![](images/06-pitch-aktor/47d6ed-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152310-2.jpg)](images/06-pitch-aktor/47d6ed-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152310-2.jpg)

Die M6 Mutter wird dann wie abgebildet eingesetzt.

[![](images/06-pitch-aktor/12bf4b-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152311-1.jpg)](images/06-pitch-aktor/12bf4b-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152311-1.jpg)

Fertig eingesetzt sollte das dann so aussehen.

[![](images/06-pitch-aktor/08b0e5-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152321-1.jpg)](images/06-pitch-aktor/08b0e5-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152321-1.jpg)

Damit die M6 Mutter nicht mehr herausfallen kann, könnt Ihr Sie mit der abgebildeten Platte sichern.

[![](images/06-pitch-aktor/d989a3-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152335-1.jpg)](images/06-pitch-aktor/d989a3-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152335-1.jpg)

Verschraubt die Platte dazu mit der Basis.

[![](images/06-pitch-aktor/2cc5a7-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152520-1.jpg)](images/06-pitch-aktor/2cc5a7-www.nerdiy.de-howto-windiy-pitchaktor-zusammenbauen-20200805-152520-1.jpg)

Ansicht der fertig verschraubten Platte.

---

## Verbindung des pitch Aktors mit der Basisplatte

Damit Ihr den Pitch Aktor korrekt montieren könnt, müsst Ihr diesen noch auf einer Basisplatte montieren. Dies ist im folgenden Absatz beschrieben.

[![](images/06-pitch-aktor/f8799f-www.nerdiy.de-20200805-152643.jpg)](images/06-pitch-aktor/f8799f-www.nerdiy.de-20200805-152643.jpg)

Dazu benötigt Ihr die abgebildeten Teile.

[![](images/06-pitch-aktor/6615e1-www.nerdiy.de-20200805-152921.jpg)](images/06-pitch-aktor/6615e1-www.nerdiy.de-20200805-152921.jpg)

Setzt nun vier M3 Muttern wie abgebildet in die Basis des pitch Aktors ein.

[![](images/06-pitch-aktor/d3eb7c-www.nerdiy.de-20200805-152958.jpg)](images/06-pitch-aktor/d3eb7c-www.nerdiy.de-20200805-152958.jpg)

Mithilfe von vier M3 Schrauben könnt Ihr die Basisplatte nun…

[![](images/06-pitch-aktor/3c4350-www.nerdiy.de-20200805-153110.jpg)](images/06-pitch-aktor/3c4350-www.nerdiy.de-20200805-153110.jpg)

…mit der Basis des pitch Aktors verschrauben.

[![](images/06-pitch-aktor/914adc-www.nerdiy.de-20200805-153115.jpg)](images/06-pitch-aktor/914adc-www.nerdiy.de-20200805-153115.jpg)

Fertig verschraubt sollte das Ganze dann so aussehen.

[![](images/06-pitch-aktor/0a733b-www.nerdiy.de-20200805-153120.jpg)](images/06-pitch-aktor/0a733b-www.nerdiy.de-20200805-153120.jpg)

Ansicht der anderen Seite.

---

## Leitungen anbringen und Schiebewiderstand einbauen

In diesem Schritt werden die Leitungen an den Motor angebracht und der Schiebewiderstand – über welchen später die Pitch-Position eingelesen kann – eingeklebt.

[![](images/06-pitch-aktor/9e796a-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144610.jpg)](images/06-pitch-aktor/9e796a-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144610.jpg)

Auf diesem Bild sind die Versorgungsleitungen des Getriebemotors bereits angelötet.

[![](images/06-pitch-aktor/744d15-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144614.jpg)](images/06-pitch-aktor/744d15-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144614.jpg)

Ich empfehle dringend, die Anschlusskontakte nach dem verlöten mit etwas Heißkleber zu sichern.

Nicht nur damit die Kontakte elektrisch isoliert sind. Sondern auch um die fragilen Kontaktfahnen vor mechanischer Belastung durch biegen zu schützen.

[![](images/06-pitch-aktor/0a3ff8-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144619.jpg)](images/06-pitch-aktor/0a3ff8-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144619.jpg)

Nun geht es an die Verdrahtung des Schiebewiderstandes.

Wie Ihr seht ist dieser hier schon verdrahtet.

[![](images/06-pitch-aktor/5c89c8-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144624.jpg)](images/06-pitch-aktor/5c89c8-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144624.jpg)

Dazu benötigt Ihr drei Leitungen und drei ca. zwei cm lange Schrumpfschlauch-Stücke.

Auf der dargestellten Seite wird der Kontakt des Schleifers mit einer Leitung verbunden.

[![](images/06-pitch-aktor/5d4977-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144626.jpg)](images/06-pitch-aktor/5d4977-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144626.jpg)

Auf der anderen Seite werden die beiden Kontakte des Widerstands an jeweils eine Leitung angeschlossen.

[![](images/06-pitch-aktor/00b716-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144635.jpg)](images/06-pitch-aktor/00b716-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144635.jpg)

Nahansicht der angeschlossenen Widerstandskontakte.

[![](images/06-pitch-aktor/b9b5fa-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144640.jpg)](images/06-pitch-aktor/b9b5fa-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144640.jpg)

Nahansicht des angeschlossenen Schleiferkontakts.

[![](images/06-pitch-aktor/f8d736-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144646.jpg)](images/06-pitch-aktor/f8d736-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144646.jpg)

Weitere Ansicht.

[![](images/06-pitch-aktor/a55f47-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144704.jpg)](images/06-pitch-aktor/a55f47-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144704.jpg)

Auf dem Schleifer könnt Ihr noch einen Adapter abringen.

[![](images/06-pitch-aktor/a2e2a6-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144712.jpg)](images/06-pitch-aktor/a2e2a6-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144712.jpg)

Steckt diesen dazu einfach auf die Metallfläche des Schleifers.

[![](images/06-pitch-aktor/c8e196-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144713.jpg)](images/06-pitch-aktor/c8e196-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144713.jpg)

Nahansicht des aufgesteckten Adapters auf die Metallfläche des Schleifers.

[![](images/06-pitch-aktor/726fa0-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144758.jpg)](images/06-pitch-aktor/726fa0-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144758.jpg)

Nachdem der Schiebewiderstand verdrahtet ist, könnt Ihr ihn mit einem Tropfen Heißkleber in der dafür vorgesehenen Halterung einkleben.

[![](images/06-pitch-aktor/a12a76-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144813.jpg)](images/06-pitch-aktor/a12a76-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144813.jpg)

Die Leitungen sollten Dabei wie abgebildet aus der Halterung verlaufen.

[![](images/06-pitch-aktor/7d0002-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144820.jpg)](images/06-pitch-aktor/7d0002-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144820.jpg)

Nun ist der Aufbau des Pitch Aktors soweit abgeschlossen.

[![](images/06-pitch-aktor/008bf9-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144823.jpg)](images/06-pitch-aktor/008bf9-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144823.jpg)

Weitere Ansicht.

[![](images/06-pitch-aktor/deacff-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144826.jpg)](images/06-pitch-aktor/deacff-www.nerdiy.de-howto-windiy-pitch-aktor-zusammenbauen-20201003-144826.jpg)

Weitere Ansicht.

---

## Viel Spaß mit dem Projekt

Ich hoffe bei euch hat alles wie beschrieben funktioniert. Falls nicht oder ihr Fragen oder Anregungen habt lasst es mich in den Kommentaren bitte wissen. Ich trage dies dann ggf. in den Artikel nach.  
Auch Ideen für neue Projekte sind immer gerne willkommen. 🙂

**P.S. Viele dieser Projekte - besonders die Hardwareprojekte - kosten viel Zeit und Geld. Natürlich mache ich das weil ich Spaß daran habe, aber wenn Du es cool findest, dass ich die Infos dazu mit Euch teile, würde ich mich über eine kleine Spende an die Kaffeekasse freuen. 🙂**
