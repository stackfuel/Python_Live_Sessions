# %% [markdown]
# # Kontrollstrukturen in Python
#
# In diesem Notebook werden wir die typischen Kontrollstrukturen in Python kennenlernen und anhand von Beispielen demonstrieren.

# %% [markdown]
# ## Bedingte Anweisungen
#
# Bedingte Anweisungen führen Code in Abhängigkeit von einer konkreten Bedingung aus. Durch bedingte Anweisungen können Verzweigungen im Code eingebaut werden.

# %% [markdown]
# ### Die `if`-Anweisung
#
# Durch das Schlüsselwort `if` können wir einen bestimmten Teil des Codes nur dann ausführen lassen, wenn eine Bedingung erfüllt ist.
#
# Bedingungen sind Ausdrücke, die als Boolean ausgewertet werden können, also ein `True` oder `False` Ergebnis liefern.

# %% [markdown]
# #### Beispiele für Bedingungen
#
# - `... in ...`
# - `... == ...`, `... > ...`, etc.
# - Auch Zahlen und Collections können in Bedingungen genutzt werden.

# %%
# Beispiel: Überprüfen, ob ein Schüler in der Liste der bestandenen Schüler ist

bestandene_schueler = ["Anna", "Bernd", "Claudia"]
schueler = "Daniel"

if schueler in bestandene_schueler:
    print(f"{schueler} hat die Prüfung bestanden.")
else:
    print(f"{schueler} hat die Prüfung nicht bestanden.")

# %%
# Beispiel: Überprüfen, ob eine Note größer oder gleich 50 ist

note = 75

if note >= 50:
    print("Der Schüler hat bestanden.")
else:
    print("Der Schüler ist durchgefallen.")

# %%
# Beispiel: Überprüfen, ob eine Liste leer ist

studenten_liste = []

if studenten_liste:
    print("Die Liste der Studenten ist nicht leer.")
else:
    print("Es sind keine Studenten vorhanden.")

# %% [markdown]
# ### Das Schlüsselwort `pass`
#
# Das Schlüsselwort `pass` kann verwendet werden, um der Sprache klar zu machen, dass hier zunächst nichts passieren soll.

# %%
# Beispiel: Platzhalter für zukünftigen Code

if True:
    pass  # Hier wird später Code eingefügt

print("Dies ist außerhalb des if-Blocks.")

# %% [markdown]
# ### Der `else`-Block
#
# Durch das Schlüsselwort `else` nach einem `if`-Block kann eine alternative Folge von Anweisungen ausgeführt werden, falls die Bedingung aus der `if`-Anweisung `False` ist.

# %%
# Beispiel: Bestimmen, ob eine Zahl gerade oder ungerade ist

zahl = 7

if zahl % 2 == 0:
    print(f"{zahl} ist eine gerade Zahl.")
else:
    print(f"{zahl} ist eine ungerade Zahl.")

# %% [markdown]
# ### Die `elif`-Anweisung
#
# Eine Kombination von `if` und `else`, um mehrere Bedingungen nacheinander zu überprüfen.

# %%
# Beispiel: Schulnoten bewerten

note = 85

if note >= 90:
    print("Note: Sehr gut")
elif note >= 75:
    print("Note: Gut")
elif note >= 60:
    print("Note: Befriedigend")
elif note >= 50:
    print("Note: Ausreichend")
else:
    print("Note: Mangelhaft")

# %% [markdown]
# ### Negation von Bedingungen mit `not`
#
# Bedingungen für die `if`-Anweisung können durch `not` negiert werden. Dies ist oft praktisch, um zu stark verschachtelte `if`-Konstrukte zu reduzieren.

# %%
# Beispiel ohne `not`

status = "inaktiv"

if status == "aktiv":
    print("Der Benutzer ist aktiv.")
else:
    print("Der Benutzer ist nicht aktiv.")

# %%
# Beispiel mit `not`

status = "inaktiv"

if not status == "aktiv":
    print("Der Benutzer ist nicht aktiv.")
else:
    print("Der Benutzer ist aktiv.")

# %%
# Reduzierung von Verschachtelung mit `not`

logged_in = False

if not logged_in:
    print("Bitte melden Sie sich an.")
else:
    print("Willkommen zurück!")

# %% [markdown]
# ## Schleifen
#
# Schleifen werden genutzt, um eine Abfolge von Anweisungen wiederholt auszuführen.

# %% [markdown]
# ### Die `while`-Schleife
#
# Die `while`-Schleife funktioniert wie die `if`-Bedingung, nur dass der Körper solange wiederholt ausgeführt wird, wie die Bedingung zu `True` ausgewertet wird.

# %%
# Beispiel: Countdown von 5 auf 1

count = 5

while count > 0:
    print(count)
    count -= 1

print("Start!")

# %% [markdown]
# Schleifen können durch zwei Anweisungen unterbrochen werden:
#
# - `break` beendet die Schleife komplett und verlässt den Schleifenkörper.
# - `continue` stoppt die aktuelle Iteration und führt dazu, dass die Schleife mit der nächsten Iteration fortfährt.

# %%
# Beispiel für `break`

zahl = 0

while True:
    print(zahl)
    zahl += 1
    if zahl > 5:
        break

print("Schleife wurde mit `break` beendet.")

# %%
# Beispiel für `continue` in einer `while`-Schleife

zahl = 0

while zahl < 10:
    zahl += 1
    if zahl % 2 == 0:
        continue
    print(zahl)

print("Es wurden nur ungerade Zahlen ausgegeben.")

# %% [markdown]
# ### Der `else`-Zweig in Schleifen
#
# Auch `while`-Schleifen können durch einen `else`-Zweig erweitert werden. Dieser wird, wie bei der `if`-Anweisung, nur dann ausgeführt, wenn die Schleifenbedingung zu `False` ausgewertet wird. Dies passiert in der Regel, wenn eine Schleife ohne Unterbrechung (`break`) durchläuft.

# %%
# Beispiel für `else` in einer `while`-Schleife

zahl = 5

while zahl > 0:
    print(zahl)
    zahl -= 1
else:
    print("Die Schleife wurde normal beendet.")

# %% [markdown]
# ### Sonderfall Endlosschleife
#
# `while`-Schleifen können schnell zu Endlosschleifen führen. Dies passiert immer dann, wenn während der Ausführung des Schleifenkörpers keine Elemente verändert werden, die in der Bedingung der Schleife genutzt werden, und keine `break`-Anweisung getriggert wird.

# %%
# Beispiel einer unbeabsichtigten Endlosschleife

zahl = 5

# Achtung: Dieser Code würde unendlich laufen, da `zahl` nie verändert wird.
# while zahl > 0:
#     print("Dies ist eine Endlosschleife.")

# %%
# Beispiel einer beabsichtigten Endlosschleife

while True:
    eingabe = input("Geben Sie 'exit' ein, um zu beenden: ")
    if eingabe == "exit":
        print("Programm wird beendet.")
        break
    else:
        print(f"Sie haben '{eingabe}' eingegeben.")

# %% [markdown]
# ## Einschub: Iteratoren
#
# Ein Iterator ist ein Objekt, das auf einer gegebenen Datenstruktur oder einem Generator bzw. einer Instanz dieser aufsetzt und stets auf ein Element dieser Struktur zeigt.

# %% [markdown]
# ### Beispiele für Datenstrukturen, die einen Iterator unterstützen:
#
# - `list`, `tuple`, `set`, `dictionary`, `string`, etc.

# %%
# Beispiel mit einer Liste

meine_liste = [1, 2, 3]
mein_iterator = iter(meine_liste)

print(next(mein_iterator))  # Ausgabe: 1
print(next(mein_iterator))  # Ausgabe: 2
print(next(mein_iterator))  # Ausgabe: 3

# %%
# Versuch, über das Ende hinaus zu iterieren

try:
    print(next(mein_iterator))
except StopIteration:
    print("Keine weiteren Elemente im Iterator.")

# %% [markdown]
# ### Einschub: Exception Handling
#
# Solche Fehler können durch eine weitere Kontrollstruktur behandelt werden: `try` und `except`.

# %%
# Beispiel: Nachbildung einer `for`-Schleife mit einem Iterator und `while`

meine_liste = [1, 2, 3]
mein_iterator = iter(meine_liste)

while True:
    try:
        element = next(mein_iterator)
        print(element)
    except StopIteration:
        print("Alle Elemente wurden verarbeitet.")
        break

# %% [markdown]
# ## Die `for`-Schleife
#
# Pythons `for`-Schleife ist in anderen Sprachen als `for-each`-Schleife bekannt. Sie arbeitet mit einem Iterator und durchläuft jedes Element einer gegebenen Datenstruktur bzw. eines Generators. Bei jedem Durchlauf werden diese Elemente einer Variable zugeordnet, wodurch auf die Elemente einzeln zugegriffen werden kann.

# %%
# Beispiel: Durchlaufen einer Liste von Studenten

studenten = ["Anna", "Bernd", "Claudia"]

for student in studenten:
    print(f"Student: {student}")

# %%
# Beispiel: Berechnung der Quadratwerte einer Zahlenliste

zahlen = [1, 2, 3, 4, 5]

for zahl in zahlen:
    quadrat = zahl ** 2
    print(f"Das Quadrat von {zahl} ist {quadrat}")

# %%
# Beispiel mit `break` in einer `for`-Schleife

for zahl in zahlen:
    if zahl == 3:
        print("Zahl 3 gefunden, Schleife wird beendet.")
        break
    print(f"Zahl: {zahl}")

# %%
# Beispiel mit `continue` in einer `for`-Schleife

for zahl in zahlen:
    if zahl % 2 == 0:
        continue
    print(f"Ungerade Zahl: {zahl}")

# %%
# Beispiel: Verwendung von `enumerate` in einer `for`-Schleife

studenten = ["Anna", "Bernd", "Claudia"]

for index, student in enumerate(studenten, start=1):
    print(f"Student {index}: {student}")

# %%
# Beispiel: Durchlaufen eines Wörterbuchs

noten = {"Anna": 85, "Bernd": 78, "Claudia": 92}

for name, note in noten.items():
    print(f"{name} hat {note} Punkte erzielt.")

# %%
# Beispiel: Verschachtelte Schleifen

for student in studenten:
    for buchstabe in student:
        print(buchstabe, end=" ")
    print()  # Neue Zeile nach jedem Namen

# %% [markdown]
# ## Typische Fehler beim Arbeiten mit Schleifen

# %% [markdown]
# ### Änderung der Liste während der Iteration

# %%
# Beispiel für Problem beim Ändern einer Liste während der Iteration

zahlen = [1, 2, 3, 4, 5]

for zahl in zahlen:
    if zahl % 2 == 0:
        zahlen.remove(zahl)

print(zahlen)

# Kommentar: Dies führt zu unerwartetem Verhalten, da die Liste während der Iteration verändert wird.

# %%
# Korrekte Vorgehensweise mit List Comprehension

zahlen = [1, 2, 3, 4, 5]
zahlen_neu = [zahl for zahl in zahlen if zahl % 2 != 0]

print(zahlen_neu)

# %% [markdown]
# ### Vergessen der Iterationsvariable in einer `while`-Schleife

# %%
# Beispiel: Endlosschleife aufgrund fehlender Änderung der Bedingung

# Achtung: Dieser Code würde eine Endlosschleife erzeugen.
# count = 5
#
# while count > 0:
#     print(count)
#     # Vergessen, `count` zu verringern
#     # count -= 1

# %%
# Korrektur:

count = 5

while count > 0:
    print(count)
    count -= 1

# %% [markdown]
# ### Off-by-One Fehler

# %%
# Beispiel: Falscher Bereich in `range`

for i in range(1, 10):  # Geht von 1 bis 9, nicht bis 10
    print(i)

# Kommentar: Wenn man bis einschließlich 10 zählen möchte, muss man `range(1, 11)` verwenden.

# %%
# Korrektur:

for i in range(1, 11):
    print(i)

# %% [markdown]
# ## Fazit
#
# In diesem Notebook haben wir die grundlegenden Kontrollstrukturen in Python kennengelernt, darunter bedingte Anweisungen mit `if`, `else` und `elif`, sowie Schleifenstrukturen wie die `while`- und `for`-Schleife. Wir haben gesehen, wie man Bedingungen formuliert, Schleifen kontrolliert und häufige Fehler vermeidet.

# %%
# Ende des Notebooks