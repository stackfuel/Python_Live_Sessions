# Python Live Sessions

## Einleitung

Willkommen zu den **Python Live Sessions** von StackFuel! Diese Sessions sind als **begleitendes, freiwilliges Angebot** für alle Teilnehmenden der StackFuel-Kurse konzipiert. Da die meisten Trainings auf Python aufbauen, vermitteln wir hier systematisch die grundlegenden Konzepte der Programmiersprache.

Die Sessions sind in zwei parallele Bereiche unterteilt:
- **Python Basics**: *Montags 13:30 Uhr* - Grundlagen für Data Analytics (DAN) und Data Science (DSC) Teilnehmende
- **Python Advanced**: *Donnerstags 13:30 Uhr* - Vertiefende Konzepte für Weiterführende Programmierung (WPP), Objektorientierte Programmierung (OOP) und Data Science Portfolio Projekt (DPP) Teilnehmer

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

Die Advanced Sessions vertiefen das Python-Wissen und behandeln fortgeschrittene Konzepte der objektorientierten Programmierung. Sie richten sich an Teilnehmende der Kurse **Weiterführende Programmierung (WPP)**, **Objektorientierte Programmierung (OOP)** und **Data Science Portfolio Projekt (DPP)**. Es sind aber alle interessierten Teilnehmenden willkommen.

### 1. Technisches Setup

Diese Session bereitet Sie auf professionelle Python-Entwicklung vor und ist **essentiell für DPP-Teilnehmer**.

- **Visual Studio Code Setup**: Konfiguration der IDE für optimale Python-Entwicklung
- **Virtuelle Umgebungen mit uv**: Moderne Abhängigkeitsverwaltung und Projekt-Isolation

### 2. Objektorientierte Programmierung - Grundlagen

Diese Session führt in die Grundkonzepte der objektorientierten Programmierung ein anhand einer praktischen Vector-Klassen-Implementierung.

- **Klassen und Objekte**: Grundlegende OOP-Konzepte
  - *Klassendefinition* und *Instanziierung*
  - Das `self`-Argument verstehen
- **Attribute**: Eigenschaften von Objekten
- **Methoden**: Funktionen innerhalb von Klassen
- **Special Methods**: Implementierung von Operatoren
  - `__add__`, `__sub__`, `__mul__` etc. zum Überladen von Operatoren
  - `__str__`, `__repr__` für String-Repräsentation
- **Praktisches Projekt**: Vollständige Vector-Klasse mit mathematischen Operationen

### 3. Higher Order Functions und Dekoratoren

Diese Session behandelt fortgeschrittene Funktionskonzepte und die mächtige Decorator-Syntax von Python.

- **Variable Argumentlisten**: Flexible Funktionsparameter
  - `*args`: Variable Anzahl positionaler Argumente
  - `**kwargs`: Variable Anzahl benannter Argumente
- **Closures**: Verschachtelte Funktionen und Zustandsspeicherung
- **Dekoratoren**: Funktionserweiterung mit `@`-Syntax
  - Grundlagen der Decorator-Implementierung
  - `functools.wraps`: Metadaten-Erhaltung
- **Built-in Dekoratoren**:
  - `@property`: Getter/Setter-Implementierung
  - `@classmethod`: Klassenmethoden
  - `@staticmethod`: Statische Methoden

### 4. Python Data Model

Diese Session erklärt, wie Sie eigene Klassen nahtlos in Python's Ökosystem integrieren können.

- **Callable Objects**: `__call__` für funktionsähnliche Objekte
- **Iteration Protocol**: 
  - `__iter__` und `__next__` für eigene Iteratoren
  - *Generator-Funktionen* mit `yield`
- **Container Types**:
  - **Sequences**: `__getitem__`, `__setitem__`, `__delitem__`
  - **Mappings**: `__contains__` für Zugehörigkeitstests
- **Context Managers**: Ressourcenverwaltung
  - `__enter__` und `__exit__` implementieren
  - `@contextmanager` Decorator
- **Numerische Operationen**:
  - Arithmetische Operatoren: `__add__`, `__sub__`, `__mul__`, `__truediv__`
  - Vergleichsoperatoren: `__eq__`, `__lt__`, `__gt__` etc.
- **Object Lifecycle**:
  - `__init__`: Objekt-Initialisierung
  - `__new__`: Instanz-Erzeugung  
  - `__del__`: Aufräumarbeiten
- **Hashing und Repräsentation**: `__hash__` für Hashable Objects

### 5. Vererbung und Komposition

Diese Session behandelt fortgeschrittene OOP-Konzepte für die Strukturierung komplexer Anwendungen.

- **Vererbung**: Wiederverwendung und Erweiterung von Klassen
  - `super()`: Zugriff auf Parent-Class-Methoden
  - **Mehrfachvererbung**: Komplexe Klassenhierarchien
  - **MRO** (Method Resolution Order): Methodenauflösung verstehen
- **Komposition**: Alternative zu Vererbung durch Objektzusammensetzung


### 6. Erweiterte OOP-Konzepte

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
- **Codewars** ([codewars.com](https://www.codewars.com)) - Programmier-Challenges zur Übung
- **LeetCode** ([leetcode.com](https://leetcode.com)) - Algorithmus- und Datenstruktur-Übungen