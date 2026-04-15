# Python Live Sessions

## Einleitung

Willkommen zu den **Python Live Sessions** von StackFuel! Diese Sessions sind als **begleitendes, freiwilliges Angebot** für alle Teilnehmenden der StackFuel-Kurse konzipiert. Da die meisten Trainings auf Python aufbauen, vermitteln wir hier systematisch die grundlegenden Konzepte der Programmiersprache.

Die Sessions sind in zwei parallele Bereiche unterteilt:
- **Python Basics**: Grundlagen für Data Analytics (DAN) und Data Science (DSC) Teilnehmende
- **Python Advanced**: Vertiefende Konzepte für Weiterführende Programmierung (WPP), Objektorientierte Programmierung (OOP) und Data Science Portfolio Projekt (DPP) Teilnehmer

Jede Live Session dauert **ca. 1 Stunde** und behandelt ein konkretes Thema. Die Basics-Sessions verwenden *Jupyter Notebooks*, während die Advanced-Sessions auch mit *Python-Skripten und Modulen* arbeiten, um ein realistisches Bild der Softwareentwicklung zu vermitteln.

**Wichtiger Hinweis:** Die Konzepte bauen stark aufeinander auf - ein regelmäßiger Besuch der Sessions ist daher empfehlenswert.


## Empfohlene Entwicklungsumgebung

Die Notebooks und Python Scripte können im DataLab hochgeladen werden um die Inhalte nachzuarbeiten. Allerdings kann es dazu kommen, dass aufgrund von Versionskonflikten einige Funktionen nicht im DataLab verfügbar sind. Aus diesem Grund empfehlen wir eine eigene Entwicklungsumgebung mit aktuellen Paketen einzurichten.

Für die optimale Teilnahme an den Sessions empfehlen wir:

- **IDE**: [Visual Studio Code](https://code.visualstudio.com/) mit Python-Extension - Professionelle Entwicklungsumgebung mit ausgezeichneter Python-Unterstützung
- **Package Manager**: [uv](https://docs.astral.sh/uv/) - Moderner, schneller Python Package Manager für Dependency Management und virtuelle Umgebungen

*Zu diesen Tools gibt es in der ersten Python Advanced Session eine Einführung.*


## Sessionübersicht

### Python Basics Sessions

- [1. Einfache Datentypen](#1-einfache-datentypen)
- [2. Einfache Datenstrukturen](#2-einfache-datenstrukturen)
- [3. Kontrollstrukturen](#3-kontrollstrukturen)
- [4. Funktionen](#4-funktionen)
- [5. Iteratoren, Generatoren und Lazy Evaluation](#5-iteratoren-generatoren-und-lazy-evaluation)
- [6. Algorithmen](#6-algorithmen)
- [7. Code-Qualität und Refactoring](#7-code-qualität-und-refactoring)
- [8. Erweiterte Python Syntax (Syntactic Sugar)](#8-erweiterte-python-syntax-syntactic-sugar)
 
### Python Advanced Sessions
- [1. Technisches Setup](#1-technisches-setup)
- [2. Objektorientierte Programmierung - Grundlagen](#2-objektorientierte-programmierung---grundlagen)
- [3. Higher Order Functions und Dekoratoren](#3-higher-order-functions-und-dekoratoren)
- [4. Python Data Model](#4-python-data-model)
- [5. Vererbung und Komposition](#5-vererbung-und-komposition)
- [6. Erweiterte OOP-Konzepte](#6-erweiterte-oop-konzepte)
<!--- Error Handling Exeptions und Assert -->
<!--- Unit Testing -->



## Python Basics Sessions

Die Basics Sessions vermitteln die fundamentalen Sprachkonstrukte von Python, die für die Datenanalyse unerlässlich sind. Sie richten sich primär an Teilnehmende der **Data Analytics (DAN)** und **Data Science (DSC)** Kurse.

### 1. Einfache Datentypen

Diese Session führt in die grundlegenden Datentypen von Python ein, die das Fundament für alle weiteren Programmierkonzepte bilden.

- **Expressions**: Ausdrücke und deren Auswertung
- **Variablen**: Speicherung und Benennung von Werten
- **`bool`**: Wahrheitswerte für logische Aussagen
- **`int`**: Ganzzahlen ohne Dezimalstellen
- **`float`**: Gleitkommazahlen für mathematische Berechnungen
- **`str`**: Zeichenketten für Textdaten
- **`None`**: Spezieller Typ für nicht vorhandene Werte


### 2. Einfache Datenstrukturen

Hier lernst du die wichtigsten Datenstrukturen kennen, um mehrere Werte effizient zu organisieren und zu verwalten.

- **`tuple`**: Unveränderliche, geordnete Sammlung von Elementen
- **`list`**: Änderbare, geordnete Sammlung von Elementen
- **`set`**: Ungeordnete Sammlung von eindeutigen Elementen
- **`dict`**: Sammlung von Schlüssel-Wert-Paaren
- **Eigenschaften von Datenstrukturen**:
  - *Iterable*: Durchlaufbare Objekte
  - *Mutable vs. Immutable*: Änderbare vs. unveränderliche Datentypen

### 3. Kontrollstrukturen

Kontrollstrukturen ermöglichen es, den Programmfluss zu steuern und komplexere Logik zu implementieren.

- **`if/else`**: Bedingte Ausführung von Codeblöcken
- **`pass`**: Platzhalter für leere Codeblöcke
- **`while`**: Wiederholung von Codeblöcken solange Bedingungen wahr sind
- **`for`**: Iteration über Elemente von Sequenzen
- **`break/continue`**: Unterbrechung und Fortsetzung von Schleifen

### 4. Funktionen

Funktionen sind essentiell für die Strukturierung und Wiederverwendung von Code. Diese Session vermittelt die Grundlagen der Funktionsdefinition und -verwendung.

- **`def`**: Definition von Funktionen zur Wiederverwendung von Code
- **`return`**: Rückgabe eines Wertes aus einer Funktion
- **Funktionsaufrufe**: Ausführung definierter Funktionen
- **Parameter/Argumente**: Übergabe von Werten an Funktionen
  - *Default-Werte*: Standardwerte für Parameter
  - *Positional Parameters*: Positionelle Parameterübergabe
  - *Named Parameter*: Bennante Parameterübergabe
- **Funktionen Höherer Ordnung**: eingebaute Funktionen in Python

### 5. Iteratoren, Generatoren und Lazy Evaluation

Hier lernst du effiziente Methoden zur Verarbeitung großer Datenmengen und speicherschonende Programmierung kennen.

- **Iteratoren**: Objekte für schrittweise Durchlaufung von Sequenzen
- **Generatoren**: Speicher-effiziente Ergebniserzeugung mit `yield`
- **Generator Comprehensions**: Kompakte Generator-Erstellung
- **Built-in Funktionen für Iteration**:
  - `range`, `map`, `filter`, `zip`
  - `enumerate`, `reversed`

### 6. Algorithmen

Diese Session führt in algorithmisches Denken ein und zeigt, wie komplexere Probleme systematisch gelöst werden können.

- **Algorithmische Problemlösung**: Strukturierte Herangehensweise an Programmieraufgaben
- **Praktische Implementierungen**: *Euklidischer Algorithmus*
- **Klassische Algorithmen**: Sortier- und Suchalgorithmen als Beispiele
- **Rekursion**: Funktionen, die sich selbst aufrufen

### 7. Refactoring und Code Qualität

*Ankündigung*: Lerne, wie du mithilfe von Refactoring und den PEP8-Konventionen deinen Python-Code klarer, konsistenter und wartbarer gestaltest – mit praktischen Beispielen rund um einen Sudoku-Löser. Diese Live-Session richtet sich an alle, die bereits Grundkenntnisse in Python haben und ihren Code auf das nächste Level bringen möchten.

- **PEP 8**: Der offizielle Style Guide für Python-Code
- **Namenskonventionen**: Best Practices für aussagekräftige Bezeichner
- **Dokumentation**: Schreiben verständlicher und nützlicher Code-Dokumentation
- **Code-Refactoring**: Verbesserung bestehenden Codes ohne Funktionsänderung
- **Praktisches Projekt**: *Sudoku-Implementierung* zur Anwendung aller gelernten Konzepte

### 8. Erweiterte Python Syntax (Syntactic Sugar)

Diese Session stellt elegante Python-Sprachkonstrukte vor, die Code kompakter und lesbarer machen.

- **Comprehensions**: Elegante Erzeugung von Datenstrukturen
- **Lambda-Funktionen**: Kurzdefinition anonymer Funktionen
- **Context Manager**: Ressourcenmanagement mit `with`-Statement
- **Tuple Unpacking**: Entpacken von Tupeln und der `*`-Operator
- **String Formatting**: `f-strings` und erweiterte Formatierungsmöglichkeiten
- **Moderne Python-Features**:
  - *Ternary Operator*: `x if condition else y`
  - *Walrus-Operator*: `:=` für Variablenzuweisung in Expressions
  - *Chaining von Operatoren*: `a < b < c` statt `a < b and b < c`
  - *Structural Pattern Matching*: `match`-`case` Statements
  - *Type Hints*: Typannotationen für bessere Code-Dokumentation






## Python Advanced Sessions

Die Advanced Sessions vertiefen das Python-Wissen und behandeln fortgeschrittene Konzepte der objektorientierten und funktionalen Programmierung. Sie richten sich an Teilnehmende der Kurse **Weiterführende Programmierung (WPP)**, **Objektorientierte Programmierung (OOP)** und **Portfolio Projekt (DPP)**. Es sind aber alle interessierten Teilnehmenden herzlich willkommen.

### 1. Technisches Setup

Diese Session bereitet Dich auf die professionelle arbeit mit Python vor, indem sie die Einrichtung einer modernen Entwicklungsumgebung und die Nutzung von virtuellen Umgebungen behandelt.

- **Visual Studio Code Setup**: Konfiguration der IDE für optimale Python-Entwicklung
- **Virtuelle Umgebungen mit uv**: Moderne Abhängigkeitsverwaltung und Projekt-Isolation

### 2. Objektorientierte Programmierung - Grundlagen

Diese Session führt in die Grundkonzepte der objektorientierten Programmierung ein. 

- **Klassen und Objekte**: Grundlegende OOP-Konzepte
  - *Klassendefinition* und *Instanziierung*
  - Das `self`-Argument verstehen
- **Attribute**: Eigenschaften von Objekten
- **Methoden**: Funktionen innerhalb von Klassen
- **Special Methods**: Implementierung von Operatoren
  - `__add__`, `__sub__`, `__mul__` etc. zum Überladen von Operatoren
  - `__str__`, `__repr__` für String-Repräsentation


### 3. Higher Order Functions und Dekoratoren

Diese Session behandelt fortgeschrittene Funktionskonzepte und die Decorator-Syntax von Python.

- **Variable Argumentlisten**: Flexible Funktionsparameter
  - `*args`: Variable Anzahl positionaler Argumente
  - `**kwargs`: Variable Anzahl benannter Argumente
- **First-Class Functions**: Funktionen als Callables mit `__call__`-Methode
- **Closures**: Verschachtelte Funktionen und Zustandsspeicherung
- **Dekoratoren**: Funktionserweiterung mit `@`-Syntax
  - Grundlagen der Decorator-Implementierung
  - `functools.wraps`: Metadaten-Erhaltung
- **Built-in Dekoratoren**:
  - `@cache`: Memoization für Funktionen
  - `@property`: Getter/Setter-Implementierung
  - `@classmethod`: Klassenmethoden
  - `@staticmethod`: Statische Methoden

### 4. Python Data Model

Diese Session erklärt, wie Sie eigene Klassen nahtlos in Python's Ökosystem integrieren können.


- **Iteration Protocol**: 
  - `__iter__` und `__next__` für eigene Iteratoren
- **Container Types**:
  - **Sequences**: `__getitem__`, `__setitem__`, `__delitem__`
  - **Mappings**: `__contains__` für Zugehörigkeitstests
- **Numerische Operationen**:
  - Arithmetische Operatoren: `__add__`, `__sub__`, `__mul__`, `__truediv__`
  - Vergleichsoperatoren: `__eq__`, `__lt__`, `__gt__` etc.

### 5. Vererbung und Komposition

Diese Session behandelt fortgeschrittene OOP-Konzepte für die Strukturierung komplexer Anwendungen.

- **Vererbung**: Wiederverwendung und Erweiterung von Klassen
  - `super()`: Zugriff auf Parent-Class-Methoden
  - **Mehrfachvererbung**: Komplexe Klassenhierarchien
  - **MRO** (Method Resolution Order): Methodenauflösung verstehen
- **Komposition**: Alternative zu Vererbung durch Objektzusammensetzung


### 6. Fehlerbehandlung mit Exceptions
Diese Session vermittelt die Grundlagen der Fehlerbehandlung in Python, um robuste und fehlertolerante Anwendungen zu entwickeln.
- **Exceptions**: Fehlerbehandlung mit `try/except`-Blöcken
- **Eigene Exceptions**: Definition benutzerdefinierter Fehlertypen
- **`assert`-Anweisungen**: Einfache Fehlerüberprüfung und Debugging-Hilfe

### 7. Unit Testing
Diese Session führt in die Praxis des Unit Testings ein, um die Qualität und Zuverlässigkeit von Python-Code sicherzustellen.
- **Unittest Framework**: Einführung in das `pytest`-Modul
- **Einfache Testfälle schreiben**: Strukturierung von Tests für Funktionen und Klassen
- **Fixture und parametrisierte Tests**: Wiederverwendbare Testdaten und Testvariationen

### 8. Erweiterte OOP-Konzepte

Diese abschließende Session stellt moderne Python-Features für elegante Klassendesigns vor.

- **Dataclasses**: Vereinfachte Datenklassen mit `@dataclass`
- **Enumerations**: Typisierte Konstanten mit `enum.Enum`
- **Named Tuples**: Strukturierte, unveränderliche Datentypen
- **Collections-Erweiterungen**:
  - `defaultdict`: Dictionaries mit Standardwerten
  - `Counter`: Automatische Häufigkeitszählung
- **Mixin-Pattern**: Wiederverwendbare Funktionalität durch Mehrfachvererbung
- **Metaclasses**: *"Classes that create classes"* - Fortgeschrittene Metaprogrammierung




## Literaturempfehlungen

### Für Python Basics Sessions

**"Python Crash Course" von Eric Matthes**
- Praktische Projekte und grundlegende Konzepte für Anfänger
- Ideal für Sessions 1-4 (Datentypen bis Funktionen)

**"Automate the Boring Stuff with Python" von Al Sweigart**
- Automatisierung alltäglicher Aufgaben, sehr praxisorientiert
- Kostenlos verfügbar unter [automatetheboringstuff.com](https://automatetheboringstuff.com/)
- Perfekt für Sessions 3-6 (Kontrollstrukturen bis Syntactic Sugar)

**"Python 3: Das umfassende Handbuch" von Ernesti & Kaiser**
- Deutschsprachiges Standardwerk für systematische Lerner
- Umfassende Abdeckung aller Basics Sessions (1-8)

### Für Python Advanced Sessions

**"Python Tricks: The Book" von Dan Bader**
- Python-Idiome und Best Practices für Fortgeschrittene
- Hervorragend für Dekoratoren, OOP-Grundlagen und Code-Qualität

**"Effective Python" von Brett Slatkin**
- 90 konkrete Tipps für besseren Python-Code
- 

**"Fluent Python" von Luciano Ramalho**
- Tiefgehende Erläuterung fortgeschrittener Python-Konzepte
- Unverzichtbar für tiefes Python-Verständnis (2. Auflage empfohlen)

### Online-Ressourcen

- **Python Documentation** ([docs.python.org](https://docs.python.org)) - Offizielle Referenz und Tutorials
- **Real Python** ([realpython.com](https://realpython.com)) - Hochwertige Tutorials zu allen Themen
- **PEP 8** - [Style Guide](https://peps.python.org/pep-0008/) for Python Code (essentiell für Code-Qualität)
- **Raymond Hettinger PyCon Talks** ([YouTube](https://www.youtube.com/playlist?list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA)) - Insights von Python Core Developern
- **James Powell: So you want to be a Python expert? | PyData Seattle 2017** [YouTube](https://youtu.be/cKPlPJyQrt4?si=809g7Qkl9PNkGPX2) - Inspirierende Einblicke in fortgeschrittene Python-Konzepte
- **Codewars** ([codewars.com](https://www.codewars.com)) - Programmier-Challenges zur Übung
- **LeetCode** ([leetcode.com](https://leetcode.com)) - Algorithmus- und Datenstruktur-Übungen 