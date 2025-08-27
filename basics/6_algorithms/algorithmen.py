# %% [markdown]
# ## Algorithmen
# 
# Ein Algorithmus ist eine **eindeutige**, **endliche Abfolge** von **Anweisungen** oder Regeln, die dazu dient, ein bestimmtes **Problem zu lösen** oder eine bestimmte Aufgabe zu erfüllen. Diese Anweisungen werden in einer **bestimmten Reihenfolge** ausgeführt, um von einem Ausgangszustand zu einem gewünschten Endzustand zu gelangen.
# 
# Hier sind einige wichtige Merkmale eines Algorithmus:
# 
# 1. **Eindeutigkeit**: Jede Anweisung muss klar und unmissverständlich sein.
# 2. **Endlichkeit**: Der Algorithmus muss nach einer endlichen Anzahl von Schritten zum Abschluss kommen.
# 3. **Ausführbarkeit**: Jeder Schritt des Algorithmus muss ausführbar sein.
# 4. **Determinismus**: Ein Algorithmus sollte bei gleichen Ausgangsbedingungen immer dieselben Ergebnisse liefern.
# 5. **Eingaben und Ausgaben**: Ein Algorithmus kann Null oder mehr Eingaben haben und eine oder mehrere Ausgaben liefern.
# 
# Algorithmen sind grundlegend in der Informatik und Mathematik und werden in vielen Bereichen eingesetzt, von der Berechnung mathematischer Funktionen bis hin zur Steuerung komplexer Systeme in der Technik und Wirtschaft.
# 

# %% [markdown]
# ### Größter gemeinsame Teiler
# Der größte gemeinsame Teiler (GGT) zweier natürlicher Zahlen $a$ und $b$, auch als größter gemeinsamer Divisor (ggD) bezeichnet, ist die größte natürliche Zahl $d$, die sowohl $a$ als auch $b$ ohne Rest teilt. Mathematisch lässt sich der GGT so definieren:
# 
# $$
# \text{GGT}(a, b) = \max \{ d \in \mathbb{N} : d \mid a \text{ und } d \mid b \}
# $$
# 
# Dabei bedeutet $d \mid a$, dass $d$ ein Teiler von $a$ ist, also $a$ durch $d$ ohne Rest teilbar ist.

# %%
a = 60
b = 90

max_d = min(a, b)
N = range(1, max_d+1)

cds = {d for d in N if a%d==0 and b%d==0}
gcd = max(cds)

print(f"Alle gemeinsamend Teiler von {a} und {b}: {cds}")
print(f"Größter gemeinsame Teiler: {gcd}")

# %% [markdown]
# ### Beispiel Euklidischer Algorithmus
# 
# Der euklidische Algorithmus ist ein effizienter Weg zur Bestimmung des größten gemeinsamen Teilers (GGT) zweier natürlicher Zahlen. Er basiert auf der Tatsache, dass der GGT zweier Zahlen auch der GGT der kleineren Zahl und dem Rest der Division der größeren Zahl durch die kleinere Zahl ist. 
# 
# Hier sind die Schritte des euklidischen Algorithmus in Kurzform:
# 
# 1. Gegeben sind zwei Zahlen $a$ und $b$ mit $a > b$.
# 2. Teile $a$ durch $b$ und bestimme den Rest $r$ (also $a \mod b$).
# 3. Ersetze $a$ durch $b$ und $b$ durch $r$.
# 4. Wiederhole die Schritte 2 und 3, bis $r = 0$.
# 5. Der GGT ist der letzte nicht-null Rest $b$.
# 
# Der Algorithmus ist besonders effizient, da er die Größe der Zahlen in jedem Schritt reduziert. Dies führt zu einer logarithmischen Laufzeit im Verhältnis zur Größe der Eingabewerte.
# 
# ![Euclidean Algorithm](Euclidean_algorithm.gif)
# 
# *Subtraktionsbasierte Animation des euklidischen Algorithmus. Das ursprüngliche Rechteck hat die Dimensionen a = 1071 und b = 462. Quadrate der Größe 462×462 werden darin platziert, wobei ein Rechteck von 462×147 übrig bleibt. Dieses Rechteck wird mit 147×147-Quadraten gefüllt, bis ein Rechteck von 21×147 übrig bleibt, das wiederum mit 21×21-Quadraten gefüllt wird, ohne unbedeckte Fläche zu hinterlassen. Die kleinste Quadratgröße, 21, ist der GGT von 1071 und 462.*
# *Quelle: [Wikipedia](https://de.wikipedia.org/wiki/Euklidischer_Algorithmus)*
# 
# Beispiel:
# Um den GGT von 48 und 18 zu finden:
# 
# 1. 48 mod 18 = 12 (Rest ist 12)
# 2. 18 mod 12 = 6 (Rest ist 6)
# 3. 12 mod 6 = 0 (Rest ist 0)
# 
# Der GGT ist 6.

# %%
a = 48
b = 18

while b != 0:
    print(f"{'a '*a}")
    print(f"{'b '*b}")
    print("")
    rest = a%b
    a = b
    b = rest
    
print(f"{'a '*a}")
print(f"{'b '*b}")
print(f"gcd is {a}")


# %% [markdown]
# #### Verallgemeinerung als Funktion

# %%
def gcd(a, b):
    while b != 0:
        rest = a%b
        a = b
        b = rest
    return a

# %%
# Testfälle mit tabellarischer Ausgabe
test_cases = [
    (48, 18),
    (101, 10),
    (20, 8),
    (0, 5),
    (42, 56),
    (270, 192),
    (17, 31),
    (123456, 789012)
]

# Header der Tabelle
print(f"{'a':>10} | {'b':>10} | {'gcd(a, b)':>10}")
print("-" * 36)

# Testfälle und Ergebnisse in tabellarischer Form ausgeben
for a, b in test_cases:
    result = gcd(a, b)
    print(f"{a:>10} | {b:>10} | {result:>10}")

# %% [markdown]
# ## Rekursion
# 
# Rekursion ist ein Prinzip, bei dem eine **Funktion sich selbst aufruft**, um ein Problem in kleinere, leichter lösbare Teilprobleme zu zerlegen. Eine rekursive Funktion enthält eine oder mehrere **Basisbedingungen**, die ohne weitere Rekursion gelöst werden können, und eine **Rekursionsbedingung**, die die Funktion erneut mit anderen Argumenten aufruft.
# 
# In unserem Beispiel wird die Funktion `gcd` rekursiv aufgerufen, um den größten gemeinsamen Teiler (GGT) zweier Zahlen zu berechnen. Die Basisbedingung tritt ein, wenn der zweite Parameter `b` gleich 0 ist. In diesem Fall gibt die Funktion den Wert von `a` zurück, da der GGT in diesem Fall `a` ist. Andernfalls wird die Funktion erneut mit den Argumenten `b` und dem Rest der Division von `a` durch `b` aufgerufen.

# %%
def gcd(a, b=0):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(12, 18))

# %% [markdown]
# 
# In dieser Version der Funktion `gcd` wird die Rekursion so implementiert, dass sie eine beliebige Anzahl von Argumenten akzeptiert. Wenn nur ein Argument übergeben wird, wird die Funktion mit dem ersten Argument und 0 aufgerufen. Wenn mehrere Argumente übergeben werden, wird die Funktion rekursiv mit dem ersten und dem Rest der Argumente aufgerufen.
# 

# %%
def gcd(a, b=0, *args):
    if b == 0:
        if not args:
            return a
        return gcd(a, *args)
    
    return gcd(b, a%b)

print(gcd(12, 18))
print(gcd(12, 18, 24))

# %% [markdown]
# ### Beispiel Quicksort
# 
# ![Quicksort](Quicksort_image.png)
# 
# *Quelle: [Medium](https://medium.com/@dinmukhamed.dukumbayev26/quicksort-is-c-a8cc34a6ccc0)*
# 
# Quicksort ist ein effizienter Sortieralgorithmus, der das **"Teile und Herrsche"**-Prinzip nutzt. Er wählt ein Pivotelement und teilt das Array in kleinere Teile, die rekursiv sortiert werden. Seine Einfachheit und Effektivität machen ihn zu einem der am häufigsten verwendeten Sortieralgorithmen in der Informatik.
# 
# 1. **Basisfall**: Wenn das Array `arr` leer ist oder nur ein Element enthält, ist es bereits sortiert, und wir geben es zurück.
# 
# 2. **Pivot-Auswahl**: Wir wählen das letzte Element des Arrays als Pivot.
# 
# 3. **Partitionierung**:
#    - `left`: Alle Elemente, die kleiner als der Pivot sind.
#    - `middle`: Alle Elemente, die gleich dem Pivot sind (dies berücksichtigt auch Duplikate).
#    - `right`: Alle Elemente, die größer als der Pivot sind.
# 
# 4. **Rekursion**: Wir sortieren rekursiv die `left`- und `right`-Teile und kombinieren die Ergebnisse mit den `middle`-Elementen.
# 

# %%

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot  = arr[-1]
        left, middle, right = [], [], []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                middle.append(arr[i])
        print(left, middle, right)
        return quicksort(left) + middle + quicksort(right)


# %%
# Beispielnutzung
array = [15, 3, 2, 8, 11, 10, 1, 6, 3, 1]
print(array)
sorted_array = quicksort(array)
print(sorted_array)

# %% [markdown]
# ## Beispiel Binäre Suche
# 
# ![Binary Search](binarysearch_image.png)
# 
# *Quelle: [GeekforGeeks](https://www.geeksforgeeks.org/complexity-analysis-of-binary-search/)*
# 
# Die binäre Suche ist ein effizienter Suchalgorithmus, der das Prinzip der Divide and Conquer Strategie (Teile und Herrsche) nutzt. Dies ermöglicht es, in logarithmischer Zeit zu operieren, indem der Suchbereich mit jedem Schritt halbiert wird, anstatt jedes Element sequenziell zu durchlaufen. Angenommen, dass das Array bereits sortiert ist, wird der Algorithmus wie folgt beschrieben:
# 
# 1. Initialisierung der Zeiger left und right,
# 
# 2. Berechnung des mittleren Index und Vergleich des Zielwertes (target) mit dem Wert am mittleren Index mid_val,
# 
# 3. Anpassung der Zeiger basierend darauf, ob mid_val kleiner oder größer als target ist.
# 
# 4. Rückgabe des Indexes des gefundenen Zielwertes oder -1, falls das Element nicht gefunden wird.

# %%
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        print(arr[left:right+1])
        
        mid = (left + right) // 2
        mid_val = arr[mid]
        
        if mid_val == target:
            return mid                      # Element gefunden, Rückgabe des Index
        elif mid_val < target:
            left = mid + 1                  # Suche im rechten Teil weiter
        else:
            right = mid - 1                 # Suche im linken Teil weiter
    
    return -1  # Element nicht gefunden



# %%
# Beispielverwendung:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} gefunden bei Index {result}.")
else:
    print(f"Element {target} nicht in der Liste gefunden.")

# %%



