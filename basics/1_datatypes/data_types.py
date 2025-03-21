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
# # Python "primitive" Datentypen
#
# ## 1. Einleitung
# In diesem Notebook lernen wir die grundlegenden Datentypen in Python kennen.
#
# In Python werden Informationen bzw. Daten in **Objekten** gespeichert. Diese Objekte sind immer von einem bestimmten **Typ**. Der Typ eines Objektes bestimmt, welche art von Daten in dem Objekt gespeichert, und welche operationen mit dem Objekt ausgeführt werden können.
#
# Zwei Zahlen `3` und `9` werden Beispielsweise in dem Datentyp `int` (Integer) gespeichert. Und da zwei Integer Objekte durch das `+`-Zeichen addiert werden können, können auch die Zahlen `3` und `9` addiert werden:

# %%
3 + 9

# %% [markdown]
# Code wie in der obigen Zelle nennen wir **Ausdruck** (oder Expression). Eine Expression ist ein kleiner Teil Programmcode, der zu einem Objekt ausgewertet werden kann.
#
# Weitere Beispiele für Expressions wären:
# ``` Python
# 3 * (4 - 1)
# [x**2 for x in range(5)]
# max(10, 20, 5)
# "hello".upper()
# ```
#
# Du kannst alle Zeilen in einer Jupyter Zelle ausführen und wirst ein Objekt als Ergebnis bekommen.
#
# Eine Expression alleine ist oft nicht sehr hilfreich. Meistens wollen wir uns den Wert den wir berechnet haben auch abspeichern und später wiederverwenden.
#
# Durch eine **Zuweisung** mit `=` können wir das Ergebnis einer Expression in einer **Variable** speichern.

# %%
meine_variable = 42

# %% [markdown]
# Dieser Code gibt uns kein Ergebnis zurück, da es sich bei dem Code nicht um eine Expression sondern um eine Zuweisung handelt. Die Expression ist nur der Teil, der rechts vom `=` steht (also die `42`).
#
# In der Variable `meine_variable` ist nun ein Objekt vom Typ `int` mit dem Wert `42` gespeichert.

# %% [markdown]
# Python ist eine **dynamisch typisierte** Sprache, was bedeutet, dass wir **Variablen** erstellen können,
# ohne explizit ihren Typ deklarieren zu müssen.
#
# Das hat den Vorteil, dass wir uns um den konkreten Datentyp oft keine Gedanken machen müssen. Es verschleiert aber auch oft, was tatsächlich unter der Haube von Python vor sich geht.

# %%
# Mit der funktion `type` können wir den Datentyp einer variable überprüfen.
print(f"Der Wert ist {meine_variable} und hat den Typ: {type(meine_variable)}")

# %% [markdown]
# ## 2. Einfache Datentypen
#
# In Python gibt es mehrere grundlegende Datentypen, die als "primitiv" betrachtet werden können. Diese Typen bilden die Basis für komplexere Datenstrukturen und sind in der Standardbibliothek von Python enthalten. Im Folgenden lernen wir die wichtigsten primitiven Datentypen kennen und wie sie verwendet werden.
#
# ### 2.1 Boolean (bool)
# Ein Objekt vom Typ `bool` kann nur zwei Werte annehmen: `True` oder `False`. 
#
# Boolean-Werte werden primär für logische Operationen und Bedingungen verwendet. Sie sind das Ergebnis von Vergleichsoperationen und steuern den Ablauf von Kontrollstrukturen wie `if`-Anweisungen und Schleifen.
#
# Wir können Boolean-Werte direkt zuweisen oder durch Vergleiche erzeugen:

# %%
wahr = True
falsch = False

print(f"Typ von wahr: {type(wahr)}")

# %%
# Logische Operationen mit Booleans
print("\nLogische Operationen:")
print(f"True and False: {True and False}")  # Logisches UND: Beide Bedingungen müssen wahr sein
print(f"True or False: {True or False}")    # Logisches ODER: Eine Bedingung muss wahr sein
print(f"not True: {not True}")              # Logische Negation: Kehrt den Wert um

# %%
# Vergleichsoperatoren erzeugen Boolean-Werte
print("\nVergleiche:")
print(f"5 > 3: {5 > 3}")    # Größer als
print(f"5 == 5: {5 == 5}")  # Gleich (Beachte den doppelten Gleichheitsoperator für Vergleiche)
print(f"5 != 10: {5 != 10}") # Ungleich

# %% [markdown]
# Interessanterweise können in Python alle Objekte in einem Boolean-Kontext ausgewertet werden. Die Funktion `bool()` gibt den entsprechenden Boolean-Wert zurück. Einige Beispiele für Werte, die als `False` betrachtet werden:
#
# - `False` (Boolean False)
# - `None` (Der Python Null-Wert)
# - `0` (Integer Null)
# - `0.0` (Float Null)
# - `''` oder `""` (Leerer String)
# - `[]` (Leere Liste)
# - `()` (Leeres Tupel)
# - `{}` (Leeres Dictionary)
# - `set()` (Leeres Set)
#
# Alle anderen Werte werden als `True` angesehen. Diese Eigenschaft wird oft in Bedingungen genutzt, z.B. `if my_list:` prüft, ob die Liste nicht leer ist.

# %%
# Boolean-Konversion von verschiedenen Werten
print("\nBoolean Konvertierung:")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hallo'): {bool('Hallo')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

# %% [markdown]
# ### 2.2 Integer (int)
# Integer sind ganze Zahlen ohne Dezimalstellen. Sie können positiv oder negativ sein und haben in Python keine festgelegte Größenbeschränkung (solange der verfügbare Speicher ausreicht).
#
# Integers werden für die Darstellung von ganzen Zahlen verwendet und unterstützen alle grundlegenden arithmetischen Operationen.
#
# In vielen Programmiersprachen haben Integer eine feste Größe (wie 32 oder 64 Bit), was zu Überlaufproblemen führen kann. In Python werden Integer jedoch automatisch erweitert, wenn sie zu groß werden, was sehr große Zahlen ermöglicht.

# %%
positiv = 42
negativ = -42
gross = 10**20  # 10 hoch 20 - eine sehr große Zahl

print("\nInteger-Beispiele:")
print(f"positiv = {positiv}, Typ: {type(positiv)}")
print(f"negativ = {negativ}, Typ: {type(negativ)}")
print(f"gross = {gross}, Typ: {type(gross)}")


# %%
# Integer-Operationen
a, b = 10, 3
print(f"{a=}")  # Kompakte Ausgabe des Variablennamens und -werts
print(f"{b=}")
print("\nInteger-Operationen:")


print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraktion
print(f"a * b = {a * b}")  # Multiplikation
print(f"a / b = {a / b}")  # Division (Ergebnis ist float)
print(f"a // b = {a // b}")  # Ganzzahlige Division (Abrunden zum nächsten ganzzahligen Wert)
print(f"a % b = {a % b}")  # Modulo (Rest der ganzzahligen Division)
print(f"a ** b = {a ** b}")  # Potenzierung (a hoch b)

# %% [markdown]
# Integer in Python haben einige besondere Eigenschaften:
#
# 1. **Unbegrenzte Präzision**: Python kann mit beliebig großen Zahlen umgehen, ohne dass ein Überlauf auftritt. Dies unterscheidet Python von Sprachen wie C oder Java, wo Integer eine feste Größe haben.
#
# 2. **Automatische Typkonvertierung**: Bei der Division zweier Integer (`/`) gibt Python standardmäßig einen Float zurück, während die ganzzahlige Division (`//`) einen Integer zurückgibt.
#
# 3. **Bitoperationen**: Integer unterstützen bitweise Operationen wie `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (Links-Shift) und `>>` (Rechts-Shift).

# %%
# Demonstration der Bitoperationen
c, d = 10, 6  # In Binär: 10 = 1010, 6 = 0110
print("\nBitweise Operationen:")
print(f"c = {c} (Binär: {bin(c)})")
print(f"d = {d} (Binär: {bin(d)})")
print(f"c & d = {c & d} (Binär: {bin(c & d)})")  # Bitweises AND
print(f"c | d = {c | d} (Binär: {bin(c | d)})")  # Bitweises OR
print(f"c ^ d = {c ^ d} (Binär: {bin(c ^ d)})")  # Bitweises XOR
print(f"~c = {~c} (Binär: {bin(~c)})")           # Bitweises NOT
print(f"c << 1 = {c << 1} (Binär: {bin(c << 1)})")  # Links-Shift (multipliziert mit 2)
print(f"c >> 1 = {c >> 1} (Binär: {bin(c >> 1)})")  # Rechts-Shift (dividiert durch 2)

# %% [markdown]
# ### 2.3 Float (float)
# Floats sind Zahlen mit Dezimalstellen. Sie werden intern mit doppelter Präzision dargestellt (64 Bit IEEE 754), was eine hohe Genauigkeit, aber keine unbegrenzte Präzision bietet.
#
# Floats werden für wissenschaftliche Berechnungen, Messungen und überall dort verwendet, wo Dezimalzahlen benötigt werden. Sie können in der Standardnotation (z.B. `3.14`) oder in wissenschaftlicher Notation (z.B. `2.5e8` für 2.5 × 10⁸) dargestellt werden.
#
# Es ist wichtig zu verstehen, dass Floats aufgrund ihrer binären Darstellung im Speicher nicht alle Dezimalzahlen exakt darstellen können, was zu Rundungsfehlern führen kann.

# %%
x = 3.14          # Standard Dezimalnotation
y = -0.001        # Negative Dezimalzahl
z = 2.5e8         # Wissenschaftliche Notation: 2.5 * 10^8 = 250000000.0
w = 1.23e-5       # Wissenschaftliche Notation für kleine Zahlen: 1.23 * 10^-5 = 0.0000123

print(f"{x=}")
print(f"{y=}")
print(f"{z=}")
print(f"{w=}")


print("\nFloat-Beispiele:")
print(f"x = {x}, Typ: {type(x)}")
print(f"y = {y}, Typ: {type(y)}")
print(f"z = {z}, Typ: {type(z)}")
print(f"w = {w}, Typ: {type(w)}")


# %%
# Umwandlung zwischen int und float
i = 5
f = float(i)  # int zu float
print(f"\nInt {i} zu Float: {f}")

f = 7.8
i = int(f)  # float zu int (schneidet Dezimalstellen ab, kein Runden!)
print(f"Float {f} zu Int: {i}")

# Achtung bei Float-Arithmetik: Rundungsfehler können auftreten
print("\nFloat-Präzision:")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # Ergibt nicht exakt 0.3 wegen binärer Darstellung
print(f"Ist 0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")  # Wird 'False' sein!

# %% [markdown]
# Der Rundungsfehler bei Floats ist ein wichtiges Konzept in der Programmierung. Wenn wir präzise Dezimalberechnungen benötigen, sollten wir das `decimal`-Modul von Python verwenden:

# %%
from decimal import Decimal

print("\nMit dem Decimal-Modul:")
print(f"Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")
print(f"Ist Decimal('0.1') + Decimal('0.2') == Decimal('0.3')? {Decimal('0.1') + Decimal('0.2') == Decimal('0.3')}")

# %% [markdown]
# Floats unterstützen alle arithmetischen Operationen wie Integer, bieten aber auch zusätzliche mathematische Funktionen über das `math`-Modul:

# %%
import math

print("\nMathematische Operationen mit Floats:")
print(f"Quadratwurzel von 25: {math.sqrt(25)}")
print(f"Sinus von Pi/2: {math.sin(math.pi/2)}")
print(f"e hoch 2: {math.exp(2)}")
print(f"Natürlicher Logarithmus von 10: {math.log(10)}")
print(f"Logarithmus zur Basis 10 von 100: {math.log10(100)}")
print(f"Aufrunden von 4.3: {math.ceil(4.3)}")
print(f"Abrunden von 4.7: {math.floor(4.7)}")

# %% [markdown]
# ### 2.4 String (str)
# Strings sind Zeichenketten beliebiger länge. Sie sind eine Sequenz von Unicode-Zeichen und gehören damit eigentlich zu den Datenstrukturen, werden aber oft als primitive Datentypen behandelt.
#
# Strings werden für die Darstellung von Text, Namen, Codes, und anderen zeichenbasierten Informationen verwendet. Sie sind unveränderlich (immutable), d.h. einmal erstellt, kann ihr Inhalt nicht mehr geändert werden.
#
# Strings können durch doppelte `"` oder einzelne `'` Anführungszeichen erzeugt werden. Für mehrzeilige Strings verwendet man dreifache Anführungszeichen `"""` oder `'''`.

# %%
s1 = "Hallo Welt"
s2 = 'Einzelne Anführungszeichen'
s3 = "String mit einem 'Wort' in Anführungszeichen"
s4 = 'String mit einem "Wort" in doppelten Anführungszeichen'

s5 = """Ein String
mit einem Zeilenumbruch.
Und noch einer Zeile."""

s6 = '''Auch mit einfachen
dreifachen Anführungszeichen
geht das.'''

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# %% [markdown]
# Strings können durch das `+`-Zeichen aneinandergehängt (konkateniert) werden. Diese Operation erstellt einen neuen String, da Strings immutable sind.

# %%
# String-Konkatenation
greeting = "Hallo"
name = "Welt"
message = greeting + " " + name
print(message)

# %% [markdown]
# Strings können durch das `*`-Zeichen und einem Integer vervielfältigt werden. Dies ist nützlich, um Muster oder Trennlinien zu erstellen.

# %%
# String-Multiplikation
trennlinie = "-" * 20
rahmen = "+" + "-" * 18 + "+"
print(trennlinie)
print(rahmen)
print("| " + "Python ist toll!".ljust(16) + " |")
print(rahmen)

# %% [markdown]
# Ein wichtiges Konzept bei Strings ist das **Indexing** und **Slicing**. Durch eckige Klammern `[]` können wir einzelne Zeichen oder Teilstrings extrahieren:
#
# - ein bestimmtes Zeichen indexieren mit `[<index>]`
# - den Anfang und den Ende der Teilfolge definieren mit `[<start>:<end>]`
# - den Angang, das Ende und eine Schrittweite definieren mit `[<start>:<end>:<step>]`
#
# In Python beginnen Indizes bei 0, und negative Indizes zählen vom Ende des Strings.

# %%
s = "Hallo Welt"

print(f"{s=}")
print(f"{s[0]=}")        # Erstes Zeichen (Index 0)
print(f"{s[1]=}")        # Zweites Zeichen (Index 1)
print(f"{s[2]=}")        # Drittes Zeichen (Index 2)
print(f"{s[-1]=}")       # Letztes Zeichen
print(f"{s[-2]=}")       # Vorletztes Zeichen
print(f"{s[0:3]=}")      # Zeichen 0 bis 2 (Index 3 ist exklusiv)
print(f"{s[0:-1]=}")     # Vom Anfang bis zum vorletzten Zeichen
print(f"{s[0:]=}")       # Vom Anfang bis zum Ende (komplett)
print(f"{s[:]=}")        # Der komplette String
print(f"{s[::2]=}")      # Jedes zweite Zeichen
print(f"{s[::-1]=}")     # Umgekehrter String (von hinten nach vorne)

# %% [markdown]
# Der `in`-Operator prüft, ob ein Substring in einem String enthalten ist. `not in` prüft auf Nichtvorhandensein.

# %%
# Prüfen, ob ein Substring enthalten ist
print("'l' in 'Hallo Welt':", "l" in "Hallo Welt")
print("'flup' in 'Hallo Welt':", "flup" in "Hallo Welt")
print("'flup' nicht in 'Hallo Welt':", "flup" not in "Hallo Welt")
print("'hallo' in 'Hallo Welt' (Groß-/Kleinschreibung beachten):", "hallo" in "Hallo Welt")
print("'hallo' in 'Hallo Welt' (Groß-/Kleinschreibung ignorieren):", "hallo".lower() in "Hallo Welt".lower())

# %% [markdown]
# Die `len`-Funktion gibt die Länge (Anzahl der Zeichen) eines Strings zurück. Diese Funktion funktioniert auch mit anderen Sequenztypen wie Listen, Tupeln usw.

# %%
# String-Länge
print(f"Länge von 'Hallo Welt': {len('Hallo Welt')}")
print(f"Länge eines leeren Strings: {len('')}")
print(f"Länge eines Strings mit Leerzeichen: {len('   ')}")

# %% [markdown]
# Die String-Klasse bietet eine Vielzahl nützlicher Methoden, die wir durch einen `.` gefolgt vom Methodennamen aufrufen können. Diese erstellen immer einen neuen String und verändern den ursprünglichen String nicht (weil Strings immutable sind).

# %%
s = "  Hallo Welt  "
print(f"Original: '{s}'")
print(f"{s.upper()=}")      # Alle Zeichen in Großbuchstaben
print(f"{s.lower()=}")      # Alle Zeichen in Kleinbuchstaben
print(f"{s.strip()=}")      # Entfernt Leerzeichen am Anfang und Ende
print(f"{s.split()=}")      # Teilt den String an Leerzeichen und erstellt eine Liste

# %% [markdown]
# Hier sind weitere nützliche String-Methoden:

# %%
text = "Python ist eine großartige Programmiersprache!"
print(f"Original: '{text}'")
print(f"Erste Buchstaben groß: {text.title()}")
print(f"Ersten Buchstaben eines Satzes groß: {text.capitalize()}")
print(f"Ersetzt 'großartige' durch 'fantastische': {text.replace('großartige', 'fantastische')}")
print(f"Beginnt mit 'Python'? {text.startswith('Python')}")
print(f"Endet mit '!'? {text.endswith('!')}")
print(f"Position von 'großartige': {text.find('großartige')}")
print(f"Anzahl des Buchstabens 'e': {text.count('e')}")

# String-Formatierung
name = "Alice"
alter = 30
print(f"Formatierung mit f-Strings: {name} ist {alter} Jahre alt.")
print("Formatierung mit .format(): {} ist {} Jahre alt.".format(name, alter))
print("Formatierung mit benannten Parametern: {n} ist {a} Jahre alt.".format(n=name, a=alter))

# %% [markdown]
# ### 2.5 None
# Der `None`-Typ in Python wird verwendet, um die Abwesenheit eines Wertes zu kennzeichnen. Er ist vergleichbar mit `null` in anderen Programmiersprachen.
#
# `None` wird oft als Standardrückgabewert von Funktionen verwendet, die keinen expliziten Wert zurückgeben. Es ist auch nützlich als Initialwert für Variablen, die später einen Wert erhalten sollen.
#
# `None` ist ein Singleton-Objekt, d.h. es gibt nur eine Instanz von `None` im gesamten Programm. Wir können prüfen, ob ein Objekt `None` ist, indem wir den `is`-Operator verwenden.

# %%
def f():
    print("Ich gebe nichts zurück :)")
    
result = f()

print(f"Rückgabewert: {result}")
print(f"Typ des Rückgabewerts: {type(result)}")

# %% [markdown]
# Der `None`-Wert hat einige besondere Eigenschaften:

# %%
# None in Vergleichen
print(f"None == None: {None == None}")    # Gleichheitsprüfung
print(f"None is None: {None is None}")    # Identitätsprüfung (bevorzugt für None)

# None in Wahrheitswerten
print(f"bool(None): {bool(None)}")       # None ist False in Boolean-Kontext

# None als Default-Parameter
def greet(name=None):
    if name is None:
        return "Hallo, Gast!"
    else:
        return f"Hallo, {name}!"

print(greet())             # Verwendet den Default-Wert None
print(greet("Max"))        # Verwendet den übergebenen Namen

# %% [markdown]
# ## 3. Zusammenfassung
#
# In diesem Notebook haben wir die grundlegenden Datentypen in Python kennengelernt:
#
# - **Boolean (bool)**: `True` oder `False`, für logische Operationen
# - **Integer (int)**: Ganze Zahlen ohne Größenbeschränkung
# - **Float (float)**: Dezimalzahlen mit doppelter Präzision
# - **String (str)**: Zeichenketten mit Unicode-Unterstützung
# - **None**: Zur Darstellung der Abwesenheit eines Wertes
#
# Diese Datentypen bilden die Grundlage für komplexere Datenstrukturen und Algorithmen in Python. Das Verständnis dieser Grundlagen ist essenziell für die effektive Programmierung in Python.
#
# In fortgeschrittenen Anwendungen werden wir auch weitere Datentypen wie Listen, Tupel, Dictionaries und Sets kennenlernen, die auf diesen primitiven Typen aufbauen.