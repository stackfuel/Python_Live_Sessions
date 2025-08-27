# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Erweiterte Python Syntax (Syntactic Sugar)
#
# In diesem Notebook lernen wir fortgeschrittene Python-Syntaxelemente kennen, die Code eleganter, lesbarer und effizienter machen. Diese "syntaktischen Zuckergüsse" sind ein wichtiger Teil der Python-Philosophie: "Es sollte eine – und vorzugsweise nur eine – offensichtliche Möglichkeit geben, etwas zu tun."
#

# %% [markdown]
# ## 1. List-, Dict- und Set-Comprehensions
#
# Comprehensions erlauben es uns, neue Datenstrukturen auf elegante und kompakte Weise zu erzeugen. Sie kombinieren Schleifen und bedingte Logik in einer einzigen Zeile, was den Code lesbarer und oft effizienter macht.

# %%
# "Normale" Schleife zur Erstellung einer Liste
quadrate = []
for x in range(10):
    quadrate.append(x**2)
print(f"Mit Schleife erzeugt: {quadrate}")

# Gleiche Liste mit List Comprehension
quadrate_comp = [x**2 for x in range(10)]
print(f"Mit List Comprehension: {quadrate_comp}")

# %% [markdown]
# Comprehensions können auch bedingte Ausdrücke enthalten:

# %%
# List Comprehension mit Bedingung (nur gerade Zahlen)
gerade_quadrate = [x**2 for x in range(10) if x % 2 == 0]
print(f"Quadrate der geraden Zahlen: {gerade_quadrate}")

# %% [markdown]
# ### 1.1 Dictionary Comprehensions
# Mit Dictionary Comprehensions können wir auf ähnliche Weise neue Dictionaries erstellen:

# %%
# Dictionary Comprehension: Zahlen -> Quadratzahlen
quadrat_dict = {x: x**2 for x in range(6)}
print(f"Dictionary mit Quadratzahlen: {quadrat_dict}")


# %%

# Dictionary Comprehension mit Bedingung
gerade_quadrat_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Dictionary mit Quadraten gerader Zahlen: {gerade_quadrat_dict}")


# %%

# Umkehrung eines Dictionaries mit Dictionary Comprehension
original = {'a': 1, 'b': 3, 'c': 3}


# %%
original.items()

# %%

umgekehrt = {wert: schluessel for schluessel, wert in original.items()}
print(f"Originales Dictionary: {original}")
print(f"Umgekehrtes Dictionary: {umgekehrt}")

# %% [markdown]
# ### 1.2 Set Comprehensions
# Set Comprehensions erstellen auf ähnliche Weise Mengen (Sets):

# %%
# Set Comprehension
quadrat_set = {x**2 for x in range(10)}
print(f"Set mit Quadratzahlen: {quadrat_set}")


# %%

# Beachte: Doppelte Werte werden automatisch entfernt
zahlen = [1, 2, 2, 3, 3, 3, 4, 5, 5]
eindeutige_zahlen = {x for x in zahlen}
print(f"Originale Liste mit Duplikaten: {zahlen}")
print(f"Set ohne Duplikate: {eindeutige_zahlen}")

# %%
set(zahlen)

# %% [markdown]
# ### 1.3 Verschachtelte Comprehensions
# Comprehensions können auch verschachtelt werden, was besonders nützlich ist, um mit mehrdimensionalen Daten zu arbeiten:

# %%
# Verschachtelte List Comprehension: Erstellen einer Matrix
matrix = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Matrix 5x5:")
for zeile in matrix:
    print(zeile)

# Flatten einer Matrix (aus 2D zu 1D)
flach = [element for zeile in matrix for element in zeile]
print(f"Flache Liste aus Matrix: {flach[:10]}... (gekürzt)")

# %% [markdown]
# ## 2. Lambda-Funktionen
#
# Lambda-Funktionen sind anonyme Funktionen (Funktionen ohne Namen), die in einer einzigen Zeile definiert werden können. Sie sind nützlich, wenn wir eine kleine Funktion nur einmal benötigen, z.B. als Argument für `map()`, `filter()` oder `sorted()`.

# %%
# "Normale" Funktion
def quadriere(x):
    return x**2

# Äquivalente Lambda-Funktion
quadriere_lambda = lambda x: x**2

print(f"Normale Funktion: {quadriere(5)}")
print(f"Lambda-Funktion: {quadriere_lambda(5)}")

# %%
quadriere.__name__

# %%
q = quadriere

q(5)

# %%
quadriere_lambda.__name__

# %%
quadriere_lambda(12)

# %% [markdown]
# Lambda-Funktionen werden oft als Argumente für höherwertige Funktionen verwendet:

# %%
# Verwendung mit map() - wendet eine Funktion auf jedes Element einer Sequenz an
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x**2, zahlen))
print(f"Quadratzahlen mit map(): {quadrate}")


# %%

# Verwendung mit filter() - filtert Elemente basierend auf einer Bedingung
gerade = list(filter(lambda x: x % 2 == 0, zahlen))
quadrate = list(map(lambda x: x**2, zahlen))
print(f"Gefilterte gerade Zahlen: {gerade}")


# %%
sorted([5, 2, -7, 12], key=abs)

# %%

# Verwendung mit sorted() - sortiert mit benutzerdefiniertem Schlüssel
personen = [
    {'name': 'Alice', 'alter': 30},
    {'name': 'Bob', 'alter': 25},
    {'name': 'Charlie', 'alter': 35}
]
sortiert_nach_alter = sorted(personen, key=lambda person: person['alter'])
print(f"Nach Alter sortiert: {sortiert_nach_alter}")

# %% [markdown]
# Es ist wichtig zu beachten, dass Lambda-Funktionen auf einfache Ausdrücke beschränkt sind. Für komplexere Funktionen sollten normale Funktionsdefinitionen verwendet werden.

# %% [markdown]
# ## 3. With-Statement und Context Manager
#
# Das `with`-Statement erstellt einen Kontext, in dem Ressourcen automatisch verwaltet werden. Dies ist besonders nützlich für Operationen, die eine Bereinigung erfordern, wie das Schließen von Dateien oder das Freigeben von Netzwerkverbindungen.

# %%
# Dateien ohne with-Statement (traditionell)
f = open('beispiel.txt', 'w')
try:
    f.write('Hallo Welt!\n')
finally:
    f.close()  # Muss manuell geschlossen werden


# %%

# Gleiche Operation mit with-Statement
with open('beispiel.txt', 'w') as f:
    f.write('Hallo mit with-Statement!\n')
# Datei wird automatisch geschlossen, wenn der Block verlassen wird


# %%

# Lesen der Datei
with open('beispiel.txt', 'r') as f:
    inhalt = f.read()
print(f"Dateiinhalt: {inhalt}")

# %% [markdown]
# Das `with`-Statement kann auch mehrere Context Manager gleichzeitig verwalten:

# %%
# Mehrere Context Manager
with open('quelle.txt', 'w') as quelle, open('ziel.txt', 'w') as ziel:
    quelle.write('Quelldaten\n')
    ziel.write('Zieldaten\n')
# Beide Dateien werden automatisch geschlossen

# %% [markdown]
# ### 3.1 Eigene Context Manager mit Klassen
#
# Wir können eigene Context Manager erstellen, indem wir die Methoden `__enter__` und `__exit__` implementieren:

# %%
class MeinContextManager:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"Context '{self.name}' wird betreten")
        return self  # Gibt das Objekt zurück, das dem as-Ausdruck zugewiesen wird
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Context '{self.name}' wird verlassen")
        # Rückgabewert True unterdrückt Ausnahmen
        return False  # Ausnahmen werden nicht unterdrückt

# Verwendung des eigenen Context Managers
with MeinContextManager("Test") as cm:
    print("Innerhalb des Context Managers")
    print(f"Verwendung des Context Manager Objekts: {cm.name}")

# %% [markdown]
# ## 4. Tuple Unpacking und *-Operatoren
#
# Tuple Unpacking ermöglicht es, die Elemente eines Tuples (oder einer anderen Sequenz) in einzelne Variablen zu "entpacken". Der `*`-Operator kann zum Packen und Entpacken von variablen Argumenten verwendet werden.

# %%
# Einfaches Tuple Unpacking
koordinaten = (10, 20)


# %%
koordinaten
x = koordinaten[0]
y = koordinaten[1]

# %%

x, y = koordinaten
print(f"x = {x}, y = {y}")


# %%

# Unpacking funktioniert mit jeder Sequenz
liste = [1, 2, 3]
a, b, c = liste
print(f"a = {a}, b = {b}, c = {c}")


# %%

# Tauschen von Variablen ohne temporäre Variable
a, b = 10, 20
print(f"Vor dem Tausch: a = {a}, b = {b}")
a, b = b, a
print(f"Nach dem Tausch: a = {a}, b = {b}")

# %% [markdown]
# ### 4.1 Die *-Syntax zum Entpacken
#
# Mit dem `*`-Operator können wir restliche Elemente in einer Liste sammeln oder eine Liste in einzelne Argumente entpacken:

# %%
# Sammeln von Argumenten mit *
erster, zweiter, *rest = [1, 2, 3, 4, 5]
print(f"Erster: {erster}, Zweiter: {zweiter},  Rest: {rest}")


# %%

*anfang, letzter = [1, 2, 3, 4, 5]
print(f"Anfang: {anfang}, Letzter: {letzter}")


# %%

erster, *mitte, letzter = [1, 2, 3, 4, 5]
print(f"Erster: {erster}, Mitte: {mitte}, Letzter: {letzter}")


# %% [markdown]
# ### 4.2 Die *-Syntax in Funktionen
#
# In Funktionen kann der `*`-Operator verwendet werden, um eine variable Anzahl von Positionsargumenten zu empfangen oder um Sequenzen als einzelne Argumente zu übergeben:

# %%
# Funktion mit variabler Argumentanzahl
def summe(*zahlen):
    print(zahlen)
    result = 0
    for zahl in zahlen:
        result += zahl
    return result

print(f"Summe von 1, 2, 3: {summe(1, 2, 3)}")
print(f"Summe von 5, 10, 15, 20: {summe(5, 10, 15, 20, 25, -12)}")


# %%

# Entpacken einer Sequenz als Argumente
zahlen = [1, 2, 3, 4, 5]
print(f"Summe der Liste: {summe(*zahlen)}")


# %% [markdown]
# ### 4.3 Die **-Syntax für Dictionaries
#
# Analog dazu kann der `**`-Operator verwendet werden, um Dictionaries in Schlüssel-Wert-Paare zu entpacken oder um eine variable Anzahl von Schlüsselwortargumenten zu sammeln:

# %%
# Funktion mit variabler Anzahl von Schlüsselwortargumenten
def beschreibe_person(name, **eigenschaften):
    print(f"Name: {name}")
    for eigenschaft, wert in eigenschaften.items():
        print(f"  {eigenschaft}: {wert}")

beschreibe_person("Alice", alter=30, beruf="Entwicklerin", hobby="Lesen")


# %%

# Entpacken eines Dictionaries als Schlüsselwortargumente
person_info = {
    "name": "Bob",
    "alter": 25,
    "beruf": "Designer",
    "wohnort": "Berlin"
}

beschreibe_person(**person_info)


# %%

# Kombinieren von Dictionaries mit **
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
kombiniert = {**dict1, **dict2}
print(f"Kombiniertes Dictionary: {kombiniert}")

# %% [markdown]
# ## 5. F-Strings und String-Formatierung
#
# F-Strings (Formatted String Literals) sind eine leistungsstarke und lesbare Methode zur String-Formatierung, die seit Python 3.6 verfügbar ist.

# %%
# Traditionelle String-Formatierung mit %
name = "Alice"
alter = 30
print("Hallo, ich bin %s und %d Jahre alt." % (name, alter))

# Formatierung mit str.format()
print("Hallo, ich bin {} und {} Jahre alt.".format(name, alter))
print("Hallo, ich bin {0} und {1} Jahre alt. {0} ist ein schöner Name.".format(name, alter))


# %%
s = "Hallo ich bin {name}"

s.format(name=name)



# %%
s = f"Hallo {name}"

# %%



# F-Strings (ab Python 3.6)
print(f"Hallo, ich bin {name} und {alter} Jahre alt.")

# Ausdrücke in F-Strings
print(f"Die Summe von 2 + 2 ist {2 + 2}.")
print(f"{name.upper()} ist {2023 - alter} geboren.")

# %% [markdown]
# F-Strings bieten erweiterte Formatierungsoptionen mit spezifischen Formatspezifikatoren:

# %%
# Formatierungsoptionen
pi = 3.14159265359
print(f"Pi: {pi}")
print(f"Pi auf 2 Dezimalstellen: {pi:.2f}")
print(f"Pi in wissenschaftlicher Notation: {pi:.2e}")
print(f"Pi als Prozent: {pi:.2%}")


# %%

# Zahlenformatierung
betrag = 1234567.897654
print(f"Währungsformatierung: ${betrag:,.2f}")

# Ausrichtung und Breite
for i in range(1, 100):
    print(f"{i:2d} hoch 2 = {i**2:3d}")

# %% [markdown]
# ### 5.1 Debugging mit F-Strings
#
# In Python 3.8 wurde ein "Debugging"-Syntax für F-Strings eingeführt, der den Variablennamen zusammen mit seinem Wert anzeigt:

# %%
# F-String Debugging (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}")
print(f"{x+y=}")
print(f"{x*y=}")

# %% [markdown]
# ## 6. Ternary Operator
#
# Der ternäre Operator in Python hat die Form `x if condition else y`. Er ermöglicht bedingte Ausdrücke in einer einzigen Zeile.

# %%
# Herkömmliche if-else-Struktur
a = 5
b = 10
if a > b:
    maximum = a
else:
    maximum = b
print(f"Maximum (mit if-else): {maximum}")

# Äquivalent mit dem ternären Operator
maximum = a if a > b else b
print(f"Maximum (mit ternärem Operator): {maximum}")

# %% [markdown]
# Der ternäre Operator kann auch verschachtelt werden, was jedoch die Lesbarkeit beeinträchtigen kann:

# %%
# Einfache Verwendung
alter = 19
status = "Kind" if alter < 18 else "Erwachsener"
print(f"Status: {status}")


# %%

# Verschachtelte ternäre Operatoren
alter = 65
status = "Kind" if alter < 18 else "Senior" if alter >= 65 else "Erwachsener"
print(f"Status: {status}")

# Besser lesbar mit mehreren Zeilen oder normalen if-elif-else-Strukturen
status = (
    "Kind" if alter < 18 else
    "Senior" if alter >= 65 else
    "Erwachsener"
)
print(f"Status (besser formatiert): {status}")

# %% [markdown]
# ### 6.1 Ternary Operator in (List)-Comprehensions
#
# Der Ternary Operator wird oft in List Comprehensions verwendet um elemente in Abhängigkeit einer Bedingung zu erzeugen.

# %%
print([a**2 if a>0 else a for a in range(-5, 6)])

# %% [markdown]
# ## 7. Walrus-Operator `:=`
#
# Der Walrus-Operator `:=` wurde in Python 3.8 eingeführt. Er ermöglicht es, einer Variable im Rahmen eines Ausdrucks einen Wert zuzuweisen und dann diesen Wert im selben Ausdruck zu verwenden.

# %%
# Traditioneller Ansatz
string = "Hallo Welt"
length = len(string)
if length > 5:
    print(f"Der String '{string}' hat {length} Zeichen, das ist mehr als 5.")


# %%

# Mit dem Walrus-Operator
string_2 = "Tschüs Welt"
if (length_2 := len(string_2)) > 5:
    print(f"Der String '{string_2}' hat {length_2} Zeichen, das ist mehr als 5.")

# %% [markdown]
# Der Walrus-Operator ist besonders nützlich in Schleifen oder Comprehensions, wo ein Ausdruck berechnet und dann verwendet werden muss:

# %%
# Traditionell: Berechnung wird zweimal durchgeführt
zahlen = [1, 2, 3, 4, 5]
quadrate = [x**2 for x in zahlen if x**2 > 10]
print(f"Quadrate > 10 (traditionell): {quadrate}")

# Mit Walrus: Berechnung wird nur einmal durchgeführt
quadrate_walrus = [q for x in zahlen if (q := x**2) > 10]
print(f"Quadrate > 10 (mit Walrus): {quadrate_walrus}")

# %% [markdown]
# ## 8. Chaining von Vergleichsoperatoren
#
# In Python können Vergleichsoperatoren aneinandergereiht (chained) werden, was den Code lesbarer macht und unnötige Wiederholungen vermeidet.

# %%
# Traditionelle Vergleiche mit 'and'
x = 5
if x > 0 and x < 10:
    print("x liegt zwischen 0 und 10 (traditioneller Vergleich)")

# Äquivalent mit Operator Chaining
if 0 < x < 10:
    print("x liegt zwischen 0 und 10 (Operator Chaining)")

# Komplexere Verkettungen
y = 7
if 0 < x < y < 10:
    print(f"x ({x}) ist größer als 0, kleiner als y ({y}), und y ist kleiner als 10")

# %% [markdown]
# Operator Chaining funktioniert mit allen Vergleichsoperatoren (`<`, `<=`, `>`, `>=`, `==`, `!=`) und kann gemischt werden:

# %%
# Verschiedene Vergleichsoperatoren in einer Kette
a, b, c = 3, 5, 7
if a < b <= c:
    print(f"a ({a}) ist kleiner als b ({b}), und b ist kleiner oder gleich c ({c})")

if a < b != c > a:
    print("Komplexe Bedingung ist wahr")

# %% [markdown]
# ### 8.1 Operatorreihenfolge (Precedence)
#
# In Python gibt es eine festgelegte Reihenfolge, in der Operatoren ausgewertet werden. Es ist wichtig, diese zu kennen, um unerwartetes Verhalten zu vermeiden.

# %%
# Beispiel für Operatorreihenfolge
x = 5
y = 10
z = 15

# Arithmetische Operatoren haben Vorrang vor Vergleichsoperatoren
result = x + y < z
print(f"x + y < z: {result} (Berechnung: {x + y} < {z})")

# Logische Operatoren: not hat Vorrang vor and, and hat Vorrang vor or
result = not x < y and z > y or x == 5
print(f"not x < y and z > y or x == 5: {result}")

# Auswertungsreihenfolge mit Klammern verdeutlichen
result = (not (x < y)) and (z > y or x == 5)
print(f"(not (x < y)) and (z > y or x == 5): {result}")

# %% [markdown]
# Hier ist eine vereinfachte Darstellung der Operatorreihenfolge in Python (von höchster zu niedrigster Priorität):
#
# 1. Klammerausdrücke `()`
# 2. Potenzierung `**`
# 3. Unäre Operatoren `+x`, `-x`, `~x`
# 4. Multiplikation, Division `*`, `/`, `//`, `%`
# 5. Addition, Subtraktion `+`, `-`
# 6. Bitweise Shifts `<<`, `>>`
# 7. Bitweises AND `&`
# 8. Bitweises XOR `^`
# 9. Bitweises OR `|`
# 10. Vergleiche `<`, `<=`, `>`, `>=`, `!=`, `==`
# 11. `is`, `is not`, `in`, `not in`
# 12. Logisches NOT `not`
# 13. Logisches AND `and`
# 14. Logisches OR `or`

# %% [markdown]
# ## 9. Structural Pattern Matching (Match-Case)
#
# Structural Pattern Matching wurde in Python 3.10 eingeführt und bietet eine elegante Möglichkeit, komplexe Bedingungsprüfungen durchzuführen. Es ähnelt der `switch`-`case`-Struktur aus anderen Sprachen, ist aber deutlich mächtiger.

# %%
# Einfaches Pattern Matching
def check_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # Default-Fall
            return f"Unbekannter Status: {status_code}"

print(f"HTTP 200: {check_status(200)}")
print(f"HTTP 404: {check_status(404)}")
print(f"HTTP 302: {check_status(302)}")

# %% [markdown]
# ### 9.1 Komplexe Muster und Guards
#
# Pattern Matching unterstützt komplexe Muster, einschließlich der Zerlegung von Datenstrukturen, OR-Muster und Bedingungsprüfungen (Guards):

# %%
# Pattern Matching mit strukturierten Daten
def analyze_point(point):
    match point:
        case (0, 0):
            return "Ursprung"
        case (0, y):
            return f"Y-Achse bei y={y}"
        case (x, 0):
            return f"X-Achse bei x={x}"
        case (x, y) if x == y:
            return f"Punkt auf der Diagonalen: ({x}, {y})"
        case (x, y):
            return f"Punkt bei ({x}, {y})"

print(analyze_point((0, 0)))
print(analyze_point((0, 5)))
print(analyze_point((3, 0)))
print(analyze_point((2, 2)))
print(analyze_point((3, 4)))

# %% [markdown]
# ### 9.2 Musterabgleich mit Klassen
#
# Pattern Matching ist besonders nützlich für den Abgleich mit Objekten und deren Attributen:

# %%
# Klassen für Pattern Matching
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# Funktion mit Pattern Matching für verschiedene Formen
def describe_shape(shape):
    match shape:
        case Point(x=0, y=0):
            return "Punkt im Ursprung"
        case Point(x=x, y=y):
            return f"Punkt bei ({x}, {y})"
        case Rectangle(pos=Point(x=0, y=0), width=w, height=h):
            return f"Rechteck mit Ursprung (0, 0), Breite {w} und Höhe {h}"
        case Rectangle(pos=pos, width=w, height=h):
            return f"Rechteck bei ({pos.x}, {pos.y}), Breite {w} und Höhe {h}"
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"Kreis mit Mittelpunkt im Ursprung und Radius {r}"
        case Circle(center=center, radius=r):
            return f"Kreis mit Mittelpunkt ({center.x}, {center.y}) und Radius {r}"
        case _:
            return "Unbekannte Form"

point = Point(3, 4)
rect = Rectangle(Point(0, 0), 10, 20)
circle = Circle(Point(5, 5), 15)

print(describe_shape(point))
print(describe_shape(rect))
print(describe_shape(circle))

# %% [markdown]
# ## 10. Type Hints
#
# Type Hints wurden in Python 3.5 eingeführt und ermöglichen es, den erwarteten Typ von Variablen, Funktionsparametern und Rückgabewerten anzugeben. Sie werden nicht zur Laufzeit überprüft, sondern dienen hauptsächlich der Dokumentation und der statischen Typprüfung durch externe Tools.

# %%
def greeting(name):
    return f"Hallo {name}"


# Einfache Type Hints
def greeting(name: str) -> str:
    return f"Hallo {name}"




print(greeting("Python"))

# Type Hints für Variablen
user_id: int = 12345
is_active: bool = True
username: str = "alice"

# %% [markdown]
# Type Hints unterstützen komplexe Typen aus dem `typing`-Modul:

# %%
from typing import List, Dict, Tuple, Optional, Union, Any, Callable

# Listen
def double_all(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

print(double_all([1, 2, 3, 4]))



# %%

# Dictionaries
def count_words(text: str) -> Dict[str, int]:
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}

print(count_words("Die Katze ist eine Katze"))


# %%

# Optionale Parameter
def greet_user(name: Optional[str] = None) -> str:
    if name is None:
        return "Hallo Gast"
    return f"Hallo {name}"

print(greet_user())
print(greet_user("Max"))


# %%

# Union-Typen (entweder str oder int)
def process_id(user_id: Union[str, int]) -> str:
    return f"Verarbeite ID: {user_id}"

print(process_id(12345))
print(process_id("AB-12345"))
