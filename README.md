# 🐍 PCEP Gehirn-Trainer Ultimate (200 Fragen Edition)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PCEP](https://img.shields.io/badge/OpenEDG-PCEP--30--02%20%7C%2030--03-ffd23f?style=for-the-badge)
![Status](https://img.shields.io/badge/Fragenpool-200%20Fragen%20%26%2079%20Fallen-3ddc84?style=for-the-badge)
![License](https://img.shields.io/badge/Lizenz-MIT-blue?style=for-the-badge)

Ein interaktiver Prüfungs- und Fangfragen-Trainer für die offizielle **Certified Entry-Level Python Programmer (`PCEP-30-02` & `PCEP-30-03`)** Zertifizierung des Python Institute (OpenEDG).

Entwickelt als **Zero-Dependency Web-App (HTML5/JS)** sowie als **Python Desktop-App (`tkinter`)** – speziell konzipiert, um englische Original-Prüfungsfragen mit deutschen Erklärungen auf zwei Verständnisebenen (*„👶 Für 5-Jährige"* & *„🤓 Profi-Regel"*) systematisch zu meistern.

---

## ✨ Features & Lern-Modi

* 📚 **200 handverlesene PCEP-Fragen** nach offizieller Prüfungsgewichtung:
  * **🧮 Block 1 (18%):** Grundlagen, Zahlensysteme (`0b`, `0o`, `0x`), Operatoren-Rangfolge (`**`, `//`, `%`, Bitwise) & `print()` / `input()`
  * **🔁 Block 2 (29%):** Kontrollstrukturen (`if/elif/else`), Schleifen (`for`, `while`, `range`), `break` / `continue` & die `for...else`-Falle
  * **📦 Block 3 (25%):** Datenstrukturen (`list`, `tuple`, `dict`, `str`), Slicing, Aliasing (`b = a` vs. `a[:]`) & Methoden
  * **🧯 Block 4 (28%):** Funktionen, Scope (`global`, `UnboundLocalError`), Default-Parameter & die `BaseException`-Hierarchie
  * **📁 Block 5 (Zusatz für PCEP-30-03):** Dateioperationen (`with open`), `csv`, `math`, `random`, `set` & `f-Strings`
* 🪤 **79 markierte Fangfragen (Trap-Mode):** Gezieltes Training der typischen OpenEDG-Stolpersteine.
* 🇩🇪 **1-Klick Deutsch-Übersetzer:** Jede Frage ist wie in der echten Prüfung auf Englisch formuliert, lässt sich aber jederzeit per Knopfdruck (oder Dauer-Schalter) auf Deutsch übersetzen.
* 📦 **Automatische Fehler-Kiste (Spaced Repetition):** Falsch beantwortete Fragen landen automatisch in der Fehler-Kiste und verschwinden erst, wenn sie dort korrekt gelöst wurden.
* 🎓 **Realistische Prüfungssimulation:**
  * **PCEP-30-02:** 30 Fragen · 40 Minuten Timer · 70 % Bestehensgrenze
  * **PCEP-30-03:** 35 Fragen · 50 Minuten Timer · 70 % Bestehensgrenze
  * Inklusive Fragen-Navigator, Markierungsfunktion (`🚩`) und anschließender Stärken-/Schwächen-Analyse pro Themenblock.
* 📜 **Integrierter Spickzettel & 🇬🇧 Englisch-Überlebens-Wörterbuch:** Alle 25 Kernregeln, Operator-Prioritäten, der Exception-Stammbaum und die wichtigsten englischen Prüfungsbegriffe auf einen Blick.

---

## 🚀 Schnellstart

### Option 1: Direkt im Browser (Web-App – ohne Installation)
1. Öffne einfach die Datei **`index.html`** (oder **`PCEP_Gehirn_Trainer_Ultimate.html`**) per Doppelklick in einem beliebigen Browser (Chrome, Edge, Firefox, Safari).
2. Läuft **100 % offline** auf PC, Mac, Tablet und Smartphone – der Lernfortschritt wird automatisch im `localStorage` des Browsers gespeichert.

### Option 2: Als Python Desktop-App (`tkinter`)
```bash
python pcep_quiz_app.py
```
*(Nutzt ausschließlich die Python-Standardbibliothek – kein `pip install` erforderlich! Der Fortschritt wird lokal in `pcep_fortschritt.json` gespeichert.)*

---

## ⌨️ Tastatur-Steuerung (Web & Desktop)

| Taste | Aktion |
| :--- | :--- |
| **`1` – `4`** oder **`A` – `D`** | Antwortmöglichkeit A, B, C oder D auswählen |
| **`Enter`** | Nächste Frage aufrufen |
| **`Ü`** oder **`T`** | 🇩🇪 Deutsche Übersetzung der Frage ein-/ausblenden |
| **`←`** / **`→`** | Zwischen Fragen in der Prüfungssimulation blättern |

---

## 👨‍💻 Autor

Erstellt von **Vuk (`@Vuki73`)** im Rahmen des Software & AI Engineering Trainings.
