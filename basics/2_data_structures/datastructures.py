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
# # Python Datenstrukturen: Listen, Tupel, Mengen und Dictionaries
#
# In Python werden Datenstrukturen verwendet, um Sammlungen von Daten zu speichern, auf die auf vielfältige Weise zugegriffen und manipuliert werden kann. Die eingebauten Datenstrukturen in Python umfassen **Listen**, **Tupel**, **Mengen** und **Dictionaries**. Jede dieser Datenstrukturen hat einzigartige Eigenschaften und Verwendungszwecke.
#
# In dieser Lektion werden wir diese Datenstrukturen erkunden, ihre Eigenschaften verstehen und lernen, wie man sie effektiv in der Python-Programmierung einsetzt.
#
# **Überblick:**
#
# - Einführung in grundlegende Datentypen
# - Verständnis von Tupeln
# - Arbeiten mit Listen
# - Erkundung von Mengen
# - Verwendung von Dictionaries
# - Zusammenfassung

# %% [markdown]
# ## Grundlegende Datentypen in Python
#
# Bevor wir uns mit komplexen Datenstrukturen befassen, lassen Sie uns kurz einige der grundlegenden Datentypen in Python überprüfen:
#
# - **Boolean**: Repräsentiert `True` oder `False`.
# - **Integer**: Ganze Zahlen, positiv oder negativ, ohne Dezimalstellen.
# - **Float**: Zahlen mit Dezimalstellen.
# - **String**: Geordnete Sequenz von Zeichen, eingeschlossen in einfache, doppelte oder dreifache Anführungszeichen.
# - **None**: Repräsentiert das Fehlen eines Wertes.

# %%
# Beispiele für grundlegende Datentypen
boolesche_variable = True                # Boolean
integer_variable = 42                    # Integer
float_variable = 3.14                    # Float
string_variable = "Hallo, Welt!"         # String
keine_variable = None                    # NoneType

print("Boolean:", boolesche_variable)
print("Integer:", integer_variable)
print("Float:", float_variable)
print("String:", string_variable)
print("NoneType:", keine_variable)

# %% [markdown]
# ## Tupel
#
# ### Was ist ein Tupel?
#
# Ein **Tupel** ist eine **unveränderliche**, **geordnete** Sequenz von Elementen. Tupel werden verwendet, um mehrere Elemente in einer einzelnen Variablen zu speichern und werden durch Klammern `(` `)` definiert, wobei die Elemente durch Kommas `,` getrennt sind.
#
# **Eigenschaften von Tupeln:**
#
# - **Geordnet**: Elemente haben eine definierte Reihenfolge und können über Indizes angesprochen werden.
# - **Unveränderlich**: Elemente können nach der Erstellung des Tupels nicht geändert werden.
# - **Erlaubt Duplikate**: Tupel können doppelte Elemente enthalten.
# - **Kann gemischte Datentypen enthalten**: Elemente können unterschiedliche Datentypen haben.
#
# Tupel sind Listen ähnlich, aber der Hauptunterschied besteht darin, dass Tupel unveränderlich sind, während Listen veränderlich sind.

# %%
# Erstellen eines Tupels mit verschiedenen Datentypen
mein_tupel = (boolesche_variable, integer_variable, float_variable, string_variable, keine_variable)
print("Mein Tupel:", mein_tupel)

# %% [markdown]
# ### Erstellen von Tupeln
#
# Tupel können auf verschiedene Weise erstellt werden:

# %%
# Mit Klammern
tupel1 = (1, 2, 3)
print("Tupel1:", tupel1)

# Ohne Klammern (Tupel-Packing)
tupel2 = 4, 5, 6
print("Tupel2:", tupel2)

# Mit dem tuple()-Konstruktor
tupel3 = tuple([7, 8, 9])
print("Tupel3:", tupel3)

# Erstellen eines leeren Tupels
leeres_tupel = ()
print("Leeres Tupel:", leeres_tupel)

# Erstellen eines Einzel-Element-Tupels (beachten Sie das Komma)
einzelnes_element_tupel = (42,)
print("Einzelnes Element Tupel:", einzelnes_element_tupel)

# %% [markdown]
# ### Zugriff auf Tupel-Elemente
#
# Sie können auf Tupel-Elemente durch Indizierung und Slicing zugreifen, ähnlich wie bei Listen.

# %%
früchte = ('apfel', 'banane', 'kirsche', 'apfel', 'orange', 'banane', 'apfel')

# Zugriff auf Elemente über den Index
print("Erstes Element:", früchte[0])
print("Drittes Element:", früchte[2])

# Zugriff auf Elemente mit negativen Indizes
print("Letztes Element:", früchte[-1])
print("Vorletztes Element:", früchte[-2])

# Tupel schneiden
print("Elemente von Index 1 bis 3:", früchte[1:4])
print("Jedes zweite Element:", früchte[::2])
print("Umgekehrtes Tupel:", früchte[::-1])

# %% [markdown]
# ### Tupel-Methoden
#
# Tupel haben nur zwei eingebaute Methoden:
#
# - **count()**: Gibt die Anzahl der Vorkommen eines bestimmten Wertes im Tupel zurück.
# - **index()**: Sucht im Tupel nach einem bestimmten Wert und gibt die Position des ersten Vorkommens zurück.

# %%
# Verwendung von count()
apfel_anzahl = früchte.count('apfel')
print("Anzahl der 'apfel' Vorkommen:", apfel_anzahl)

# Verwendung von index()
erste_banane_index = früchte.index('banane')
print("Erstes Auftreten von 'banane' an Index:", erste_banane_index)

# Verwendung von index() mit Start- und Endparametern
zweiter_apfel_index = früchte.index('apfel', erste_banane_index + 1)
print("Zweites Auftreten von 'apfel' an Index:", zweiter_apfel_index)

# %% [markdown]
# ### Unveränderlichkeit von Tupeln
#
# Tupel sind unveränderlich, was bedeutet, dass nach der Erstellung eines Tupels seine Elemente nicht geändert, hinzugefügt oder entfernt werden können. Der Versuch, ein Tupel zu ändern, führt zu einem `TypeError`.

# %%
# Versuch, ein Tupel-Element zu ändern (dies führt zu einem Fehler)
try:
    früchte[0] = 'birne'
except TypeError as e:
    print("Fehler:", e)

# %% [markdown]
# ### Wann man Tupel verwendet
#
# Tupel sind nützlich, wenn Sie sicherstellen möchten, dass die Daten nicht geändert werden können. Sie werden oft verwendet, um feste Sammlungen von Elementen zu repräsentieren, wie Koordinaten, Datenbankeinträge oder beliebige Daten, die konstant bleiben sollen.

# %% [markdown]
# ## Listen
#
# ### Was ist eine Liste?
#
# Eine **Liste** ist eine **veränderliche**, **geordnete** Sequenz von Elementen. Listen sind einer der vielseitigsten Datentypen in Python und ermöglichen das Hinzufügen, Entfernen oder Ändern von Elementen.
#
# **Eigenschaften von Listen:**
#
# - **Geordnet**: Elemente haben eine definierte Reihenfolge und können über Indizes angesprochen werden.
# - **Veränderlich**: Elemente können nach der Erstellung der Liste geändert werden.
# - **Erlaubt Duplikate**: Listen können doppelte Elemente enthalten.
# - **Kann gemischte Datentypen enthalten**: Elemente können unterschiedliche Datentypen haben.

# %%
# Erstellen einer Liste mit verschiedenen Datentypen
meine_liste = [boolesche_variable, integer_variable, float_variable, string_variable, keine_variable]
print("Meine Liste:", meine_liste)

# %% [markdown]
# ### Zugriff auf Listenelemente
#
# Ähnlich wie bei Tupeln können Sie auf Elemente in einer Liste mit Indizes und Slicing zugreifen.

# %%
namen = ["Alice", "Bob", "Charlie", "Bob", "David", "Eve"]

# Zugriff auf Elemente über den Index
print("Erster Name:", namen[0])
print("Dritter Name:", namen[2])

# Zugriff auf Elemente mit negativen Indizes
print("Letzter Name:", namen[-1])
print("Vorletzter Name:", namen[-2])

# Listen schneiden
print("Namen von Index 1 bis 3:", namen[1:4])
print("Jeder zweite Name:", namen[::2])
print("Umgekehrte Liste:", namen[::-1])

# %% [markdown]
# ### Listen modifizieren
#
# Listen sind veränderlich, was bedeutet, dass Sie sie nach der Erstellung ändern können.

# %%
# Ändern eines Elements
print("Ursprüngliche Liste:", namen)
namen[3] = "Daniel"
print("Nach Änderung:", namen)

# %% [markdown]
# ### Listenmethoden
#
# Listen haben viele eingebaute Methoden, die es ermöglichen, sie zu manipulieren:
#
# - **append()**: Fügt ein Element am Ende der Liste hinzu.
# - **extend()**: Fügt alle Elemente eines Iterables am Ende der Liste hinzu.
# - **insert()**: Fügt ein Element an einer bestimmten Position ein.
# - **remove()**: Entfernt das erste Vorkommen eines bestimmten Elements.
# - **pop()**: Entfernt und gibt das Element an der angegebenen Position zurück.
# - **clear()**: Entfernt alle Elemente aus der Liste.
# - **index()**: Gibt den Index des ersten Vorkommens eines bestimmten Elements zurück.
# - **count()**: Gibt die Anzahl der Vorkommen eines bestimmten Elements zurück.
# - **sort()**: Sortiert die Liste.
# - **reverse()**: Kehrt die Reihenfolge der Liste um.

# %%
# append()
namen.append("Frank")
print("Nach append('Frank'):", namen)

# extend()
namen.extend(["Grace", "Henry"])
print("Nach extend(['Grace', 'Henry']):", namen)

# insert()
namen.insert(2, "Ivy")
print("Nach insert('Ivy') an Index 2:", namen)

# remove()
namen.remove("Bob")
print("Nach remove('Bob'):", namen)

# pop()
entfernter_name = namen.pop(3)
print("Nach pop(3):", namen)
print("Entfernter Name:", entfernter_name)

# clear()
namen.clear()
print("Nach clear():", namen)

# Liste für weitere Beispiele neu befüllen
namen = ["Alice", "Bob", "Charlie", "David", "Eve"]

# index()
index_von_charlie = namen.index("Charlie")
print("Index von 'Charlie':", index_von_charlie)

# count()
anzahl_von_bob = namen.count("Bob")
print("Anzahl von 'Bob':", anzahl_von_bob)

# sort()
zahlen = [3, 1, 4, 1, 5, 9, 2, 6]
print("Ursprüngliche Zahlen:", zahlen)
zahlen.sort()
print("Sortierte Zahlen:", zahlen)

# reverse()
zahlen.reverse()
print("Umgekehrte Zahlen:", zahlen)

# %% [markdown]
# ### Listenoperationen
#
# Listen unterstützen Operationen wie Verkettung und Wiederholung.

# %%
# Verkettung mit +
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
verkettete_liste = liste1 + liste2
print("Verkettete Liste:", verkettete_liste)

# Wiederholung mit *
wiederholte_liste = liste1 * 3
print("Wiederholte Liste:", wiederholte_liste)

# %% [markdown]
# ### Listen als Stapel und Warteschlangen
#
# Listen können verwendet werden, um Stapel (LIFO) und Warteschlangen (FIFO) zu implementieren.

# %%
# Verwendung der Liste als Stapel
stapel = []
stapel.append(1)
stapel.append(2)
stapel.append(3)
print("Stapel nach push:", stapel)

letztes_element = stapel.pop()
print("Gepopptes Element:", letztes_element)
print("Stapel nach pop:", stapel)


# %%

# Verwendung der Liste als Warteschlange (Hinweis: Für große Listen ineffizient)
warteschlange = []
warteschlange.append('a')
warteschlange.append('b')
warteschlange.append('c')
print("Warteschlange nach enqueue:", warteschlange)

erstes_element = warteschlange.pop(0)
print("Dequeued Element:", erstes_element)
print("Warteschlange nach dequeue:", warteschlange)

# %% [markdown]
# ## Mengen
#
# ### Was ist eine Menge?
#
# Eine **Menge** ist eine **ungeordnete**, **veränderliche** Sammlung von **einzigartigen** Elementen. Mengen werden verwendet, um mehrere Elemente in einer einzelnen Variablen zu speichern und werden durch geschweifte Klammern `{}` definiert, wobei die Elemente durch Kommas `,` getrennt sind, oder durch Verwendung des `set()`-Konstruktors.
#
# **Eigenschaften von Mengen:**
#
# - **Ungeordnet**: Elemente haben keine definierte Reihenfolge.
# - **Veränderlich**: Elemente können nach der Erstellung der Menge hinzugefügt oder entfernt werden.
# - **Keine doppelten Elemente**: Jedes Element ist einzigartig.
# - **Elemente müssen unveränderlich sein**: Elemente müssen von unveränderlichen Datentypen sein.

# %%
# Erstellen einer Menge
meine_menge = {1, 2, 3, 4, 5}
print("Meine Menge:", meine_menge)

# Erstellen einer Menge mit gemischten Datentypen
gemischte_menge = {"Hallo", 3.14, (1, 2, 3)}
print("Gemischte Menge:", gemischte_menge)

# Erstellen einer leeren Menge (Hinweis: Verwenden Sie set(), nicht {})
leere_menge = set()
print("Leere Menge:", leere_menge)

# %% [markdown]
# ### Zugriff auf Mengenelemente
#
# Da Mengen ungeordnet sind, können Sie nicht mit Indizes oder Slicing auf Elemente zugreifen. Sie können jedoch über eine Menge iterieren.

# %%
# Iterieren über eine Menge
for element in meine_menge:
    print(element)

# %% [markdown]
# ### Mengen modifizieren
#
# Sie können Elemente zu einer Menge hinzufügen und entfernen.

# %%
# Elemente hinzufügen
meine_menge.add(6)
print("Nach Hinzufügen von 6:", meine_menge)

# Elemente entfernen
meine_menge.remove(3)
print("Nach Entfernen von 3:", meine_menge)

# Element verwerfen (kein Fehler, wenn Element nicht existiert)
meine_menge.discard(10)
print("Nach discard(10) (nicht in der Menge):", meine_menge)

# Entfernen und Zurückgeben eines beliebigen Elements
entferntes_element = meine_menge.pop()
print("Entferntes Element:", entferntes_element)
print("Menge nach pop:", meine_menge)

# Alle Elemente entfernen
meine_menge.clear()
print("Menge nach clear:", meine_menge)

# %% [markdown]
# ### Mengenoperationen
#
# Mengen unterstützen mathematische Mengenoperationen wie Vereinigung, Schnittmenge, Differenz und symmetrische Differenz.

# %%
# Definieren von Mengen
menge_a = {1, 2, 3, 4, 5}
menge_b = {4, 5, 6, 7, 8}

print("Menge A:", menge_a)
print("Menge B:", menge_b)

# Vereinigung
vereinigung = menge_a.union(menge_b)
print("Vereinigung:", vereinigung)

# Schnittmenge
schnittmenge = menge_a.intersection(menge_b)
print("Schnittmenge:", schnittmenge)

# Differenz
differenz = menge_a.difference(menge_b)
print("Differenz (A - B):", differenz)

# Symmetrische Differenz
symm_diff = menge_a.symmetric_difference(menge_b)
print("Symmetrische Differenz:", symm_diff)

# %% [markdown]
# ### Mitgliedschaftstest in Mengen
#
# Das Überprüfen, ob ein Element in einer Menge enthalten ist, ist sehr effizient.

# %%
# Mitgliedschaftstest
print("Ist 3 in menge_a?", 3 in menge_a)
print("Ist 6 in menge_a?", 6 in menge_a)

# %% [markdown]
# ## Dictionaries
#
# ### Was ist ein Dictionary?
#
# Ein **Dictionary** ist eine **ungeordnete**, **veränderliche** Sammlung von **Schlüssel-Wert-Paaren**. Dictionaries sind für das Abrufen von Werten optimiert, wenn der Schlüssel bekannt ist.
#
# **Eigenschaften von Dictionaries:**
#
# - **Ungeordnet** (Python 3.7+ behält die Einfügereihenfolge bei)
# - **Schlüssel sind einzigartig** und müssen unveränderliche Typen sein (wie Strings, Zahlen oder Tupel).
# - **Werte** können jeglichen Typ haben und können dupliziert werden.

# %%
# Erstellen eines Dictionaries
mein_dict = {
    "name": "Alice",
    "alter": 30,
    "stadt": "Wunderland"
}
print("Mein Dictionary:", mein_dict)

# Verwendung des dict()-Konstruktors
anders_dict = dict([('name', 'Bob'), ('alter', 25)])
print("Anderes Dictionary:", anders_dict)

# Leeres Dictionary
leeres_dict = {}
print("Leeres Dictionary:", leeres_dict)

# %% [markdown]
# ### Zugriff auf Dictionary-Elemente
#
# Sie können auf Dictionary-Elemente über Schlüssel zugreifen, sie hinzufügen und ändern.

# %%
# Werte abrufen
name = mein_dict["name"]
print("Name:", name)

# Werte ändern
mein_dict["alter"] = 31
print("Aktualisiertes Dictionary:", mein_dict)

# Neue Schlüssel-Wert-Paare hinzufügen
mein_dict["beruf"] = "Abenteurer"
print("Nach Hinzufügen von 'beruf':", mein_dict)

# %% [markdown]
# ### Dictionary-Methoden
#
# Einige nützliche Methoden für Dictionaries sind:
#
# - **get()**: Gibt den Wert für den angegebenen Schlüssel zurück, falls vorhanden.
# - **keys()**: Gibt ein View-Objekt aller Schlüssel zurück.
# - **values()**: Gibt ein View-Objekt aller Werte zurück.
# - **items()**: Gibt ein View-Objekt aller Schlüssel-Wert-Paare (als Tupel) zurück.
# - **pop()**: Entfernt den angegebenen Schlüssel und gibt den entsprechenden Wert zurück.
# - **popitem()**: Entfernt und gibt das zuletzt eingefügte Schlüssel-Wert-Paar zurück.
# - **update()**: Aktualisiert das Dictionary mit Elementen aus einem anderen Dictionary oder Iterable von Schlüssel-Wert-Paaren.
# - **clear()**: Entfernt alle Elemente aus dem Dictionary.

# %%
# get()
stadt = mein_dict.get("stadt")
print("Stadt:", stadt)

# get() mit Standardwert
land = mein_dict.get("land", "Unbekannt")
print("Land:", land)

# keys()
schlüssel = mein_dict.keys()
print("Schlüssel:", schlüssel)

# values()
werte = mein_dict.values()
print("Werte:", werte)

# items()
paare = mein_dict.items()
print("Schlüssel-Wert-Paare:", paare)

# pop()
beruf = mein_dict.pop("beruf")
print("Entfernter Beruf:", beruf)
print("Dictionary nach pop:", mein_dict)

# popitem()
letztes_paar = mein_dict.popitem()
print("Zuletzt entferntes Paar:", letztes_paar)
print("Dictionary nach popitem:", mein_dict)

# update()
mein_dict.update({"alter": 32, "land": "Wunderland"})
print("Dictionary nach update:", mein_dict)

# clear()
mein_dict.clear()
print("Dictionary nach clear:", mein_dict)

# %% [markdown]
# ### Iterieren über Dictionaries

# %%
# Dictionary neu befüllen
mein_dict = {
    "name": "Alice",
    "alter": 32,
    "stadt": "Wunderland",
    "land": "Wunderland"
}

# Über Schlüssel iterieren
print("Schlüssel:")
for schlüssel in mein_dict:
    print(schlüssel)

# Über Werte iterieren
print("\nWerte:")
for wert in mein_dict.values():
    print(wert)

# Über Schlüssel-Wert-Paare iterieren
print("\nSchlüssel-Wert-Paare:")
for schlüssel, wert in mein_dict.items():
    print(f"{schlüssel}: {wert}")

# %% [markdown]
# ### Verschachtelte Dictionaries
#
# Dictionaries können andere Dictionaries enthalten, was es ermöglicht, verschachtelte Datenstrukturen zu erstellen.

# %%
# Erstellen eines verschachtelten Dictionaries
verschachteltes_dict = {
    "kind1": {"name": "Emily", "alter": 5},
    "kind2": {"name": "Daniel", "alter": 3}
}
print("Verschachteltes Dictionary:", verschachteltes_dict)

# Zugriff auf Elemente im verschachtelten Dictionary
name_von_kind1 = verschachteltes_dict["kind1"]["name"]
print("Name von Kind1:", name_von_kind1)

# %% [markdown]
# ## Zusammenfassung
#
# In dieser Lektion haben wir die grundlegenden Datenstrukturen in Python erkundet:
#
# - **Tupel**: Unveränderliche, geordnete Sequenzen von Elementen.
# - **Listen**: Veränderliche, geordnete Sequenzen von Elementen.
# - **Mengen**: Veränderliche, ungeordnete Sammlungen von einzigartigen Elementen.
# - **Dictionaries**: Veränderliche, ungeordnete Sammlungen von Schlüssel-Wert-Paaren.
#
# Das Verständnis dieser Datenstrukturen ist entscheidend für effektive Python-Programmierung, da sie es ermöglichen, Daten effizient zu speichern und zu manipulieren. Jede Datenstruktur hat ihre eigenen Anwendungsfälle und Vorteile, abhängig von den Anforderungen Ihres Programms.
#
# **Wesentliche Erkenntnisse:**
#
# - Verwenden Sie **Tupel**, wenn Sie eine unveränderliche Sequenz von Elementen benötigen.
# - Verwenden Sie **Listen**, wenn Sie eine veränderliche Sequenz benötigen, in der Elemente hinzugefügt, entfernt oder geändert werden können.
# - Verwenden Sie **Mengen**, wenn Sie einzigartige Elemente speichern und Mengenoperationen durchführen müssen.
# - Verwenden Sie **Dictionaries**, wenn Sie Schlüssel mit Werten für effizientes Nachschlagen und Manipulieren verknüpfen müssen.
