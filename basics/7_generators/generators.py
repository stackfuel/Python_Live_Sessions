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
# # Iteratoren, Generatoren und Lazy Evaluation
#
# In Python sind einige Datentypen **iterierbar**, was bedeutet, dass sie durchlaufen werden können, zum Beispiel in einer For-Schleife. Zu diesen iterierbaren Objekten gehören Listen, Tupel, Strings und auch spezielle Objekte wie `range`. Auf den ersten Blick verhalten sich eine Liste und ein `range`-Objekt sehr ähnlich, aber es gibt einen wichtigen Unterschied:
#
# - **Liste**: Enthält alle Elemente und speichert sie im Speicher.
# - **`range`-Objekt**: Enthält nicht alle Elemente direkt, sondern erzeugt sie bei Bedarf.
#
# Dieser Unterschied hat Auswirkungen auf den Speicherbedarf und die Effizienz von Programmen, besonders bei der Arbeit mit großen Datenmengen. In dieser Lektion werden wir uns mit den Konzepten von **Iteratoren**, **Generatoren** und **Lazy Evaluation** beschäftigen und lernen, wie sie uns dabei helfen können, effizientere Programme zu schreiben.

# %% [markdown]
# ## Listen und `range`-Objekte im Vergleich
#
# Beginnen wir mit einem einfachen Beispiel, um den Unterschied zwischen Listen und `range`-Objekten zu verstehen.

# %%
# Funktion, um den Speicherplatzbedarf einer Variable zu ermitteln
from sys import getsizeof

# Erstellen einer Liste und eines range-Objekts
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r = range(10)

# Ausgabe der Typen und Inhalte
print("Typ von l:", type(l))
print("Typ von r:", type(r))
print("Inhalt von l:", l)
print("Inhalt von r:", r)

# %% [markdown]
# Wir sehen, dass `l` eine Liste ist, die die Zahlen von 0 bis 9 enthält, während `r` ein `range`-Objekt ist, das die Zahlen von 0 bis 9 repräsentiert. Beim Ausgeben des `range`-Objekts sehen wir nur die Repräsentation `range(0, 10)` und nicht die einzelnen Zahlen.
#
# Obwohl beide Objekte ähnlich aussehen und verwendet werden können, unterscheiden sie sich in der Art, wie sie die Daten speichern.

# %%
# Iteration über die Liste
print("Iteration über die Liste l:")
for e in l:
    print(e, end=" ")
print("\n")

# Iteration über das range-Objekt
print("Iteration über das range-Objekt r:")
for e in r:
    print(e, end=" ")
print("\n")

# %% [markdown]
# Beide Objekte können in einer For-Schleife durchlaufen werden, und die Ausgabe ist identisch.

# %%
# Speicherbedarf vergleichen
print("Größe der Liste l:", getsizeof(l), "Bytes")
print("Größe des range-Objekts r:", getsizeof(r), "Bytes")

# %% [markdown]
# Die Liste `l` benötigt mehr Speicher als das `range`-Objekt `r`. Dies liegt daran, dass die Liste alle Elemente im Speicher hält, während das `range`-Objekt nur Start-, Endwert und Schrittweite speichern muss.

# %% [markdown]
# Schauen wir uns an, wie sich der Speicherbedarf ändert, wenn wir die Länge der iterierbaren Objekte erhöhen.

# %%
large_range = range(1000000)
large_list = list(large_range)

print("Größe des range-Objekts mit 1.000.000 Elementen:", getsizeof(large_range), "Bytes")
print("Größe der Liste mit 1.000.000 Elementen:", getsizeof(large_list), "Bytes")

# %% [markdown]
# **Erläuterung:**
#
# - Der Speicherbedarf des `range`-Objekts bleibt nahezu konstant, selbst bei einer Million Elemente.
# - Die Liste benötigt jedoch über 8 MB Speicher, um alle Elemente zu speichern.
#
# **Hinweis:**
#
# Die Funktion `getsizeof` misst nur die Größe des Objekts selbst und nicht den Speicherbedarf der einzelnen Elemente. Dennoch verdeutlicht dies den Unterschied zwischen den beiden Objekttypen.

# %% [markdown]
# ## Iterables und Iteratoren
#
# - **Iterables**: Ein Iterable ist ein Objekt, das eine `__iter__()`-Methode implementiert, die einen Iterator zurückgibt. Iterables sind Objekte, über die man in einer Schleife iterieren kann. Beispiele für eingebaute Iterable-Objekte in Python sind Listen, Tupel, Strings und Mengen.
#
# - **Iteratoren**: Ein Iterator ist ein Objekt, das die Methoden `__iter__()` und `__next__()` implementiert. Die Methode `__next__()` gibt das nächste Element des Iterators zurück und wirft eine `StopIteration`-Exception, wenn keine weiteren Elemente vorhanden sind.
#
# **Hinweis:** Dunder-Methoden (Double-underscore-Methoden) wie `__next__()` oder `__iter__()` werden in Python meist nicht direkt aufgerufen. Stattdessen greift man auf diese spezielle Funktionalität durch dafür vorgesehene Hilfsfunktionen oder Sprachkonstrukte zu. Beispielsweise verwendet man die eingebaute `next()`-Funktion, um das nächste Element von einem Iterator zu erhalten, anstatt direkt `iterator.__next__()` aufzurufen. Dies fördert klareren und lesbareren Code und nutzt die volle Flexibilität, die Python bietet.
#
# Bei der Iteration über ein Iterable in einer Schleife wird implizit ein Iterator erstellt, um die Iteration durchzuführen. Hier ist ein einfaches Beispiel:

# %%
# Einfache Liste als Iterable
liste = [1, 2, 3]

# Erstellen eines Iterators aus dem Iterable
iterator = iter(liste)

# Abrufen von Elementen mit einem Iterator
print(next(iterator))  # Gibt 1 zurück
print(next(iterator))  # Gibt 2 zurück
print(next(iterator))  # Gibt 3 zurück
#print(next(iterator))  # Wirft eine StopIteration Exeption

# %% [markdown]
# ## Funktionen, die Iteratoren zurückgeben
#
# Mehrere eingebaute Funktionen in Python geben Iteratoren zurück. Beispiele sind `map`, `zip` und `enumerate`.

# %%
l = [1, 2, 3, 4, 5]

# Verwenden von map
m = map(lambda x: x**2, l)

print("Typ von m:", type(m))
print(next(m)) # Die erste Zahl außerhalb der for-Schleife

for item in m:
    print(item, end=" ")
print("\n")

# %%
# Verwenden von zip
z = zip(l, l)

print("Typ von z:", type(z))
for item in z:
    print(item, end=" ")
print("\n")

# %%
# Verwenden von enumerate
e = enumerate(l)

print("Typ von e:", type(e))
for index, value in e:
    print(f"Index {index}: Wert {value}")


# %% [markdown]
# Die Iteratoren generieren ihre Elemente erst bei der Iteration. Dies spart Speicher, da nicht alle Elemente im Voraus berechnet werden.

# %% [markdown]
# ## Eigene Iteratoren mit Generatoren erstellen
#
# Wenn wir Funktionen schreiben, die große Datenmengen verarbeiten, ist es hilfreich, wenn sie Iteratoren zurückgeben. Dies können wir mit Generatoren erreichen.

# %% [markdown]
# ### Generator-Funktionen mit `yield`
#
# Durch das Schlüsselwort `yield` können wir Funktionen schreiben, die bei jedem Aufruf von `next()` ein neues Element liefern.

# %%
def my_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = my_generator(5)
print("Typ von gen:", type(gen))

for num in gen:
    print(num)

# %% [markdown]
# **Erläuterung:**
#
# - Die Funktion `my_generator` ist ein Generator. Bei jedem `yield` wird der aktuelle Wert von `i` zurückgegeben.
# - Beim nächsten Aufruf wird die Ausführung nach dem `yield` fortgesetzt.

# %% [markdown]
# ### Vergleich von Funktionen mit und ohne Generatoren

# %% [markdown]
# **Funktion, die eine Liste zurückgibt:**

# %%
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

squares = squares_list(20)
print("Quadratzahlen als Liste:", squares)
print("Größe der Liste:", getsizeof(squares), "Bytes")

# %% [markdown]
# **Funktion, die einen Generator zurückgibt:**

# %%
def squares_generator(n):
    for i in range(n):
        yield i**2

squares_gen = squares_generator(20)
print("Quadratzahlen als Generator:", squares_gen)
print("Größe des Generators:", getsizeof(squares_gen), "Bytes")

print("Quadratzahlen aus Generator:")
for num in squares_gen:
    print(num, end=" ")
print()


# %% [markdown]
# **Erläuterung:**
#
# - Die Listenfunktion `squares_list` erstellt eine Liste aller Quadratzahlen und speichert sie im Speicher.
# - Die Generatorfunktion `squares_generator` liefert die Quadratzahlen bei Bedarf und benötigt weniger Speicher.

# %% [markdown]
# ### Beispiele map, zip, enumeratre Implementierung

# %%
def my_enumerate(iterable, start=0):
    index = start
    it = iter(iterable)
    while True:
        try:
            yield (index, next(it))
        except StopIteration:
            return
        index += 1


# %%

# Beispiel für `my_enumerate`
colors = ['red', 'green', 'blue']

enumerated_colors = my_enumerate(colors, start=1)

for index, color in enumerated_colors:
    print(index, color)


# %%
def my_zip(*iterables):
    iterators = [iter(i) for i in iterables]
    while True:
        try:
            result = [next(i) for i in iterators]
            yield tuple(result)
        except StopIteration:
            return



# %%
# Beispiel für `my_zip`
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

zipped_result = my_zip(list1, list2, list3)

for item in zipped_result:
    print(item)


# %%
def my_map(f, *iteraples):
    for args in my_zip(*iteraples):
        yield f(*args)


# %%
# Beispiel für `my_map`
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]

mapped_result = my_map(add, list1, list2)

for item in mapped_result:
    print(item)

# %% [markdown]
# ### Generator Expressions
#
# Ähnlich zu List Comprehensions können wir Generator Expressions verwenden, um Generatoren zu erstellen.

# %%
# List Comprehension
lc = [i**2 for i in range(20)]
print("List Comprehension:", lc)
print("Größe von lc:", getsizeof(lc), "Bytes")

# Generator Expression
ge = (i**2 for i in range(20))
print("Generator Expression:", ge)
print("Größe von ge:", getsizeof(ge), "Bytes")

print("Quadratzahlen aus Generator Expression:")
for num in ge:
    print(num, end=" ")
print()


# %% [markdown]
# **Erläuterung:**
#
# - Die List Comprehension erstellt sofort eine Liste mit allen Elementen.
# - Die Generator Expression erzeugt die Elemente bei Bedarf und verbraucht weniger Speicher.
#
#
#
#

# %% [markdown]
# ## Einsatz von Generatoren für Lazy Evaluation
#
# **Lazy Evaluation** bedeutet, dass Berechnungen erst dann durchgeführt werden, wenn sie tatsächlich benötigt werden. Generatoren ermöglichen es uns, dieses Konzept in Python zu nutzen.

# %% [markdown]
# **Beispiel mit unendlicher Folge von Fibonacci-Zahlen:**
#
# Fibonacci-Zahlen sind eine berühmte Zahlenfolge, die aus der Summe der beiden vorherigen Zahlen gebildet wird. Die Folge beginnt mit 0 und 1, und jedes nachfolgende Element ist die Summe der vorhergehenden beiden. 
#
# $$
# F(n) = 
# \begin{cases} 
# 0, & \text{wenn } n = 0 \\
# 1, & \text{wenn } n = 1 \\
# F(n-1) + F(n-2), & \text{wenn } n > 1
# \end{cases}
# $$
#
# Dabei steht $ F(n) $ für die $ n $-te Fibonacci-Zahl.
#
#
#
# | $n$ | $F(n)$ |
# |-----|--------|
# |0    | 0      |
# |1    | 1      |
# |2    | 1      |
# |3    | 2      |
# |4    | 3      |
# |5    | 5      |
# |6    | 8      |
# |7    |13      |
#
# Durch den Einsatz von Lazy Evaluation mit Generatoren können wir diese unendliche Folge generieren, ohne unendlich viel Speicher zu benötigen. Wir können bei Bedarf jederzeit das nächste Element erzeugen.

# %%
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

# Ausgabe der ersten 20 Fibonacci-Zahlen
print(f"{'n':>3} | {'F(n)':<5}")
print("-"*11)

for n, f in zip(range(20), fib_gen):
    print(f"{n:>3} | {f:>5}")

# %% [markdown]
# **Erläuterung:**
#
# - Die Funktion `fibonacci` erzeugt eine unendliche Zahlenfolge.
# - Da die Zahlen bei Bedarf generiert werden, können wir theoretisch unendlich viele Elemente haben, ohne den Speicher zu überlasten.

# %% [markdown]
# ## Nachteile von Generatoren gegenüber Listen
#
# Generatoren sind speicher- und zeiteffizient, haben aber Nachteile gegenüber Listen:
#
# - **Nicht indexierbar**: Kein direkter Zugriff auf Elemente per Index.
# - **Einmalige Iteration**: Nach vollständiger Durchlaufung erschöpft.
# - **Unbekannte Länge**: `len()` funktioniert nicht, da Länge nicht definiert.
# - **Kein zufälliger Zugriff**: Keine Möglichkeit, Elemente zu überspringen oder zurückzugehen.
# - **Erschwertes Debugging**: Zustand schwer einsehbar.
#
# **Beispiele:**

# %%
# Nicht indexierbar und Einmalige Iteration
try:
    my_generator = (x for x in range(5))
    print("Indexzugriff:", my_generator[2])  # Fehler
except TypeError as e:
    print("Fehler:", e)

print()


# Einmalige Iteration
gen = (x for x in range(3))
print("Erster Durchlauf:")
for value in gen:
    print(value)
print("Zweiter Durchlauf:")
for value in gen:
    print(value)  # Keine Ausgabe

print()

# Unbekannte Länge
try:
    gen = (x for x in range(5))
    print(len(gen))  # Fehler
except TypeError as e:
    print("Fehler:", e)


print()

# Kein zufälliger Zugriff
gen = (x for x in range(5))
next(gen)
next(gen)
try:
    print(gen[0])  # Fehler
except TypeError as e:
    print("Fehler:", e)

# %% [markdown]
# ## Zusammenfassung
#
# 1. **Speicherbedarf von `range` und Listen**: `range`-Objekte speichern nur Start, Ende und Schrittweite und verbrauchen konstanten Speicher, während Listen alle Elemente im Speicher halten.
#
# 2. **Iteratoren**: Objekte wie `map`, `zip` und `enumerate` geben Iteratoren zurück, die ihre Elemente bei Bedarf generieren.
#
# 3. **Generatoren**: Mit dem `yield`-Schlüsselwort können wir Generatoren erstellen, die Iteratoren sind und Lazy Evaluation ermöglichen.
#
# 4. **Generator Expressions**: Ähnlich zu List Comprehensions, aber sie erzeugen Elemente bei Bedarf.
#
# 5. **Lazy Evaluation**: Berechnungen werden erst durchgeführt, wenn sie benötigt werden, was Speicher und Rechenleistung spart.
