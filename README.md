


# Live Sessions
Die Themen der Live Sessions sind in zwei Bereiche geteilt. Die Basics- und Advanced-Sessions laufen jeweils wöchentlich parallel zueinander.  

Montags 13.30: Python Basics  
Donnerstags 13.30: Python Advanced  

Live Sessions dauern ca. 1,5 - 2 Stunden und behandeln ein konkretes Thema. Für die einzelnen Sessions gibt es Jupyter Notebooks (Basics) bzw. Python-Skripte (Advanced) in den jeweiligen Unterordnern. Die Sessions dienen als begleitendes, freiwilliges Angebot für die Teilnehmer aller StackFuel-Kurse. Da die meisten Trainings auf der Programmiersprache Python aufbauen, werden hier grundlegende Konzepte der Sprache vermittelt. Dabei handelt es sich um Themen zur Kernsprache selbst. Bibliotheken wie sklearn, numpy, matplotlib etc. werden in den Trainings bzw. anderen Sessions behandelt.

## Basics Sessions (DAN, DSC)
Die Basic Sessions richten sich üblicherweise an die Teilnehmer der Data Analytics (DAN) und Data Science (DSC) Kurse. Es werden die grundlegenden Sprachkonstrukte vermittelt, die für die Datenanalyse nötig sind. Die Sessions sind freiwillig und können von den Teilnehmenden bei Interesse besucht werden. Allerdings bauen die Konzepte stark aufeinander auf, sodass es sinnvoll ist, die Sessions regelmäßig zu besuchen.

1. **Einfache Datentypen**

    Einführung in die grundlegenden Datentypen von Python.
    
    - `bool`: Wahrheitswerte für logische Aussagen
    - `int`: Ganzzahlen ohne Dezimalstellen
    - `float`: Gleitkommazahlen für mathematische Berechnungen
    - `str`: Zeichenketten für Textdaten
    - `None`: Spezieller Typ für nicht vorhandene Werte
    - expressions
    - variablen
    - zuweisungen
    - operatoren

2. **Einfache Datenstrukturen**
    - `tuple`: Unveränderliche, geordnete Sammlung von Elementen
    - `list`: Änderbare, geordnete Sammlung von Elementen
    - `set`: Ungeordnete Sammlung von eindeutigen Elementen
    - `dict`: Sammlung von Schlüssel-Wert-Paaren
    - eigenschaften
        - iterable
        - mutable vs. imutable

3. **Kontrollstrukturen**
    - `if/else`: Bedingte Ausführung von Codeblöcken
    - `pass`: ...
    - `while`: Wiederholung von Codeblöcken solange Bedingungen wahr sind
    - `break/continue`: Unterbrechung von Schleifen
    - `try/except/finally`: Fehlerbehandlung und Ausnahmeverarbeitung
    - `for`: Iteration über Elemente von Sequenzen

4. **Grundlagen Funktionen**
    - `def`: Definition von Funktionen zur Wiederverwendung von Code
    - `return`: Rückgabe eines Wertes aus einer Funktion
    - Funktionen Aufrufen
    - parameter/argumente: Übergabe von Werten an Funktionen
        - named Parameter und Default-Werte
    - name spaces
        - globale vs. lokale variablen (niemals global verwenden!!!)


5. **Algorithmen**
    - Einführung in die Problemlösung mit algorithmischen Ansätzen
    - Beispiele bekannter Algorithmen (z.B. Sortier- und Suchalgorithmen)
    - Euklidischer Algorithmus, Primzahlen Generator
    - Laufzeitverhalten von Algorithmen bewerten
    - rekursion 

6. **Erweiterte Python Syntax (Syntactic Sugar)**
    - list-, dict-, set-comprehensions: Erzeugung von Datenstrukturen auf elegante Weise
    - lambda funktionen: Kurzdefinition anonymer Funktionen
    - with statement und context manager: Ressourcenmanagement und -freigabe
    - tuple unpacking / *-Operatoren
    - f-strings und string formatting
    - ternary Operator: `x if condition else y`
    - Walrus-Operator `:=`: Variablenzuweisung innerhalb von Expressions
    - Chaining von Vergleichsoperatoren - `a < b < c` statt `a < b and b < c` und logischen Operatoren operatorreihenfolge
    - Structural Pattern Matching `match`-`case`
    - Type Hints

7. **Iteratoren, Generatoren und Lazy Evaluation**
    - iteratoren: Objekt, das beim Iterieren über eine Sequenz hilft
    - yield: Erzeugung von Generatoren zur schrittweisen Ergebnisproduktion
    - generator comprehensions: Speicher-effiziente Erstellung von Generatoren
    - range, map, filter, zip, enumerate, reversed: Integrierte Funktionen zur Iteration und Manipulation
    - itertools: Modul mit iterativen Funktionen zur Kombination und Manipulation von Daten

8. **Refactoring**
    - PEP8: Style Guide für Python Code
    - Namenskonventionen: Best Practices für Bezeichnernamen
    - Dokumentation: Schreiben von verständlicher und nützlicher Dokumentation
    - (Tests: Erstellung und Ausführung von Tests zur Sicherstellung der Codequalität)
    - Sudoku Projekt: Praktisches Projekt zur Anwendung des gelernten Wissens


## Advanced (WPP, OOP, DPP Vorbereitung)
Die Advanced Sessions richten sich vorwiegend an Teilnehmende der Kurse "Weiterführende Programmierung" (WPP), "Objektorientierte Programmierung" (OOP) und "Data Science / Data Analytics Portfolio Projekt" (DPP). Es wird in zwei Sessions ein einfaches Programmiersetup vorgestellt (VSCode, uv, git), um den Teilnehmenden die Möglichkeit zu geben, die gelernten Inhalte direkt auf ihren eigenen Rechnern auszuführen. Das Setup ist vor allem für Teilnehmende des DPP unverzichtbar. Darauf folgen weitere Sessions zu tiefergehenden Python-Konzepten, insbesondere der objektorientierten Programmierung. Im Gegensatz zu den Basic-Themen wird in den Advanced Sessions überwiegend auf Skripte und Module statt auf Jupyter Notebooks gesetzt, um den Teilnehmenden ein realistisches Bild der Softwareentwicklung zu vermitteln.


**Technisches Setup** (dpp)
    - Verwendung von virtuellen Umgebungen (uv) zur Abhängigkeitsverwaltung
    - Einführung in Visual Studio Code (vscode) für die Python-Entwicklung

**OOP Intro**
    - Vector Klasse Implementieren: Grundlagen der Objektorientierung anhand einer Vector-Klasse
    - Attribute: Eigenschaften von Objekten
    - Methoden: Funktionen innerhalb von Klassen
    - Klassen, Objekte (Instanzen), `self`-Argument
    - Special Methods: `__add__`, `__sub__` etc.

**Higher Order Functions und Dekoratoren**
    - args/kwargs: Arbeiten mit variabler Argumentanzahl
    - closures: Verschachtelte Funktionen und Speichern von Zuständen
    - wrap: Funktionen zur Erhaltung von Metadaten bei Verwendung von Dekoratoren
    - `@`-Syntax: Definieren und Anwenden von Dekoratoren zur Funktionserweiterung
    - properties, classmethod, staticmethod 

**Data Model**
    - callables: Objekte, die wie Funktionen aufgerufen werden können
        - `__call__`: Implementierung von Funktionsaufrufen für Objekte
    - iterables: Objekte, die iteriert werden können
        - `__iter__`: Implementierung der Iteration für benutzerdefinierte Objekte
        - `__next__`: Implementierung der nächsten Iteration für benutzerdefinierte Objekte
        - generatoren: Erzeugung von Iteratoren mit `yield`
    - containers: Objekte, die andere Objekte enthalten können
    - sequence: Objekte, die eine geordnete Sammlung von Elementen darstellen
        - `__getitem__`, `__setitem__`, `__delitem__`: Zugriff und Manipulation von Elementen in Sequenzen
    - mapping: Objekte, die Schlüssel-Wert-Paare enthalten
        - `__contains__`: Überprüfung der Zugehörigkeit von Schlüsseln in Mappings
    - context manager: Objekte, die Ressourcen verwalten und freigeben
        - `__enter__`, `__exit__`: Implementierung von Kontextmanagern für Ressourcenverwaltung
        - @contextmanager: Dekorator zur Erstellung von Kontextmanagern
    - numerische Typen: Implementierung von numerischen Operationen
        - `__add__`, `__sub__`, `__mul__`, `__truediv__`: Implementierung von arithmetischen Operationen
        - Vergleichsoperatoren: `__eq__`, `__lt__`, `__gt__` etc. für benutzerdefinierte Vergleiche

    - Hashing: `__hash__` und `__repr__` für benutzerdefinierte Hash-Funktionen und Repräsentationen
    - `__str__`: Benutzerdefinierte String-Repräsentation von Objekten
    - `__init__`: Konstruktor für die Initialisierung von Objekten
    - `__new__`: Erzeugung neuer Instanzen von Klassen
    - `__del__`: Aufräumarbeiten beim Löschen von Objekten

**Vererbung/Komposition**
    - Vererbung: Wiederverwendung von Eigenschaften und Methoden zwischen Klassen
    - Super: Zugriff auf Methoden der Basisklasse
    - Mehrfachvererbung: Vererbung von mehreren Basisklassen
    - Komposition: Erstellen komplexer Objekte durch Kombinieren kleinerer Objekte
    - Interfaces: Definition von Verträgen für Klassen
    - Abstrakte Klassen: Definition von Basisklassen mit unvollständigen Implementierungen
    - Polymorphismus: Verwendung von Objekten unterschiedlicher Klassen auf ähnliche Weise
    - Duck Typing: Verwendung von Objekten basierend auf ihrem Verhalten statt ihrem Typ
    - MRO (Method Resolution Order): Reihenfolge, in der Methoden aufgerufen werden

**Erweiterte OOP Konzepte**
    - Dataclasses: Vereinfachte Klassen für Datenverwaltung
    - Enums: Vereinfachte Klassen für Aufzählungen
    - Namedtuples: Unveränderliche, benannte Tupel für strukturierte Daten
    - Defaultdict: Erweiterung von Dictionaries mit Standardwerten
    - Counter: Zähler für die Häufigkeit von Elementen in Sammlungen
    - Mixins: Wiederverwendbare Klassen für zusätzliche Funktionalität
    - Metaclasses: Klassen, die Klassen erstellen und deren Verhalten steuern


### Optionale Themen
**Unit Testing**
    - Einführung in das Schreiben und Ausführen von Unit Tests
    - Verwenden von Test-Frameworks wie unittest oder pytest zur Sicherstellung der Funktionalität

**Einführung in git** (dpp)
    - Grundlagen der Versionskontrolle mit Git
    - Grundlegende Befehle für Repository-Verwaltung und Zusammenarbeit

**Module und Pakete**
    - Module: Organisation von Code in separate Dateien
    - Pakete: Strukturierung von Modulen in Verzeichnissen
    - Importieren von Modulen und Paketen
    - Namensräume: Vermeidung von Namenskonflikten durch Module
    - `__init__.py`: Initialisierung von Paketen





# Weiteres
Themen die beim Brainstorming übrig geblieben sind.
- scripte module und packages / Projektstruktur
- data storytelling (teilweise schon in dan)
- logging
- Fehlerbehandlung / Debugging
- Funktionale Programmierung
- Design Patterns
- APIs und Webdienste
- asynchrone Programmierung
- multiprocessing, threading
- Arbeiten mit Dateien und Dateisystemen
- Reguläre Ausdrücke
- python executable (exe bauen)
- gui programmierung





