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

# %%
import this

# %%
# grundlegende Datentypen
boolean = True              # oder False
integer = 42                # oder -1, -45, 156, 928374528138495
float   = 3.14              # oder -3.14, 0.0, 928374528138495.0
string  = "Hallo Welt!"     # oder 'Hallo Welt!', "🚀", 'erste Zeile\nzweite Zeile', """mehrzeiliger String"""
none    = None

print(boolean, integer, float, string, none, sep="\n")

# %% [markdown]
# # Tuple

# %% [markdown]
# ## Was ist ein Tuple
#
# - Ein Tuple ist eine unveränderliche, geordnete Sammlung von Elementen.
# - Ein Tuple wird durch runde Klammern `(` `)` definiert und die Elemente werden durch Kommas `,` getrennt.
# - Ein Tuple kann Elemente unterschiedlicher Datentypen enthalten.
# - Tuple haben viele Gemeinsamkeiten mit Strings.
#

# %%

tuple_ = (boolean, integer, float, string, none)
print(tuple_)

# %%
# Tuple sind 'itterables', das bedeutet wir können sie als Basis für for Schleifen verwenden.

for element in tuple_:
    print(element)

# %%
# tuple können auf mehrere Arten erstellt werden
t1 = tuple(range(5))
print(t1)

t2 = (4, 5, 6)
print(t2)

t3 = 7, 8, 9
print(t3)


# %%
fruits = ('apple', 'banana', 'cherry', 'apple', 'orange', 'banana', 'apple')

# %%
# Mit der len Funktion können wir die Anzahl der Elemente in einem Tuple ermitteln.

print(len(fruits))

# %%
# Mit dem Keyword `in` lässt sich prüfen ob ein Element in einem Tuple enthalten ist.

print('apple' in fruits)
print('pear' in fruits)

# %% [markdown]
# #Jedem Element eines Tuples wird ein Index entsprechend seiner Position zugeordnet.
# Die Zählung beginnt bei 0. Das erste Element eines Tuples hat also stehts den Index 0.
# Um auf die Element über ihren Index zuzugreifen, schreiben wir 
# - `fruits[index]`
# - `fruits[start:stop]`
# - `fruits[start:stop:schrittweite]`
#

# %%
print(fruits)

print(fruits[0])
print(fruits[4])
print(fruits[1:3])
print(fruits[1:6:2])

# %%
# Man kann für den Index auch negative Werte verwenden
# -1 entspricht dem letzten Element, -2 dem vorletzten, usw.

print(fruits)

print(fruits[-1])
print(fruits[-2])
print(fruits[-3:-1])
print(fruits[-3:])

# %%
# Auch für die Schrittweite können negative Werte verwendet werden.
# In diesem Fall wird das Tupel rückwärts durchlaufen.
# Der Startwert muss dabei größer als der Stopwert sein.

print(fruits)

print(fruits[::-1])
print(fruits[::-2])
print(fruits[5:1:-1])
print(fruits[5:1:-2])

# %%
# Tuple haben zwei Methoden

# Verwenden der count()-Methode, um die Anzahl der Vorkommen von 'apple' zu zählen

apple_count = fruits.count('apple')
print(apple_count)

# %%
# Verwenden der index()-Methode, um den Index des ersten Vorkommens von 'banana' zu finden
fruits.index('apple', 2)

# %%
value = "apple"

start = 0
for _ in range(fruits.count(value)):
    idx = fruits.index(value, start)
    print(idx)
    start = idx+1
    

# %%
# tuple sind unveränderlich (immutable), d.h. sie können nach der Erstellung nicht mehr verändert werden.

fruits[3] = "peach"

# %% [markdown]
# # List

# %%
# Was ist eine List?

# Eine List ist eine veränderliche, geordnete Sammlung von Elementen.
# Eine List wird durch eckige Klammern [] definiert und die Elemente werden durch Kommas getrennt.
# Eine List kann Elemente unterschiedlicher Datentypen enthalten.

names = ["Alice", "Bob", "Charlie", "Bob", "David", "Eve"]

# Listen unterstützen weitestgehend die selben Funktionalitäten wie Tuple

print(names)

print(names[1:3])
print(len(names))
print("Alice" in names)
print("Mallory" in names)

for name in names:
    print(name)



# %%
print(names.count("Bob"))
print(names.index("Bob"))

# %%
# Listen sind veränderlich (mutable), d.h. sie können nach der Erstellung verändert werden.
print(names)
names[3] = "Daniel"
print(names)


# %%
# Mit der append()-Methode können wir ein Element am Ende einer Liste hinzufügen.
names.append("Eva")
print(names)

# %%
# Mit der extend()-Methode können wir eine Liste an eine andere Liste anhängen.
names.extend(["Frank", "Grace"])
# names = names + ["Frank", "Grace"] # tut das gleiche
print(names)

# %%
# Zwei Listen können auch mit dem + Operator zusammengefügt werden.
# Dabei wird eine neue Liste erstellt und die beiden Listen werden nicht verändert.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

# %%
# Mit der insert()-Methode können wir ein Element an einer bestimmten Position in einer Liste einfügen.

print(names)
names.insert(3, "Dennis")
print(names)

# %%
# Mit der pop()-Methode können wir ein Element an einer bestimmten Position aus einer Liste entfernen.

print(names)
poped_element = names.pop(3)
print(names)
print(poped_element)

# %%
# Gibt man pop keinen Index an, wird das letzte Element entfernt.
# Das entfernte Element wird dabei zurückgegeben.
# Zusammen mit append lässt sich die Liste wie ein Stack verwenden.

stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())



# %%
stack

# %%
# Wie bei Tuplen kommen wir mit der Methode index an den Index des ersten Vorkommens eines Elements.
# Mit der remove()-Methode können wir das erste Vorkommen eines Elements aus einer Liste entfernen.

print(names)
if "Dennis" in names:
    names.remove("Dennis")
else:
    print("Dennis not found")
print(names)

# %%
l = [1, 2, 2, 2, 3]

for _ in range(l.count(2)):
    l.remove(2)

l

# %%
# Mit der clear()-Methode können wir alle Elemente aus einer Liste entfernen.

l = [1, 2, 3, 4, 5]
print(l)
l.clear()
print(l)

# %%
# Mit der reverse()-Methode können wir die Reihenfolge der Elemente in einer Liste umkehren.

l = [1, 2, 3, 4, 5]
print(l)
l.reverse()
print(l)

# %%
list(reversed(l))

# %%
l

# %%
# Mit der sort()-Methode können wir die Elemente einer Liste sortieren.

l = [5, 3, 4, 1, 2]
# print(l)
# l.sort()
# print(l)

# %%
print(sorted(l))
print(l)

# %% [markdown]
# # Set

# %%
# Ein Set ist eine ungeordnete Sammlung von Elementen ohne Duplikate.
# Ein Set wird durch geschweifte Klammern {} definiert und die Elemente werden durch Kommas getrennt.
# Ein Set kann Elemente unterschiedlicher Datentypen enthalten. Dabei können nur unveränderliche Datentypen wie
# Integer, Float, String, Tuple, Boolean und None usw. enthalten sein.

s = {1, 2, 3, 4, 5, (1, 2, 3)}
print(s)

# %%
string_ = "strig"

hash(string_)

# %%
6.8 in s

# %%
s = {"Hallo Welt", 6.8, (4, 5, 6), True, None}
s

# %%
# Ein Set ist ein 'itterable', das bedeutet wir können es als Basis für for Schleifen verwenden.
# Die Reihenfolge der Elemente in einem Set ist nicht definiert.
# Ein Set hat keine Duplikate

s = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}

print(s)
for e in s:
    print(e)
    


# %%
# Ein Set hat keine Indizes, daher können wir nicht auf Elemente über ihren Index zugreifen.

s[3]

# %%
# Sets unterstützen die üblichen Mengenoperatoren aus der Mengenlehre.
# Mit den Methoden union(), intersection() und difference() können wir die Vereinigung, den Schnitt und die Differenz
# von zwei Sets berechnen.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

# %%
# Die gleichen Operatoren können auch mit den Operatoren |, &, - durchgeführt werden.

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)

# %%
# Mit der add()-Methode können wir ein Element zu einem Set hinzufügen.

s = {1, 2, 3, 4, 5}
print(s)
s.add(6)
print(s)

# %%
# Mit der remove()-Methode können wir ein Element aus einem Set entfernen.

s = {1, 2, 3, 4, 5}
print(s)
s.remove(3)
print(s)

# %%
# Mit dem Schlüsselwort `in` können wir prüfen, ob ein Element in einem Set enthalten ist.
# `in` ist in Sets effizienter als in Listen.

s = {1, 2, 3, 4, 5}
print(3 in s) 

# %% [markdown]
# # Dictionary

# %%
# Ein Dictionary ist eine ungeordnete Sammlung von Elementen, die durch Schlüssel-Wert-Paare definiert sind.
# Ein Dictionary wird durch geschweifte Klammern {} definiert und die Schlüssel-Wert-Paare werden durch Kommas getrennt.
# Ein Dictionary kann Elemente unterschiedlicher Datentypen enthalten.

d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": None}
print(d)

# %%
# Ein Dictionary ist ein 'itterable', das bedeutet wir können es als Basis für for Schleifen verwenden.
# Die Reihenfolge der Elemente in einem Dictionary ist nicht definiert.

for key in d:
    print(key, d[key])

# %%
# Mit dem Schlüsselwort `in` können wir prüfen, ob ein Schlüssel in einem Dictionary enthalten ist.

print("a" in d)
print("z" in d)

# %%
from collections import defaultdict, Counter


d = defaultdict(int)


Counter("Hallo Welt")




# %%
# Mit der Methode get() können wir den Wert eines Schlüssels abrufen.

print(d.get("a"))
print(d.get("z", 0))

# Alternativ können wir auch direkt auf den Wert eines Schlüssels zug
# Im gegensasatz zu get() wirft diese Methode einen KeyError, wenn der Schlüssel nicht im Dictionary enthalten ist.

print(d["a"])
print(d["f"])

# %%
# Mit der Methode pop() können wir ein Schlüssel-Wert-Paar aus einem Dictionary entfernen.
# Die Methode gibt den Wert des entfernten Schlüssels zurück.

d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(d)
var = d.pop("a")

print(d)
print(var)

# %%
d.pop("a")

# %%
# Die Schlüssel eines Dictionarys müssen eindeutig sein.

d = {"a": 1, "b": 2, "a": 2}
print(d)


# %%
# Zwei dictionarys können mit der update()-Methode zusammengeführt werden.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 4, "d": 5, "e": 6}

print(d1)
print(d2)

d1.update(d2)
print(d1)

# %%
# Alternativ können zwei dictionarys auch mit dem | Operator zusammengeführt werden.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 4, "d": 5, "e": 6}

print(d1)
print(d2)

d3 = d1 | d2
print(d3)

# %%
# Mit der keys()-Methode können wir eine Liste aller Schlüssel eines Dictionarys abrufen.

d = {"a": 1, "b": 2, "c": 3}
print(list(d.keys()))

# Mit der values()-Methode können wir eine Liste aller Werte eines Dictionarys abrufen.

print(d.values())

# %%
# Mit der items()-Methode können wir eine Liste aller Schlüssel-Wert-Paare eines Dictionarys abrufen.

print(d.items())

# Wir können item() benutzen um über alle Schlüssel-Wert-Paare eines Dictionarys zu iterieren.

for key, value in d.items():
    print(key, value)

# %%
# Wir können die keys nutzen um auf values zuzugreifen oder diese zu verändern

d = {"a": 1, "b": 2, "c": 3}
print(d)

d["b"] = d["b"]**2

print(d)

# %%
# Die keys eines Dictionarys müssen unveränderlich sein.

d = {"a": 1, "b": 2, "c": 3}
print(d)

#d[[1, 2, 3]] = 4

d[(1, 2, 3)] = 4

print(d)

# %%
# Praktische Anwendungen

# Drictionarys werden verwendet um die globalen Variablen in Python zu speichern.
# Die Funktion globals() gibt ein Dictionary zurück, das alle globalen Variablen und deren
# Werte enthält.

print(globals())


# %%
def f(a, b):
    print(locals())
    
f(2, 3)

# %%
# Ein Dictionary kann auch verwendet werden, um eine Konfigurationsdatei zu speichern.

config = {
    "username": "admin",
    "password": "admin",
    "host": "localhost",
    "port": 3306,
    "database": "test"
}

print(config)
