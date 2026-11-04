---
title: "Nerdiskerator – Generator aus dem 3D Drucker"
source: https://nerdiy.de/nerdiskerator-a-generator-from-the-3d-printer/
retrieved: 2026-11-04
---

# Nerdiskerator – Generator aus dem 3D Drucker

Vor ein paar Tagen habe ich die Bauanleitung zu einem Projekt von mir gepostet: ***[WinDIY eine 3D gedruckte Windturbine](https://nerdiy.de/windiy-die-wind-turbine-aus-dem-3d-drucker/)***.

Auch wenn ich noch etwas Arbeit vor mir habe funktionieren die meisten Funktionen von WinDIY bereits. Was leider noch nicht funktioniert hat ist der Hauptzweck einer Windturbine: Das Erzeugen von Energie.

Denn der Generator den ich in WinDIY verbaut habe passt nicht zu den zu erwarteten Drehzahlen der Windturbine. Während der Generator ab ca. 20 Umdrehungen pro Sekunde(!) ca. 30W liefert würde die Windturbine bei dieser Umdrehungszahl wahrscheinlich zerstört.

Hier muss ich wohl nochmal ein paar Stunden an der Werkbank investieren. 🙂

Da der Generator im Prinzip aber funktioniert und es vllt. auch Szenarien gibt zu denen er doch passen könnte will ich Ihn hier trotzdem Vorstellen. Mindestens Tipps für die Entwicklung eines eigenen Generators sollten sich daraus rausziehen lassen. 🙂

Und warum eigentlich „Nerdiskerator“? Dieser Spitzname des Scheibengenerators (=disk generator) kommt von „NERdiys DISK genERATOR“= Nerdiskerator. 🙂

---

## Überblick

- Scheibengenerator, der zum Großteil aus 3D druckbaren Teilen besteht
- Der Stator enthält 12 manuell oder automatisch gewickelte Spulen
- Die Spulen sind mit Epoxidharz im Stator vergossen
- Zwei Rotorscheiben mit jeweils 20 Neodym-Magneten
- Jede Rotorscheibe ist mit einem Kugellager gelagert
- Im Stator werden außerdem drei NTCs vergossen um die Temperatur in den Statorwicklungen zu überwachen

---

## Bilder

Im folgenden ein paar Bilder verschiedener Komponenten aus verschiedenen Entwicklungsstadien.

- ![](images/08-nerdiskerator-generator/a1ca79-www.nerdiy.de-20200923-102555.jpg)
- ![](images/08-nerdiskerator-generator/f2e80d-www.nerdiy.de-20200923-105720.jpg)
- ![](images/08-nerdiskerator-generator/93129a-www.nerdiy.de-20200923-105700.jpg)
- ![](images/08-nerdiskerator-generator/303371-www.nerdiy.de-20200923-103945.jpg)
- ![](images/08-nerdiskerator-generator/60359e-www.nerdiy.de-20200923-101816.jpg)
- ![](images/08-nerdiskerator-generator/1a79c8-www.nerdiy.de-20200923-110444.jpg)
- ![](images/08-nerdiskerator-generator/599f6c-www.nerdiy.de-20200923-110433.jpg)
- ![](images/08-nerdiskerator-generator/7766d6-www.nerdiy.de-20200829-111341.jpg)
- ![](images/08-nerdiskerator-generator/ad846c-www.nerdiy.de-20200829-110609.jpg)
- ![](images/08-nerdiskerator-generator/b4f08e-www.nerdiy.de-20200829-110315.jpg)
- ![](images/08-nerdiskerator-generator/be6c1b-www.nerdiy.de-20200829-110028.jpg)
- ![](images/08-nerdiskerator-generator/4b131d-www.nerdiy.de-20200912-162551-scaled.jpg)
- ![](images/08-nerdiskerator-generator/69ba4f-www.nerdiy.de-20200829-105638.jpg)
- ![](images/08-nerdiskerator-generator/d194eb-www.nerdiy.de-20200829-112400.jpg)
- ![](images/08-nerdiskerator-generator/bdb1b8-www.nerdiy.de-20200829-111546.jpg)
- ![](images/08-nerdiskerator-generator/1d265b-www.nerdiy.de-20200829-111430.jpg)
- ![](images/08-nerdiskerator-generator/6757ae-www.nerdiy.de-20200912-162549-scaled.jpg)
- ![](images/08-nerdiskerator-generator/6e83a3-www.nerdiy.de-20200912-162530-scaled.jpg)
- ![](images/08-nerdiskerator-generator/8d3ec1-www.nerdiy.de-20200912-161154.jpg)
- ![](images/08-nerdiskerator-generator/14be61-www.nerdiy.de-20200912-155949-scaled.jpg)
- ![](images/08-nerdiskerator-generator/7a663b-www.nerdiy.de-32-scaled.jpg)
- ![](images/08-nerdiskerator-generator/2036ef-www.nerdiy.de-31-scaled.jpg)
- ![](images/08-nerdiskerator-generator/e05a03-www.nerdiy.de-20200620-145750-scaled.jpg)
- ![](images/08-nerdiskerator-generator/1a47bd-www.nerdiy.de-20200620-145734-scaled.jpg)
- ![](images/08-nerdiskerator-generator/6e4e04-www.nerdiy.de-20200620-145711-scaled.jpg)
- ![](images/08-nerdiskerator-generator/9870d1-www.nerdiy.de-20200620-145548-scaled.jpg)
- ![](images/08-nerdiskerator-generator/dec5a9-www.nerdiy.de-20200620-145535-scaled.jpg)
- ![](images/08-nerdiskerator-generator/9e012d-www.nerdiy.de-20200620-145531-scaled.jpg)
- ![](images/08-nerdiskerator-generator/83b818-www.nerdiy.de-20200620-145336-scaled.jpg)
- ![](images/08-nerdiskerator-generator/2077e5-www.nerdiy.de-20200620-145334-scaled.jpg)
- ![](images/08-nerdiskerator-generator/dff778-www.nerdiy.de-37-scaled.jpg)
- ![](images/08-nerdiskerator-generator/0fbe58-www.nerdiy.de-36-scaled.jpg)
- ![](images/08-nerdiskerator-generator/21aa4f-www.nerdiy.de-34-scaled.jpg)
- ![](images/08-nerdiskerator-generator/b72674-www.nerdiy.de-33-scaled.jpg)

---

## Entwicklung

Die Entwicklung und die einzelnen Schwierigkeiten habe ich zum Großteil auf Hackaday.io dokumentiert. Den Link dazu findet Ihr hier. 🙂

***<https://hackaday.io/project/172445-nerdiskerator-a-3d-printed-disk-generator>***

---

## Elektronik

Neben WinDIY verfügt auch der Nerdiskerator über ein paar Sicherheitsfeatures.

In diesem sind nämlich drei NTC’s vergossen um die Spulentemperatur im Stator zu überwachen. Diese sollte natürlich nicht zu hoch werden, da das verwendete Filament dann weich werden kann.

Damit diese Sensoren ausgelesen und ggf. darauf reagiert werden kann ist natürlich etwas Elektronik notwendig. Dazu habe ich mit der Entwicklung einer Platine begonnen, auf der alle notwendigen Komponenten untergebracht sind.

Infos dazu findet Ihr auch bald hier auf Nerdiy.de.

**Darauf verbaut sind bisher folgende Komponenten:**

- Drei-Wege Brückengleichrichter
- Step-Down-Regler
- Drei voneinander unabhängige Ladeschaltungen für jeweils eine LiPo Zelle
- Drei I2C Motortreiber um die Motoren des Bremsaktors sowie des Pitch Aktors ansteuern zu können
- diverse Strom- und Spannungssensoren um die erzeugte und verbrauchte Energie messen zu können
- Anschlüsse für zwei Hall-Sensoren zur Messung der Generator-Drehzahl
- Anschlüsse für drei Schiebewiderstände um die Positionen des Pitch-Aktors und der Bremszylinder messen zu können
- Anschlüsse für zwei Kraftsensoren um den Anpressdruck der Bremszylinder messen zu können
- Anschlüsse für vier NTCs um die Temperaturen der Generatorwicklungen sowie des Lastwiderstands messen zu können.
- Anschluss um die Gleichgerichtete Spannung an einen Verbraucher abführen zu können
- Anschluss und Elektronik um einen Lastwiderstand PWM-gesteuert zuschalten zu können.
- Vibrationssensor um abnormale Vibrationen zu erkennen
- zwei Temperatursensoren um die Temperaturen auf dem PCB überwachen zu können
- ein elektronischer Kompass
- ein micro-SD kartensteckplatz
- ein Klimasensor zur Messung der Umgebungstemperatur, Luftfeuchtigkeit und Luftdruck

---

## Software

Die Software wird mithilfe der Arduino IDE entwickelt. Den aktuellen Stand findet Ihr im Nerdiy-Git unter folgendem Link:

[***https://github.com/Nerdiyde/genCtrlr***](https://github.com/Nerdiyde/genCtrlr)
