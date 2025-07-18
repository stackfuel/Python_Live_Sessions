```markdown
# Von funktionaler zu objektorientierter Vektor-Implementierung

In dieser Lektion werden wir untersuchen, wie man die Implementierung eines zweidimensionalen Vektors von einer rein **funktionalen Herangehensweise** Schritt für Schritt in eine **objektorientierte Variante** überführen kann. Dadurch wird nicht nur das Prinzip der **Kohäsion** gestärkt, sondern auch die **Kapselung** von Daten und zugehörigen Funktionen erreicht. Gleichzeitig zeigen wir, wie sich die Integration mit Python verbessert und wie die Nutzung typischer Operatoren ermöglicht wird.

> **Hinweis:** Der vollständige Code zur Vektor-Arithmetik befindet sich in den Dateien `vector_functional.py` und `vector_oop.py`. Im folgenden Notebook werden diese Dateien importiert und ihre Funktionalität vorgestellt.

---

## Inhalt

1. [Funktionale Implementierung von Vektoren](#funktional)
2. [Nachteile der funktionalen Variante](#nachteile)
3. [Objektorientierter Entwurf: Vom Funktionspaket zur Klasse](#ooo)
4. [Operatoren und Integration: Python wie gehabt](#op)
5. [Fazit: Vorteile der objektorientierten Herangehensweise](#fazit)

---

<a id="funktional"></a>
## 1. Funktionale Implementierung von Vektoren

In der funktionalen Variante werden Vektoren als **Tupel** dargestellt. Alle Operationen sind als separate Funktionen implementiert, die Vektoren manipulieren oder analysieren.

Zunächst importieren wir die Funktionen aus dem `vector_functional.py`:

```python
from vector_functional import (
    create_vector,
    add,
    sub,
    mul,
    dot_product,
    magnitude,
    normalize,
)
```

### Beispiel: Nutzung der Funktionen

```python
v1 = create_vector(3, 4)
v2 = create_vector(1, 2)

print("Addition:", add(v1, v2))
print("Skalierung:", mul(v1, 2))
print("Betrag:", magnitude(v1))
print("Skalarprodukt:", dot_product(v1, v2))
print("Normalisiert:", normalize(v1))
```

**Erklärung:**  
Jede Funktion arbeitet mit Vektoren als Tupeln, z.B. `(x, y)`. Im Beispiel werden Vektoren erstellt und anschließend verschiedene Operationen durchgeführt.

---

<a id="nachteile"></a>
## 2. Nachteile der funktionalen Variante

Die funktionale Implementierung funktioniert, hat aber einige **Nachteile**:

- **Geringe Kohäsion:** Die Daten (Tupel) und die zugehörigen Funktionen sind _getrennt_. Es besteht kein direkter Zusammenhang zwischen den Werten eines Vektors und den Operationen darauf.
- **Fehlende Kapselung:** Es gibt keine Möglichkeit, die Vektorstruktur zu verstecken oder zu schützen. Alle Operationen erfordern, dass der Nutzer die interne Struktur kennt.
- **Erweiterung und Wartung:** Das Hinzufügen neuer Funktionalität ist umständlich; neue Funktionen sind global und nicht an das Datenobjekt gebunden.
- **Fehlende Integration in Python:** Python bietet die Möglichkeit, Operatoren wie `+`, `-` oder `*` zu überladen. Diese Möglichkeit bleibt ungenutzt.

### Beispiel: Fehlende Operatorintegration

```python
v1 = create_vector(3, 4)
v2 = create_vector(1, 2)

# Funktioniert NICHT!
# result = v1 + v2   # TypeError: can only concatenate tuple (not "tuple") to tuple
```

---

<a id="ooo"></a>
## 3. Objektorientierter Entwurf: Vom Funktionspaket zur Klasse

#### Das Prinzip: Daten und Funktionalität werden **gemeinsam** verwaltet.

Statt mit einzelnen Funktionen und nackten Tupeln zu arbeiten, fassen wir sowohl die Daten (x, y) als auch die Methoden (addieren, skalieren etc.) in einer **Klasse** zusammen.

Importieren wir die Klasse aus `vector_oop.py`:

```python
from vector_oop import Vector2D
```

### Schrittweise Umstellung: Vom Tupel zur Klasse

**Funktional:**
```python
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])
```

**Objektorientiert:**
```python
class Vector2D:
    ...
    def __add__(self, other):
        return Vector2D(self[0] + other[0], self[1] + other[1])
```

**Erklärung:**  
Die Funktion `add` wird jetzt zu einer Methodenfunktion `__add__`, die automatisch durch den Operator `+` aufgerufen wird. Daten und Methoden befinden sich jetzt im selben Namensraum.

---

**Beispiel: Nutzung der objektorientierten Variante**

```python
a = Vector2D(3, 4)
b = Vector2D(1, 2)

print("Addition:", a + b)                 # Python-Operator!
print("Skalierung:", a * 2)
print("Betrag:", a.magnitude())
print("Skalarprodukt:", a.dot_product(b))
print("Normalisiert:", a.normalize())
```

**Vorteile:**
- Methoden sind direkt mit dem Vektor verknüpft (Kohäsion).
- Neue Funktionalitäten können leicht als weitere Methoden ergänzt werden.
- Python-Operatoren sind nutzbar (intuitive Syntax).
- Die interne Darstellung ist gekapselt (z.B. könnten wir später von Tupel auf Liste wechseln, ohne den Anwendercode ändern zu müssen).

---

<a id="op"></a>
## 4. Operatoren und direkte Python-Integration

**Magische Methoden** (wie `__add__`, `__sub__`, usw.) erlauben es uns, eigene Datentypen wie eingebaute Typen (z.B. Zahlen, Listen) zu verwenden.

**Beispiel:**

```python
v1 = Vector2D(3, 4)
v2 = Vector2D(2, 7)

# Addieren mit +
result = v1 + v2      # entspricht v1.__add__(v2)
print(result)

# Skalarmultiplikation mit *
print(v1 * 10)

# Skalarprodukt (Dot-Product)
print(v1.dot_product(v2))

# Normalisierung
print(v1.normalize())
```

---

<a id="fazit"></a>
## 5. Fazit: Vorteile der objektorientierten Herangehensweise

Abschließend lässt sich festhalten:

- Methoden sind **Funktionen** – lediglich innerhalb einer Klasse gruppiert.
- Objektorientierung führt zu **Kapselung** (Daten + Methoden), **Kohäsion** (enge Bindung verwandter Funktionalität) und besserer **Wartbarkeit**.
- Die Integration mit Python wird durch Operatoren und Methoden viel _natürlicher_.

> **Zusammengefasst:**  
Während die funktionale Variante einfach zu verstehen ist, ist die objektorientierte Herangehensweise für komplexere und erweiterbare Programme meist die bessere Wahl.

---

### Weiterführende Aufgaben

- Implementieren Sie eine weitere Methode (z.B. Projektion eines Vektors auf einen anderen) als Übung sowohl für die funktionale als auch für die objektorientierte Variante.
- Testen Sie, ob die objektorientierte Methode wirklich Kapselung bietet: Ändern Sie die interne Darstellung im Konstruktor der Klasse!

---

**Ende der Lektion**
```