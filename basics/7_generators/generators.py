# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: stackfuel
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Iteratoren, Generatoren und lazy evaluation
#
# Eine Liste und ein range-Objekt verhalten sich sehr ähnlich zueinander. Beide können in einer for-Schleife als iterable verwendet werden. Im Kern gibt es aber einen großen Unterschied: Eine Liste muss stets alle Elemente, die in ihr enthalten sind, im Speicher des Computers ablegen. Ein range-Objekt hingegen basiert auf einer klaren Vorschrift, wie das nächste Element gebildet werden soll, und muss daher nur den Start, das Ende und die Step-Size abspeichern.
#

# %%
# Funktion um den Speicherplatzbedarf einer Variable zu ermitteln
from sys import getsizeof

# %%
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r = range(10)

print(type(l))
print(type(r))
print(l)
print(r)

# %%
for e in l:
    print(e, end=" ")
    
print("")

for e in r:
    print(e, end=" ")
 

# %%
print(getsizeof(l))
print(getsizeof(r))

# %% [markdown]
# Wir sehen deutlich, dass die Liste mehr Speicherplatz in Anspruch nimmt als das range-Objekt. Dies liegt daran, dass die Liste jeden einzelnen Wert speichern muss, während das range-Objekt höchstens 3 Zahlen speichert. Dieser Unterschied wird umso deutlicher, je länger die Liste wird.

# %%
print(getsizeof(range(500)))
print(getsizeof(list(range(500))))

# %% [markdown]
# Der Speicherbedarf für das range-Objekt bleibt konstant bei steigender Länge, während die äquivalente Liste drastisch viel mehr Speicher beansprucht.

# %% [markdown]
#
#
#
#
# Es gibt weitere Funktionen in Python, die ebenfalls keine fertige Liste, sondern ein Objekt zurückgeben, das durch eine Vorschrift das nächste Element bilden kann. Map, Zip und Enumerate sind Beispiele für solche Objekte.

# %%
# wir benötigen die deepcopy funktion um die orginal Objekte unangeteastet zu lassen. Mehr dazu später
from copy import deepcopy as copy

m = map(lambda x: x**2, l)
z = zip(l, r)
en = enumerate(range(10, 20))

# wir erstellen zu jedem Objekt eine äquivalente Liste
l_m = list(copy(m))
l_z = list(copy(z))
l_en = list(copy(en))


print(f"{'orginal':<10} | {'list':<10} | {'output':<10}")

print(f"{getsizeof(m):<10} | {getsizeof(l_m):<10} | {l_m}")
print(f"{getsizeof(z):<10} | {getsizeof(l_z):<10} | {l_z}")
print(f"{getsizeof(en):<10} | {getsizeof(l_en):<10} | {l_en}")


# %% [markdown]
# Es ist deutlich zu sehen, dass die Listen versionen mehr Speicher belegen.

# %% [markdown]
# Wollten wir eine Funktion wie die Map-Funktion selbst implementieren, hatten wir bislang nur die Möglichkeit, die Funktion auf alle Elemente der Liste anzuwenden und dann das Resultat als neue Liste zurückzugeben.

# %%
def my_map(function, iterable):
    res = []
    for e in iterable:
        res.append(function(e))
    return res

l = list(range(1000))
getsizeof(my_map(lambda x: x**2, l))


# %% [markdown]
# Durch das Schlüsselwort yield ist es uns möglich, einen Generator zu bauen, der beim Iterieren immer bis zum nächsten yield-Ausdruck läuft und diesen auswertet und zurückgibt. Wird das nächste Element verlangt, macht die Funktion genau an der Stelle weiter, an der sie das letzte Mal aufgehört hat, und läuft, bis sie auf den nächsten yield-Ausdruck stößt.
# Auf diese Weise lassen sich die einzelnen Elemente komfortabel genau dann generieren, wenn sie gebraucht werden. Das verringert den Speicherbedarf enorm.
# Diese Technik nennt sich lazy evaluation.

# %%
def my_map_g(function, iterable):
    for e in iterable:
        yield function(e)
        
getsizeof(my_map_g(lambda x: x**2, l))

# %%
for e in my_map_g(lambda x: x**2, l):
    print(e, end=" ")

# %% [markdown]
# Die `my_map_g`-Funktion gibt als Rückgabe ein Generator-Objekt zurück, welches als Iterator verwendet werden kann. Ein Iterator implementiert die `__next__`-Methode, welche von der built-in Funktion `next` aufgerufen wird, um das Ergebnis des nächsten Iterationsschritts zu erhalten.

# %%
g = my_map_g(lambda x: x*2, range(10))
print(g)

# %% [markdown]
# Führe die nächste Zelle mehrfach aus, um zu sehen, wie die `next`-Funktion immer das nächste Element zurückgibt.

# %%
next(g)

# %% [markdown]
# Wir können ein Generator-Objekt auch durch eine Comprehension, ähnlich der List-Comprehension, erzeugen. Hierfür müssen wir lediglich die umschließenden eckigen Klammern `[]` durch runde Klammern `()` ersetzen.

# %%
lc = [i/2 for i in range(10)]
print(lc)
gc = (i/2 for i in range(10))
print(gc)

# %% [markdown]
# Das Generator-Objekt kann nun ganz normal in einer For-Schleife verwendet werden.

# %%
for e in gc:
    print(e)

# %% [markdown]
# Auch hier lässt sich sehen, dass das Generator-Objekt deutlich Speichereffizienter ist als die entsprechende Liste.

# %%
print(getsizeof(lc))
print(getsizeof(gc))

# %% [markdown]
# Generator-Comprehensions, die direkt einer Funktion übergeben werden brauchen keine extra Klammern, da die Klammern des Funktionsaufrufs bereits ausreichen um den Ausdruck auszuwerten.

# %%
sum(i for i in range(10))

# %% [markdown]
# ## Zusammenfassung
#
# 1. **Speicherbedarf von `range` und Listen**: Der Speicherbedarf für ein `range`-Objekt bleibt konstant, auch wenn die Länge steigt, während eine äquivalente Liste deutlich mehr Speicher benötigt.
#
# 2. **`my_map_g`-Funktion**: Diese Funktion gibt ein Generator-Objekt zurück, das als Iterator verwendet werden kann. Ein Iterator implementiert die `__next__`-Methode, die von der built-in Funktion `next` aufgerufen wird, um das nächste Iterationsergebnis zu erhalten.
#
# 3. **Verwendung von `next`**: Mehrfaches Aufrufen von `next` auf einem Generator-Objekt gibt jeweils das nächste Element zurück.
#
# 4. **Generator-Comprehension**: Ein Generator-Objekt kann ähnlich wie eine List-Comprehension erzeugt werden, indem die eckigen Klammern `[]` durch runde Klammern `()` ersetzt werden.
#
# 5. **Verwendung in For-Schleifen**: Das Generator-Objekt kann in einer For-Schleife wie eine normale Liste verwendet werden.
