---
title: "HowTo: WinDIY – Nabe inkl. Mechanik aufbauen"
source: https://nerdiy.de/howto-windiy-nabe-inkl-mechanik-aufbauen/
retrieved: 2026-11-04
---

# HowTo: WinDIY – Nabe inkl. Mechanik aufbauen

An der einen oder anderen Stelle habe ich bestimmt schon erwähnt, dass es mir wichtig war WinDIY sicher steuern und im Notfall auch dessen Drehzahl begrenzen zu können.

Dazu habe ich eine Mechanik entwickelt die es ermöglicht den Anstellwinkel der Flügel einzustellen. So können die Flügel an die aktuelle Wind- und Rotationsgeschwindigkeit angepasst werden. Außerdem können sie so bei Starkwind auch aus dem Wind gedreht werden.

So lässt sich die Drehzahl und die Belastung von WinDIY steuern.

Ein paar zusätzliche Infos dazu habe ich hier aufgeschrieben: [***https://hackaday.io/project/172328-windiy-hawt-wind-turbine/log/179105-windiys-hub-oh-my-god-mechanics***](https://hackaday.io/project/172328-windiy-hawt-wind-turbine/log/179105-windiys-hub-oh-my-god-mechanics)

Im folgenden Artikel findet Ihr die Anleitung um die Mechanik zur Einstellung des Flügel-Anstellwinkels nachzubauen.

---

## Sicherheitshinweise

Ich weiß die folgenden Hinweise sind immer irgendwie lästig und wirken unnötig. Aber leider haben schon viele Menschen die es "besser" wussten aus Leichtsinnigkeit Augen, Finger oder anderes verloren bzw. sich verletzt. Im Vergleich dazu ist ein Datenverlust fast nicht der Rede Wert, aber auch diese können echt ärgerlich sein. Deswegen nehmt Euch bitte fünf Minuten Zeit um die Sicherheitshinweise zu lesen. Denn auch das coolste Projekt ist keine Verletzung oder anderen Ärger wert.  
***<https://www.nerdiy.de/sicherheitshinweise/>***

## Affiliatelinks/Werbelinks

*Die hier in aufgeführten Links zu Online-Shops sind sogenannte Affiliate-Links. Wenn Du auf so einen Affiliate-Link klickst und über diesen Link einkaufst, bekommt Nerdiy.de von dem betreffenden Online-Shop oder Anbieter eine Provision. Für Dich verändert sich der Preis nicht. Falls Du Deine Einkäufe über diese Links tätigst unterstützt Du Nerdiy.de dabei auch in Zukunft weitere nützliche Projekte anbieten zu können. 🙂*

---

## Voraussetzungen

**Benötigtes Werkzeug:**

|  |
| --- |
| Heißklebepistole |
| 3D Drucker |
| Innensechskantschlüssel |
| Zange |
| Maulschlüssel |
| Akkubohrer |
| 3mm Bohrer |
| Pinzette |

**Benötigtes Material:**

**In der folgenden Liste findet Ihr alle Teile die Ihr zur Umsetzung dieses Artikels benötigt.**

|  |  |
| --- | --- |
| 3x | pitchArm |
| 3x | pitchLever |
| 3x | pitchArmNutSecuring |
| 1x | hubBase |
| 1x | pitchLeverDisk |
| 1x | hubCover |
| 1x | hubBearingCap |
| 9x | 603ZZ Kugellager |
| 8x | 606ZZ Kugellager |
| 5x | M6 selbst sichernde Mutter |
| 6x | M6 Mutter |
| 3x | M3x20 Zylinderkopfschraube |
| 3x | M3 selbst sichernde Mutter |
| 15x | M3 Mutter |
| 3x | M3x30 Senkkopfschraube |
| 3x | M3x16 Senkkopfschraube |
| 6x | M3x40 Senkkopfschraube |
| 3x | Vorbereitete Flügelsteckplatz |
| 1x | M6 Gewindestange 60cm lang |

---

## Benötigte Teile sammeln

Bevor es mit dem Aufbau der Nabe und dessen Mechanik losgehen kann, müsst Ihr natürlich zunächst alle benötigten Teile zusammen haben. Eine komplette Liste der benötigten Materialien und Werkzeuge findet Ihr weiter oben in der Material- und Werkzeugliste

[![](images/03-nabe/23923d-www.nerdiy.de-20200609-170147.jpg)](images/03-nabe/23923d-www.nerdiy.de-20200609-170147.jpg)

Auf diesem Bild seht Ihr alle Bauteile die zum Aufbau der Naben-Mechanik benötigt werden.

Die benötigten STL-Dateien zum Ausdrucken findet Ihr hier: ***<https://github.com/Nerdiyde/WinDIY/tree/master/hub>***

Ich habe die Teile mit den Folgenden Einstellungen gedruckt.

- Perimeter: 5
- Infill: 50%

**Die Schrauben sollten am besten aus Edelstahl sein, damit sie durch Feuchtigkeit nicht rosten.**

---

## Naben Basis auf der Achse montieren

Als erstes muss die Naben-Basis mit der Achse verbunden werden. Das macht die weitere Montage eigentlich etwas komplizierter. Leider muss dies aber direkt am Anfang passieren, da die Schraubenlöcher welche bei der Montage genutzt werden, später nur noch schwer erreichbar sind.

[![](images/03-nabe/808435-www.nerdiy.de-20200612-103811.jpg)](images/03-nabe/808435-www.nerdiy.de-20200612-103811.jpg)

Dafür benötigt Ihr zunächst die abgebildeten Teile.

Die Achse, die Naben-Basis, 3x M3 Mutter und 3x M3x50 Senkkopfschrauben.

[![](images/03-nabe/0b2feb-www.nerdiy.de-20200612-103900.jpg)](images/03-nabe/0b2feb-www.nerdiy.de-20200612-103900.jpg)

Damit die Schrauben zur Befestigung der Achse halten, müsst Ihr zunächst eine M3 Mutter wie abgebildet in die Achse einlegen.

[![](images/03-nabe/4ee5cd-www.nerdiy.de-20200612-103902.jpg)](images/03-nabe/4ee5cd-www.nerdiy.de-20200612-103902.jpg)

Je nach Druckqualität Eures Druckers kann es sein, dass Ihr die Mutter etwas in die richtige Position „zwingen“ müsst.

[![](images/03-nabe/e02445-www.nerdiy.de-20200612-103910.jpg)](images/03-nabe/e02445-www.nerdiy.de-20200612-103910.jpg)

Nun könnt Ihr die erste M3x50 Schraube durch das Loch in der Naben-Basis stecken.

[![](images/03-nabe/c7356b-www.nerdiy.de-20200612-103923.jpg)](images/03-nabe/c7356b-www.nerdiy.de-20200612-103923.jpg)

Weitere Ansicht der eingesteckten Schraube.

[![](images/03-nabe/4e980d-www.nerdiy.de-20200612-103958.jpg)](images/03-nabe/4e980d-www.nerdiy.de-20200612-103958.jpg)

Die eingesteckte Schraube sollte dann …

[![](images/03-nabe/38de6d-www.nerdiy.de-20200612-104006.jpg)](images/03-nabe/38de6d-www.nerdiy.de-20200612-104006.jpg)

… wie abgebildet in die Achse eingesteckt und mit der zuvor eingelegten Mutter verschraubt werden.

[![](images/03-nabe/718853-www.nerdiy.de-20200612-104033.jpg)](images/03-nabe/718853-www.nerdiy.de-20200612-104033.jpg)

Nachdem Ihr die Achse nun zunächst provisorisch mit einer Schraube fixiert habt, könnt Ihr die anderen Muttern…

[![](images/03-nabe/8bb5ac-www.nerdiy.de-20200612-104136.jpg)](images/03-nabe/8bb5ac-www.nerdiy.de-20200612-104136.jpg)

…in die Aussparungen in der Achse einlegen.

[![](images/03-nabe/a96f1b-www.nerdiy.de-20200612-104653.jpg)](images/03-nabe/a96f1b-www.nerdiy.de-20200612-104653.jpg)

Danach könnt Ihr die übrigen Schrauen in die Naben Basis einstecken und mit den Muttern in der Achse verschrauben.

Die Achse sollte nun also über drei M3x50 Senkkopfschrauben mit der Naben-Basis verschraubt sein.

---

## Den ersten Flügelsteckplatz montieren

Die Flügel werden nicht direkt mit der Nabe verbunden. Zunächst werden nur die Steckplätze mit der Nabe verbunden. Später können die Flügel dann darauf eingesteckt werden.

[![](images/03-nabe/984cdf-www.nerdiy.de-20200612-104701.jpg)](images/03-nabe/984cdf-www.nerdiy.de-20200612-104701.jpg)

Setzt dazu das erste 606ZZ Kugellager wie abgebildet von außen in die Aussparung der Naben-Basis.

[![](images/03-nabe/7d4cb4-www.nerdiy.de-20200612-104706.jpg)](images/03-nabe/7d4cb4-www.nerdiy.de-20200612-104706.jpg)

Auf der gegenüberliegenden Innenseite wird dann…

[![](images/03-nabe/d04b84-www.nerdiy.de-20200612-104716.jpg)](images/03-nabe/d04b84-www.nerdiy.de-20200612-104716.jpg)

…das zweite Kugellager eingelegt.

[![](images/03-nabe/e1f137-www.nerdiy.de-20200612-104829.jpg)](images/03-nabe/e1f137-www.nerdiy.de-20200612-104829.jpg)

Nun könnt Ihr den ersten Flügelsteckplatz einstecken.

Diesen Flügelsteckplatz solltet Ihr bereits während des Aufbaus des Flügels vorbereitet haben.

[![](images/03-nabe/785331-www.nerdiy.de-20200612-104833.jpg)](images/03-nabe/785331-www.nerdiy.de-20200612-104833.jpg)

Dies sollte dann so aussehen.

[![](images/03-nabe/d6b160-www.nerdiy.de-20200612-104917.jpg)](images/03-nabe/d6b160-www.nerdiy.de-20200612-104917.jpg)

Die erste Sicherung des Flügels besteht aus einer selbst sichernden M6 Mutter, welche auf die M6x100 Schraube des Flügelsteckplatzes aufgeschraubt wird.

[![](images/03-nabe/8c1424-www.nerdiy.de-20200612-105004.jpg)](images/03-nabe/8c1424-www.nerdiy.de-20200612-105004.jpg)

Fertig aufgeschraubt sollte dies so aussehen.

Die Mutter sollte dabei so fest sitzen, dass sich der Flügelsteckplatz in Schraubenrichtung nicht mehr bewegen lässt. Gleichzeitig sollte dieser aber natürlich noch drehbar gelagert sein.

[![](images/03-nabe/28b470-www.nerdiy.de-20200612-105015.jpg)](images/03-nabe/28b470-www.nerdiy.de-20200612-105015.jpg)

Das nächste Kugellager wird nun auf der Innenseite der Nabe eingesetzt.

[![](images/03-nabe/4fa38c-www.nerdiy.de-20200612-105035.jpg)](images/03-nabe/4fa38c-www.nerdiy.de-20200612-105035.jpg)

Schiebt das 606ZZ Kugellager dazu über die M6x100 Schraube in die Aussparung in der Innenseite der Naben-Basis…

[![](images/03-nabe/18df44-www.nerdiy.de-20200612-105103.jpg)](images/03-nabe/18df44-www.nerdiy.de-20200612-105103.jpg)

…und sichert diese wieder mit mit einer (normalen) M6 Mutter.

[![](images/03-nabe/c7c362-www.nerdiy.de-20200612-105109.jpg)](images/03-nabe/c7c362-www.nerdiy.de-20200612-105109.jpg)

Weitere Ansicht der aufgeschraubten M6 Mutter auf der M6x100 Schraube des Flügelsteckplatzes.

---

## Hebel anbringen und korrekt einstellen

Nun kommt ein etwas kritischer Schritt, bei dem Ihr möglichst Genau arbeiten solltet. Ehrlich gesagt bin ich mit der Montage des Hebels auf der M6x100 Schraube des Flügelsteckplatzes noch nicht richtig zufrieden. Dieser wird nämlich durch das verklemmen zwischen Zwei Muttern auf der Schraube gesichert. Theoretisch sollte das halten. Praktisch tut es das auch. Allerdings wäre es sicherer hier z.B. noch einen Splint durch die M6x100 Schraube zu stecken. Hier gibt es sicherlich Platz für zukünftige Verbesserungen. 🙂

[![](images/03-nabe/3e70d5-www.nerdiy.de-20200612-105229.jpg)](images/03-nabe/3e70d5-www.nerdiy.de-20200612-105229.jpg)

Zur korrekten Einstellung des Hebels solltet Ihr die Naben-Basis nun etwas höher lagern. Ich habe sie zum Beispiel auf zwei Kartons gestellt.

[![](images/03-nabe/9befc2-www.nerdiy.de-howto-windiy-nabe-inkl-mechanik-zusammenbauen-20200612-105231.jpg)](images/03-nabe/9befc2-www.nerdiy.de-howto-windiy-nabe-inkl-mechanik-zusammenbauen-20200612-105231.jpg)

Ziel ist es, dass die Hinterkante des Flügelsteckplatzes genau auf der gleichen Höhe liegt wie die Rückseite der Naben-Basis.

[![](images/03-nabe/d7587e-www.nerdiy.de-20200612-105236.jpg)](images/03-nabe/d7587e-www.nerdiy.de-20200612-105236.jpg)

Habt Ihr den Flügelsteckplatz korrekt eingestellt, könnt Ihr nun den Hebel auf die Achse und auf die zuvor aufgeschraubte M6 Mutter aufstecken. Die Mutter sollte dabei so eng wie möglich am Kugellager anliegen, der ganze Flügelsteckplatz sich aber trotzdem noch frei drehen lassen.

Sobald der Hebel korrekt aufgesteckt ist…

[![](images/03-nabe/eb8d97-www.nerdiy.de-20200612-105240.jpg)](images/03-nabe/eb8d97-www.nerdiy.de-20200612-105240.jpg)

…könnt Ihr dessen Ausrichtung mit einer M3 Schraube provisorisch (die Schraube wird nachher wieder entfernt) in der Naben-Basis sichern. (siehe Bild)

[![](images/03-nabe/a856e7-www.nerdiy.de-20200612-105326.jpg)](images/03-nabe/a856e7-www.nerdiy.de-20200612-105326.jpg)

Ansicht des gesicherten und ausgerichteten Hebels.

---

## Führungs-Kugellager einbauen

In diesem Schritt wird das Kugellager eingebaut, dass die Schubstange zur Einstellung des Flügel-Anstellwinkels ermöglicht. Eigentlich hätte man diesen Schritt auch schon vor dem Einbau des Flügel-Hebels durchführen können.

[![](images/03-nabe/15db25-www.nerdiy.de-20200612-122405.jpg)](images/03-nabe/15db25-www.nerdiy.de-20200612-122405.jpg)

Setzt dazu das 606ZZ Kugellager…

[![](images/03-nabe/564eba-www.nerdiy.de-20200612-122408.jpg)](images/03-nabe/564eba-www.nerdiy.de-20200612-122408.jpg)

…in die Aussparung in der Naben-Basis ein.

[![](images/03-nabe/85947a-www.nerdiy.de-20200612-122420.jpg)](images/03-nabe/85947a-www.nerdiy.de-20200612-122420.jpg)

Das Kugellager wird dann mit der gezeigten Klemme in der Naben-Basis verklemmt.

[![](images/03-nabe/a5266b-www.nerdiy.de-20200612-122424.jpg)](images/03-nabe/a5266b-www.nerdiy.de-20200612-122424.jpg)

Nahansicht.

[![](images/03-nabe/32e309-www.nerdiy.de-20200612-122500.jpg)](images/03-nabe/32e309-www.nerdiy.de-20200612-122500.jpg)

Die Schraube zum verklemmen des Kugellagers wird dabei mithilfe einer Mutter in der Achse gesichert.

[![](images/03-nabe/485e87-www.nerdiy.de-20200612-122633.jpg)](images/03-nabe/485e87-www.nerdiy.de-20200612-122633.jpg)

Wiederhohlt dies nun noch zwei Mal…

[![](images/03-nabe/0e2bcb-www.nerdiy.de-20200612-122644.jpg)](images/03-nabe/0e2bcb-www.nerdiy.de-20200612-122644.jpg)

Bis das Kugellager über insgesamt drei Klemmen verklemmt ist.

[![](images/03-nabe/fe074d-www.nerdiy.de-20200612-122653.jpg)](images/03-nabe/fe074d-www.nerdiy.de-20200612-122653.jpg)

Weitere Ansicht des verklemmten Kugellagers.

[![](images/03-nabe/5c4427-www.nerdiy.de-20200612-122747.jpg)](images/03-nabe/5c4427-www.nerdiy.de-20200612-122747.jpg)

Draufsicht des verklemmten Kugellagers und einem montierten Hebel.

---

## Die restlichen zwei Flügel an der Nabe montieren

Nachdem das Kugellager zur Führung der Schubstange in der Naben-Basis montiert ist, könnt Ihr mit der Montage der restlichen zwei Flügel-Steckplätze fortfahren. Diese werden genau nach dem gleichen Verfahren wie der erste Flügel-Steckplatz montiert.

[![](images/03-nabe/745a54-www.nerdiy.de-20200612-123947.jpg)](images/03-nabe/745a54-www.nerdiy.de-20200612-123947.jpg)

Sobald alle drei Flügel-Steckplätze montiert sind, sollte Eurer bisheriger Aufbau nun so aussehen.

[![](images/03-nabe/4a1b56-www.nerdiy.de-20200612-123950.jpg)](images/03-nabe/4a1b56-www.nerdiy.de-20200612-123950.jpg)

Nahansicht der drei montierten Flügel-Steckplätze inkl. Hebel.

[![](images/03-nabe/dc245b-www.nerdiy.de-20200612-123952.jpg)](images/03-nabe/dc245b-www.nerdiy.de-20200612-123952.jpg)

Nahansicht der drei montierten Flügel-Steckplätze inkl. Hebel.

[![](images/03-nabe/e63eb9-www.nerdiy.de-20200612-123955.jpg)](images/03-nabe/e63eb9-www.nerdiy.de-20200612-123955.jpg)

Nahansicht der drei montierten Flügel-Steckplätze inkl. Hebel.

[![](images/03-nabe/5dbe8c-www.nerdiy.de-hub-20200612-132136.jpg)](images/03-nabe/5dbe8c-www.nerdiy.de-hub-20200612-132136.jpg)

Nahansicht der drei montierten Flügel-Steckplätze inkl. Hebel.

---

## Die Mutter-Sicherung anbringen

Wie bereits oben erwähnt, werden die Hebel zur Einstellung des Flügel-Anstellwinkels auf der M6x100 Schraube des jeweiligen Flügelsteckplatzes verklemmt. Damit sich die innere Mutter danach nicht mehr lösen kann (und somit der Hebel keine Wirkung mehr auf die Drehung des Flügels hätte) solltet Ihr diese Mutter nun dringend gegen eine Verdrehung sichern.

[![](images/03-nabe/9d95d5-www.nerdiy.de-hub-20200612-132141.jpg)](images/03-nabe/9d95d5-www.nerdiy.de-hub-20200612-132141.jpg)

Bevor Ihr die Mutter sichert, solltet Ihr nochmal sicherstellen, dass die innen liegende Mutter so fest wie möglich angezogen ist.

Dabei sollte die Einstellung des Hebels aber natürlich nicht verändert werden.

Prüft also erst, dass der Winkel des Hebels zum Flügel-Steckplatz stimmt und zieht dann die Mutter so fest wie möglich.

„Fest wie möglich“ heißt hier so fest, dass Ihr es „per Hand“ unter Einsatz eines Schraubenschlüssels nicht mehr fester bekommt.

[![](images/03-nabe/e2d35f-www.nerdiy.de-hub-20200612-132150.jpg)](images/03-nabe/e2d35f-www.nerdiy.de-hub-20200612-132150.jpg)

Nun benötigt Ihr eine M3x20 zylinderkopfschraube, eine M3 Mutter und das 3D gedruckte Kunststoffteil zur Sicherung des Hebels.

[![](images/03-nabe/2b8f8d-www.nerdiy.de-hub-20200612-132241.jpg)](images/03-nabe/2b8f8d-www.nerdiy.de-hub-20200612-132241.jpg)

Legt nun die Sicherung wie abgebildet über die M6 Mutter…

[![](images/03-nabe/0548ab-www.nerdiy.de-hub-20200612-132245.jpg)](images/03-nabe/0548ab-www.nerdiy.de-hub-20200612-132245.jpg)

…und sichert Sie mit der M3x10 Schraube indem…

[![](images/03-nabe/411eb5-www.nerdiy.de-hub-20200612-132250.jpg)](images/03-nabe/411eb5-www.nerdiy.de-hub-20200612-132250.jpg)

…Ihr sie mit der M3 Mutter auf der Rückseite des Hebels verschraubt.

[![](images/03-nabe/e81283-www.nerdiy.de-hub-20200612-1419360.jpg)](images/03-nabe/e81283-www.nerdiy.de-hub-20200612-1419360.jpg)

Wiederholt dies nun wieder für alle drei Flügel-Steckplätze.

[![](images/03-nabe/a39936-www.nerdiy.de-hub-20200612-141939.jpg)](images/03-nabe/a39936-www.nerdiy.de-hub-20200612-141939.jpg)

Nahansicht der Hebel inklusive angebrachter Sicherungen.

[![](images/03-nabe/eac0b2-www.nerdiy.de-hub-20200612-141946.jpg)](images/03-nabe/eac0b2-www.nerdiy.de-hub-20200612-141946.jpg)

Nahansicht der Hebel inklusive angebrachter Sicherungen.

[![](images/03-nabe/00e66d-www.nerdiy.de-hub-20200612-141956.jpg)](images/03-nabe/00e66d-www.nerdiy.de-hub-20200612-141956.jpg)

Nun könnt Ihr auch prüfen, dass die Hebel den korrekten Winkel zu den Flügel-Steckplätzen haben.

Wenn die Flügel-Steckplätze gerade stehen (so wie auf dem Bild dargestellt)…

[![](images/03-nabe/f4b502-www.nerdiy.de-hub-20200612-141958.jpg)](images/03-nabe/f4b502-www.nerdiy.de-hub-20200612-141958.jpg)

—sollten die Hebel an den Anschlägen der Naben-Basis anschlagen. Der Drehwinkel der Flügel-Steckplätze ist also in einer Richtung begrenzt.

[![](images/03-nabe/7503e1-www.nerdiy.de-hub-20200612-142001.jpg)](images/03-nabe/7503e1-www.nerdiy.de-hub-20200612-142001.jpg)

Weitere Ansicht.

---

## „Hebelstrecker“ anbringen

(Btw: Manchmal nicht leicht für die einzelnen Teile passende Namen zu finden. 🙂 )

In diesem Abschnitt geht es darum an den zuvor montierten Hebeln den „Hebelstrecker“ anzubringen. Dieser Ist Teil der Mechanik, welche aus den vor- und zurück-Bewegungen der Schubstange später eine Drehbewegung für den Flügel macht.

[![](images/03-nabe/5a1939-www.nerdiy.de-hub-20200612-142026.jpg)](images/03-nabe/5a1939-www.nerdiy.de-hub-20200612-142026.jpg)

Hierzu benötigt Ihr zunächst einen 3D gedruckten Hebelstrecker, eine M3x20 Zylinderkopfschraube und eine selbst sichernde M3 Mutter.

[![](images/03-nabe/bb6bb9-www.nerdiy.de-hub-20200612-142056.jpg)](images/03-nabe/bb6bb9-www.nerdiy.de-hub-20200612-142056.jpg)

Montiert den Hebelstrecker nun wie abgebildet am ersten Hebel.

[![](images/03-nabe/e89204-www.nerdiy.de-hub-20200612-142058.jpg)](images/03-nabe/e89204-www.nerdiy.de-hub-20200612-142058.jpg)

Weitere Ansicht des montierten Hebelstrecker.

[![](images/03-nabe/9568e0-www.nerdiy.de-hub-20200612-142137.jpg)](images/03-nabe/9568e0-www.nerdiy.de-hub-20200612-142137.jpg)

Weitere Ansicht des montierten Hebelstrecker.

[![](images/03-nabe/e7dd48-www.nerdiy.de-hub-20200612-142349.jpg)](images/03-nabe/e7dd48-www.nerdiy.de-hub-20200612-142349.jpg)

habt Ihr den ersten Hebelstrecker montiert, könnt Ihr dies für die übrigen beiden Hebel wiederholen.

[![](images/03-nabe/9100ac-www.nerdiy.de-hub-20200612-142351.jpg)](images/03-nabe/9100ac-www.nerdiy.de-hub-20200612-142351.jpg)

Nahansicht der montierten (und eingeklappten) Hebelstrecker auf den Hebeln.

[![](images/03-nabe/8882f5-www.nerdiy.de-hub-20200612-142403.jpg)](images/03-nabe/8882f5-www.nerdiy.de-hub-20200612-142403.jpg)

Nahansicht der montierten (und ausgeklappten) Hebelstrecker auf den Hebeln.

---

## Hebelplatte anbringen

Hier kommt das nächste wichtige Teil für die Mechanik zur Einstellung des Anstellwinkels: Die „Hebelplatte“.

[![](images/03-nabe/251166-www.nerdiy.de-hub-20200612-142602.jpg)](images/03-nabe/251166-www.nerdiy.de-hub-20200612-142602.jpg)

Hierzu benötigt Ihr die Hebelplatte, drei M3 Muttern und drei M3x30 Senkkopfschrauben.

[![](images/03-nabe/295d37-www.nerdiy.de-hub-20200612-142626.jpg)](images/03-nabe/295d37-www.nerdiy.de-hub-20200612-142626.jpg)

Montiert die Hebelplatte nun wie abgebildet auf dem ersten Hebelstrecker…

[![](images/03-nabe/3e922e-www.nerdiy.de-hub-20200612-142641.jpg)](images/03-nabe/3e922e-www.nerdiy.de-hub-20200612-142641.jpg)

…und fixiert ihn indem Ihr die M3x30 Schraube von außen in die Hebelplatte steckt.

[![](images/03-nabe/5b4b3b-www.nerdiy.de-hub-20200612-142656.jpg)](images/03-nabe/5b4b3b-www.nerdiy.de-hub-20200612-142656.jpg)

Damit Ihr die Schraube nun auch fixieren könnt, müsst Ihr nun noch eine M3 Mutter in die Aussparung auf der Oberseite der Hebelplatte stecken.

[![](images/03-nabe/28badc-www.nerdiy.de-hub-20200612-142716.jpg)](images/03-nabe/28badc-www.nerdiy.de-hub-20200612-142716.jpg)

Komplett eingesteckt solltet Ihr von der M3 Mutter dann nicht mehr viel sehen können.

[![](images/03-nabe/398cdf-www.nerdiy.de-hub-20200612-142735.jpg)](images/03-nabe/398cdf-www.nerdiy.de-hub-20200612-142735.jpg)

Nun könnt Ihr die M3x30 Senkkopfschraube in die Mutter einschrauben.

[![](images/03-nabe/ed9f88-www.nerdiy.de-hub-20200612-142845.jpg)](images/03-nabe/ed9f88-www.nerdiy.de-hub-20200612-142845.jpg)

Wiederholt dies für die restlichen zwei Hebelstrecker.

[![](images/03-nabe/4e146d-www.nerdiy.de-hub-20200612-142856.jpg)](images/03-nabe/4e146d-www.nerdiy.de-hub-20200612-142856.jpg)

Wenn Ihr die Hebelplatte nun vor und zurück bewegt solltet Ihr schon bemerken, dass die Flügel sich dem Abstand der hebelplatte entsprechend einstellen lassen.

[![](images/03-nabe/f3d031-www.nerdiy.de-hub-20200612-142902.jpg)](images/03-nabe/f3d031-www.nerdiy.de-hub-20200612-142902.jpg)

Ansicht der eingeklappten Hebelplatte.

---

## Kugellager am Ankerpunkt einsetzen

Bisher haben wir ein Kugellager eingesetzt, dass zur Führung der Schubstange gedacht ist.

Nun wird das Kugellager montiert, über das die Schubbewegung der Schubstange auf die Hebelplatte übertragen wird.

[![](images/03-nabe/8ebc05-www.nerdiy.de-hub-20200612-143007.jpg)](images/03-nabe/8ebc05-www.nerdiy.de-hub-20200612-143007.jpg)

Dazu benötigt Ihr die Kugellager-Sicherungsplatte, ein 606ZZ Kugellager, drei M3x16 Zylinderschrauben und drei M3 Muttern.

[![](images/03-nabe/8df948-www.nerdiy.de-hub-20200612-143101.jpg)](images/03-nabe/8df948-www.nerdiy.de-hub-20200612-143101.jpg)

Setzt nun das 606Zz Kugellager in die Aussparung in der Hebelplatte ein.

[![](images/03-nabe/a0ef21-www.nerdiy.de-hub-20200612-143107.jpg)](images/03-nabe/a0ef21-www.nerdiy.de-hub-20200612-143107.jpg)

Nahansicht des eingesetzten Kugellagers.

[![](images/03-nabe/eb4d9d-www.nerdiy.de-hub-20200612-143135.jpg)](images/03-nabe/eb4d9d-www.nerdiy.de-hub-20200612-143135.jpg)

Sichert das Kugellager nun in seiner Position indem Ihr die Kugellager-Sicherungsplatte inkl. der drei M3x16 Zylinderkopfschrauben auf der Hebelplatte montiert.

[![](images/03-nabe/65176e-www.nerdiy.de-hub-20200612-143313.jpg)](images/03-nabe/65176e-www.nerdiy.de-hub-20200612-143313.jpg)

Die Schrauben werden dabei gesichert indem Ihr sie in die Aussparungen auf der Unterseite der Hebelplatte einlegt.

[![](images/03-nabe/4f8897-www.nerdiy.de-hub-20200612-143316.jpg)](images/03-nabe/4f8897-www.nerdiy.de-hub-20200612-143316.jpg)

Weitere Ansicht.

---

## Stabilisierungsring anbringen

Um der Naben-Basis etwas mehr Stabilität zu verleihen wird nun noch ein Stabilisierungsring auf der Naben-Basis montiert.

[![](images/03-nabe/28efed-www.nerdiy.de-hub-20200612-143440.jpg)](images/03-nabe/28efed-www.nerdiy.de-hub-20200612-143440.jpg)

Dazu benötigt Ihr den 3D gedruckten Stabilisierungsring, sechs M3 Muttern und sechs M3x40 Senkkopfschrauben.

[![](images/03-nabe/58fc73-www.nerdiy.de-hub-20200612-143529.jpg)](images/03-nabe/58fc73-www.nerdiy.de-hub-20200612-143529.jpg)

Der Stabilisierungsring wird nun von oben auf die Naben-Basis aufgelegt…

[![](images/03-nabe/ebc441-www.nerdiy.de-hub-20200612-143637.jpg)](images/03-nabe/ebc441-www.nerdiy.de-hub-20200612-143637.jpg)

…und mit den M3x40 Senkkopfschrauben wie abgebildet in der Naben-Basis verschraubt.

[![](images/03-nabe/983263-www.nerdiy.de-hub-20200612-144245.jpg)](images/03-nabe/983263-www.nerdiy.de-hub-20200612-144245.jpg)

Dazu verschraubt Ihr die M3x40 Schrauben in den Muttern, welche in die Aussparungen auf der Unterseite der Naben-Basis eingelegt werden.

[![](images/03-nabe/43c1c2-www.nerdiy.de-hub-20200612-144246.jpg)](images/03-nabe/43c1c2-www.nerdiy.de-hub-20200612-144246.jpg)

Nahansicht der eingelegten M3 Muttern.

[![](images/03-nabe/d216b2-www.nerdiy.de-hub-20200612-144249.jpg)](images/03-nabe/d216b2-www.nerdiy.de-hub-20200612-144249.jpg)

Nahansicht der eingelegten M3 Muttern.

---

## Schubstange anbringen

Die Schubstange besteht aus einer M6 Gewindestange. Sie wird später die durch den pitch Aktor erzeugte Schubbewegung auf die Mechanik in der Nabe übertragen.

[![](images/03-nabe/97a124-www.nerdiy.de-hub-20200612-144412.jpg)](images/03-nabe/97a124-www.nerdiy.de-hub-20200612-144412.jpg)

An dieser Stelle benötigt Ihr die zuvor vorbereitete Naben-Basis inkl. anbauten sowie zwei selbst sichernde M6 Muttern und eine M6 Gewindestange.

[![](images/03-nabe/e7b327-www.nerdiy.de-hub-20200612-144435.jpg)](images/03-nabe/e7b327-www.nerdiy.de-hub-20200612-144435.jpg)

Schiebt die Gewindestange nun wie abgebildet durch das erste und zweite, in der Nabe verbaute Kugellager.

[![](images/03-nabe/f4cd8c-www.nerdiy.de-hub-20200612-144723.jpg)](images/03-nabe/f4cd8c-www.nerdiy.de-hub-20200612-144723.jpg)

Zieht die Schubstange dann ein Stück zurück und verschraubt die erste selbst sichernde Mutter wie abgebildet auf der Schubstange.

Die Mutter ist leider nicht zu sehen aber befindet sich in dem Steckschlüssel, mit dessen Hilfe die Montage wesentlich leichter geht.

[![](images/03-nabe/55e0f5-www.nerdiy.de-hub-20200612-144706.jpg)](images/03-nabe/55e0f5-www.nerdiy.de-hub-20200612-144706.jpg)

Ebenfalls hilfreich ist es, wenn Ihr die Gewindestange wie abgebildet in einem Akkuschrauber einspannt. So könnt Ihr die Gewindestange leicht in die M6 Mutter drehen.

[![](images/03-nabe/aecda2-www.nerdiy.de-hub-20200612-144742.jpg)](images/03-nabe/aecda2-www.nerdiy.de-hub-20200612-144742.jpg)

Hat alles geklappt sollte die M6 Mutter wie abgebildet auf der Gewindestange sitzen.

[![](images/03-nabe/4ea24c-www.nerdiy.de-hub-20200612-144855.jpg)](images/03-nabe/4ea24c-www.nerdiy.de-hub-20200612-144855.jpg)

Nun könnt Ihr die Gewindestange wieder in das obere Kugellager einstecken.

[![](images/03-nabe/ad1778-www.nerdiy.de-hub-20200612-144900.jpg)](images/03-nabe/ad1778-www.nerdiy.de-hub-20200612-144900.jpg)

Nahansicht der eingesteckten Gewindestange im oberen Kugellager.

[![](images/03-nabe/7dff1c-www.nerdiy.de-hub-20200612-145127.jpg)](images/03-nabe/7dff1c-www.nerdiy.de-hub-20200612-145127.jpg)

Damit die Schubstange nun auch im oberen Kugellager bleibt, müsst Ihr nun noch die andere M6 Mutter wie abgebildet auf die Schubstange aufschrauben.

Die Schubstange sollte nun ohne großes Spiel fest im Kugellager sitzen.

[![](images/03-nabe/b560bc-www.nerdiy.de-hub-20200612-145125.jpg)](images/03-nabe/b560bc-www.nerdiy.de-hub-20200612-145125.jpg)

Weitere Ansicht.

[![](images/03-nabe/6ba696-www.nerdiy.de-hub-20200612-145137.jpg)](images/03-nabe/6ba696-www.nerdiy.de-hub-20200612-145137.jpg)

Weitere Ansicht.

[![](images/03-nabe/4430b3-www.nerdiy.de-hub-20200612-145156.jpg)](images/03-nabe/4430b3-www.nerdiy.de-hub-20200612-145156.jpg)

Weitere Ansicht.

Spätestens jetzt ist es zeit für einen ersten Test.

[![YouTube-Video qgT8Yi2m5rM (Vorschau – klicken zum Abspielen)](images/03-nabe/068e3b-maxresdefault.jpg)](https://www.youtube.com/watch?v=qgT8Yi2m5rM)

Dieses Video zeigt wie die Mechanik nun funktionieren sollte. (Lasst Euch von den veränderten design nicht abschrecken. Das ist ein Video das ich während der Entwicklung der Mechanik aufgenommen habe.)

---

## Abdeckung befestigen

Zu guter Letzt bekommt die Nabe nun eine Abdeckung. Diese deckt zum einen die Mechanik ab und sollte sie vor Feuchtigkeit und Regen schützen. Zum anderen macht sie die Nabe etwas aerodynamischer.

[![](images/03-nabe/a46c1e-www.nerdiy.de-hub-20200612-145411.jpg)](images/03-nabe/a46c1e-www.nerdiy.de-hub-20200612-145411.jpg)

Hierzu benötigt Ihr die 3D gedruckte Abdeckung, drei M3 Muttern und drei M3x16 Senkkopfschrauben.

[![](images/03-nabe/9e4229-www.nerdiy.de-hub-20200612-145415.jpg)](images/03-nabe/9e4229-www.nerdiy.de-hub-20200612-145415.jpg)

Nahansicht der benötigten Teile.

[![](images/03-nabe/d3ab66-www.nerdiy.de-hub-20200612-145523.jpg)](images/03-nabe/d3ab66-www.nerdiy.de-hub-20200612-145523.jpg)

Steckt nun wieder die M3 Mutter in die vorgesehene Aussparung im Rahmen der Naben-Basis…

[![](images/03-nabe/626022-www.nerdiy.de-hub-20200612-145533.jpg)](images/03-nabe/626022-www.nerdiy.de-hub-20200612-145533.jpg)

… und Befestigt die M3x16 Senkkopfschraube darin.

[![](images/03-nabe/4b0b4f-www.nerdiy.de-hub-20200612-145810.jpg)](images/03-nabe/4b0b4f-www.nerdiy.de-hub-20200612-145810.jpg)

Nun sichert Ihr die M3 Mutter wieder mit etwas Heißkleber im Rahmen der Naben-Basis…

[![](images/03-nabe/106ede-www.nerdiy.de-hub-20200612-145842.jpg)](images/03-nabe/106ede-www.nerdiy.de-hub-20200612-145842.jpg)

… und entfernt die Schraube wieder.

[![](images/03-nabe/6dd979-www.nerdiy.de-hub-20200612-145902.jpg)](images/03-nabe/6dd979-www.nerdiy.de-hub-20200612-145902.jpg)

Nun könnt Ihr die Abdeckung aufsetzen und mithilfe der vorbereiteten Schrauben…

[![](images/03-nabe/83035d-www.nerdiy.de-hub-20200612-150013.jpg)](images/03-nabe/83035d-www.nerdiy.de-hub-20200612-150013.jpg)

…im Rahmen der Naben-Basis verschrauben.

[![](images/03-nabe/9b4718-www.nerdiy.de-hub-20200612-150017.jpg)](images/03-nabe/9b4718-www.nerdiy.de-hub-20200612-150017.jpg)

Ansicht der aufgesetzten und verschraubten Abdeckung.

[![](images/03-nabe/0f5696-www.nerdiy.de-hub-20200612-150026.jpg)](images/03-nabe/0f5696-www.nerdiy.de-hub-20200612-150026.jpg)

Ansicht der aufgesetzten und verschraubten Abdeckung.

[![](images/03-nabe/a67f9e-www.nerdiy.de-hub-20200612-150033.jpg)](images/03-nabe/a67f9e-www.nerdiy.de-hub-20200612-150033.jpg)

Ansicht der aufgesetzten und verschraubten Abdeckung.

---

## Viel Spaß mit dem Projekt

Ich hoffe bei euch hat alles wie beschrieben funktioniert. Falls nicht oder ihr Fragen oder Anregungen habt lasst es mich in den Kommentaren bitte wissen. Ich trage dies dann ggf. in den Artikel nach.  
Auch Ideen für neue Projekte sind immer gerne willkommen. 🙂

**P.S. Viele dieser Projekte - besonders die Hardwareprojekte - kosten viel Zeit und Geld. Natürlich mache ich das weil ich Spaß daran habe, aber wenn Du es cool findest, dass ich die Infos dazu mit Euch teile, würde ich mich über eine kleine Spende an die Kaffeekasse freuen. 🙂**
