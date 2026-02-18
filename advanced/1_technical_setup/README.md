# Technisches Setup

Willkommen zur ersten **Python Advanced Session**! Bevor wir in die spannenden Themen wie OOP, Dekoratoren oder das Python Data Model eintauchen, müssen wir zunächst eine solide Grundlage schaffen: eine professionelle Entwicklungsumgebung auf deinem eigenen Rechner.

In dieser Session richten wir gemeinsam alles ein, was du brauchst, um die folgenden Sessions komfortabel und ohne technische Hürden mitverfolgen zu können. Das mag auf den ersten Blick nach viel Aufwand klingen – aber dieser einmalige Aufwand zahlt sich schnell aus, und die Tools die du hier kennenlernst sind dieselben, die auch in der echten Softwareentwicklung täglich eingesetzt werden.

---

## Überblick: Was richten wir ein?

- **Visual Studio Code (VSCode)** – unsere Entwicklungsumgebung (IDE)
- **uv** – ein moderner Python Package Manager
- **Git** – zur Versionskontrolle und um das Repository zu klonen
- **Das Repository klonen** – den Session-Code auf deinen Rechner holen
- **Virtuelle Umgebung erstellen** – Python-Pakete projektbezogen verwalten
- **VSCode Extensions** – hilfreiche Erweiterungen für Python und Jupyter
- **Code ausführen** – Python-Skripte und Jupyter Notebooks starten

---

## 1. Visual Studio Code installieren

Visual Studio Code (kurz: VSCode) ist eine kostenlose, quelloffene IDE von Microsoft und einer der meistgenutzten Code-Editoren weltweit. Sie ist leichtgewichtig, hochgradig erweiterbar und hat eine hervorragende Python-Unterstützung.

**Download und Installation:**

1. Gehe auf [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Lade die Version für dein Betriebssystem herunter (Windows, macOS oder Linux)
3. Führe den Installer aus und folge den Anweisungen

> 💡 **Tipp für Windows-Nutzer:** Aktiviere während der Installation die Option *"Add to PATH"* und *"Open with Code"* im Kontextmenü – das spart dir später einige Klicks.

Nach der Installation kannst du VSCode starten und wirst von einem Willkommens-Tab begrüßt. Lass dich davon nicht erschlagen – wir richten gleich alles Schritt für Schritt ein.

---

## 2. uv installieren

`uv` ist ein moderner, blitzschneller Python Package Manager, der von [Astral](https://astral.sh/) entwickelt wird. Er ersetzt in vielen Bereichen das klassische Duo `pip` + `venv` und erledigt beides – Paketverwaltung und virtuelle Umgebungen – in einem einzigen Tool.

Der große Vorteil von `uv` gegenüber traditionellen Ansätzen: Es ist deutlich schneller, löst Abhängigkeitskonflikte zuverlässiger, und sorgt dafür dass dein Projekt auf jedem Rechner identisch funktioniert. Das ist besonders praktisch, wenn du Code mit anderen teilst – oder Sessions nacharbeitest.

**Installation:**

Öffne ein Terminal (unter Windows: PowerShell oder das neue Windows Terminal) und führe den passenden Befehl aus:

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Du kannst `uv` auch über den Windows Package Manager `winget` installieren:
```powershell
winget install --id=astral-sh.uv  -e
```


Nach der Installation kannst du überprüfen, ob alles geklappt hat:
```bash
uv --version
```

Du solltest eine Versionsnummer sehen, z.B. `uv 0.5.x`. Falls der Befehl nicht gefunden wird, starte dein Terminal neu – die PATH-Variable muss neu eingelesen werden.

Sollte es weiterhin Probleme geben, findest du auf der offiziellen Installationsseite von `uv` weitere Troubleshooting-Tipps und alternative Installationsmethoden: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/).

> 💡 **Was ist ein Terminal?** Das Terminal (auch Kommandozeile oder Shell genannt) ist ein Texteingabe-Interface, über das du direkt mit deinem Betriebssystem kommunizierst. In VSCode gibt es ein integriertes Terminal, das du mit `Strg+ö` (Windows/Linux) oder `` Ctrl+` `` (macOS) öffnen kannst – das wirst du gleich noch brauchen.

---

## 3. Git installieren und das Repository klonen

### Was ist Git?

Git ist ein **Versionskontrollsystem** – ein Tool, das Änderungen an Dateien über die Zeit verfolgt. Stell es dir vor wie eine Art "Speicherpunkte" in einem Videospiel: Du kannst jederzeit auf einen früheren Stand zurückspringen, Änderungen vergleichen oder parallel an verschiedenen Features arbeiten.

GitHub ist eine Plattform, auf der Git-Repositories (Projekte) gehostet werden. Unser Session-Repository liegt dort und du kannst es von dort auf deinen Rechner **klonen** – also eine vollständige lokale Kopie erstellen.

### Git installieren

**Windows:** Lade den Installer von [https://git-scm.com/download/win](https://git-scm.com/download/win) herunter und führe ihn aus. Die Standardeinstellungen passen in den meisten Fällen.

Alternativ kannst du Git auch über den Windows Package Manager `winget` installieren:
```powershell
winget install --id=Git.Git -e
```

**macOS:** Git ist auf macOS oft schon vorinstalliert. Prüfe es mit `git --version` im Terminal. Falls nicht, wird dir macOS automatisch anbieten, die Developer Tools zu installieren.

**Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

Prüfe die Installation mit:
```bash
git --version
```

### Repository in VSCode klonen

Das Klonen des Repositories geht direkt aus VSCode heraus – ganz ohne Kommandozeile. So funktioniert es:

1. Öffne VSCode
2. Klicke in der linken Seitenleiste auf das **Source Control**-Icon (das Symbol sieht aus wie eine Gabelung)
3. Klicke auf **"Clone Repository"**
4. Gib die folgende URL ein und bestätige mit Enter:
   ```
   https://github.com/stackfuel/Python_Live_Sessions.git
   ```
5. Wähle einen Ordner auf deinem Rechner, in dem das Repository gespeichert werden soll (z.B. `Dokumente/StackFuel`)
6. VSCode fragt dich, ob du das geklonte Repository direkt öffnen möchtest – bestätige das mit **"Open"**

Alternativ kannst du das Repository auch über das integrierte Terminal klonen:
```bash
git clone https://github.com/stackfuel/Python_Live_Sessions.git
cd Python_Live_Sessions
code .
```

Der letzte Befehl (`code .`) öffnet den aktuellen Ordner direkt in VSCode.

### Repository aktuell halten

Da wir das Repository während der Sessions regelmäßig aktualisieren, solltest du vor jeder Session den neuesten Stand herunterladen. Das geht ganz einfach über den Source-Control-Tab in VSCode: Klicke dort auf die drei Punkte (`...`) und wähle **"Pull"** – oder nutze das Terminal:
```bash
git pull
```

---

## 4. Virtuelle Umgebung erstellen mit `uv sync`

Jetzt kommt `uv` zum Einsatz. Das Repository enthält bereits eine `pyproject.toml`-Datei, in der alle benötigten Pakete (wie `numpy`, `matplotlib`, `jupyter` etc.) aufgelistet sind. Mit einem einzigen Befehl erstellt `uv` eine isolierte virtuelle Umgebung und installiert alle Abhängigkeiten automatisch.

**Was ist eine virtuelle Umgebung?** Stell dir vor, du arbeitest an mehreren Python-Projekten, die unterschiedliche Versionen desselben Pakets benötigen. Eine virtuelle Umgebung ist ein abgeschlossener Python-Bereich, der nur die Pakete enthält, die für dieses eine Projekt benötigt werden – so können sich Projekte nicht gegenseitig in die Quere kommen.

Öffne das Terminal in VSCode (`Strg+ö` / `` Ctrl+` ``) und stelle sicher, dass du im Projektordner bist (der Ordnerpfad sollte mit `Python_Live_Sessions` enden). Führe dann aus:

```bash
uv sync
```

`uv` liest die `pyproject.toml`, erstellt einen `.venv`-Ordner im Projektverzeichnis und installiert alle Pakete. Das geht dank `uv` deutlich schneller als mit `pip` – in der Regel in wenigen Sekunden.

> 💡 Du musst `uv sync` in der Regel nur einmal ausführen. Wenn sich die Abhängigkeiten des Projekts ändern (z.B. weil wir ein neues Paket hinzufügen), reicht ein erneutes `uv sync`, um alles auf den neuesten Stand zu bringen.

---

## 5. VSCode Extensions installieren

Einer der großen Stärken von VSCode ist seine Erweiterbarkeit. Für unsere Sessions empfehlen wir die Installation von zwei Extensions, die die Arbeit mit Python und Jupyter Notebooks erheblich angenehmer machen.

Du findest den Extension Marketplace über das Würfel-Icon in der linken Seitenleiste (oder mit `Strg+Shift+X`). Suche dort jeweils nach dem Namen der Extension und klicke auf **"Install"**.

**Empfohlene Extensions:**

- **Python** (von Microsoft) – Die offizielle Python-Extension. Sie aktiviert Syntax-Highlighting, Autovervollständigung, Linting und ermöglicht das Ausführen von Python-Skripten direkt aus VSCode.

- **Jupyter** (von Microsoft) – Diese Extension ermöglicht das Öffnen, Bearbeiten und Ausführen von `.ipynb`-Notebooks direkt in VSCode, ohne dass du einen separaten Browser-Tab öffnen musst.

Nach der Installation empfiehlt es sich, VSCode einmal neu zu starten.

### Python Interpreter auswählen

Damit VSCode weiß, welches Python es verwenden soll, müssen wir es auf unsere virtuelle Umgebung hinweisen:

1. Öffne die Command Palette mit `Strg+Shift+P` (macOS: `Cmd+Shift+P`)
2. Tippe **"Python: Select Interpreter"** und wähle den Eintrag aus
3. Wähle den Interpreter aus dem `.venv`-Ordner des Projekts – er sollte in der Liste erscheinen und mit `('.venv': venv)` oder ähnlichem gekennzeichnet sein

Falls er nicht auftaucht, kannst du auch manuell den Pfad eingeben:
- **Windows:** `.venv\Scripts\python.exe`
- **macOS/Linux:** `.venv/bin/python`

Nachdem du den Interpreter gesetzt hast, siehst du ihn in der Statusleiste unten links in VSCode. Ab sofort nutzen alle Python-Features von VSCode – Autovervollständigung, Ausführung, Linting – die Pakete aus unserer virtuellen Umgebung.

---

## 6. Code ausführen

Jetzt ist alles eingerichtet! Hier ein kurzer Überblick, wie du die verschiedenen Dateitypen in unseren Sessions ausführst.

### Python-Skripte (`.py`)

Öffne eine `.py`-Datei in VSCode. Du hast zwei Möglichkeiten:

- **Play-Button:** Klicke oben rechts auf das Dreieck-Symbol ▷ ("Run Python File")
- **Terminal:** Öffne das Terminal und führe die Datei direkt aus:
  ```bash
  uv run python pfad/zur/datei.py
  ```

  Der `uv run`-Prefix stellt sicher, dass das Python aus der virtuellen Umgebung verwendet wird.

### Jupyter Notebooks (`.ipynb`)

Öffne eine `.ipynb`-Datei. VSCode zeigt sie direkt als interaktives Notebook an. Du kannst:

- **Einzelne Zellen ausführen:** Klicke auf das ▷-Symbol links neben einer Zelle oder drücke `Shift+Enter`
- **Alle Zellen ausführen:** Klicke oben auf **"Run All"**
- **Kernel auswählen:** Beim ersten Öffnen wirst du gefragt, welchen Kernel (= Python-Interpreter) du verwenden möchtest. Wähle hier den Interpreter aus unserer `.venv`-Umgebung – denselben, den wir im vorherigen Schritt ausgewählt haben.

> 💡 **Tipp:** Mit `Shift+Enter` führst du die aktuelle Zelle aus und springst automatisch zur nächsten. Das ist der schnellste Weg, um ein Notebook von oben nach unten durchzuarbeiten.

---

## Zusammenfassung

Du hast jetzt eine vollständige, professionelle Python-Entwicklungsumgebung auf deinem Rechner. Hier nochmal alle Schritte im Überblick:

| Schritt | Was wurde gemacht |
|---|---|
| ✅ VSCode installiert | IDE für die Entwicklung |
| ✅ uv installiert | Moderner Package Manager |
| ✅ Git installiert | Versionskontrolle |
| ✅ Repository geklont | Session-Materialien lokal verfügbar |
| ✅ `uv sync` ausgeführt | Virtuelle Umgebung mit allen Paketen erstellt |
| ✅ Extensions installiert | Python + Jupyter Support in VSCode |
| ✅ Interpreter ausgewählt | VSCode nutzt die richtige Umgebung |

Ab jetzt konzentrieren wir uns in den Sessions vollständig auf Python – das Setup läuft im Hintergrund, ohne dass du dir weitere Gedanken darüber machen musst.

---

## Häufige Probleme und Lösungen

**`uv` wird nach der Installation nicht gefunden:**
Starte dein Terminal (oder VSCode) neu. Die PATH-Variable muss neu eingelesen werden.

**`uv sync` schlägt fehl:**
Stelle sicher, dass du dich im richtigen Verzeichnis befindest – dort, wo die `pyproject.toml`-Datei liegt. Prüfe mit `ls` (macOS/Linux) oder `dir` (Windows), ob die Datei vorhanden ist.

**Der `.venv`-Interpreter taucht in VSCode nicht auf:**
Öffne die Command Palette (`Strg+Shift+P`), wähle "Python: Select Interpreter" und klicke auf "Enter interpreter path..." – dann navigiere manuell zur `python.exe` (Windows) bzw. `python` (macOS/Linux) im `.venv`-Ordner.

**Notebook-Kernel ist falsch oder startet nicht:**
Klicke oben rechts im Notebook auf den aktuellen Kernel-Namen und wähle "Select Another Kernel" → "Python Environments" → `.venv`.

Bei weiteren Fragen melde dich gerne in der Live Session oder schreib uns im zugehörigen Kanal – wir helfen dir weiter!