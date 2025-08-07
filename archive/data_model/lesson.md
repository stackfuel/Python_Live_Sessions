# 1. Einleitung

In dieser Unterrichtseinheit werden wir das Python Data Model anhand einer eigens entwickelten Vector-Klasse erkunden. Das Python Data Model definiert, wie Objekte in Python mit besonderen Methoden – den sogenannten *Dunder-Methoden* (double underscore methods) – interagieren. Diese Methoden ermöglichen es, benutzerdefinierte Klassen nahtlos in die Python-Sprache zu integrieren, sodass sie sich wie eingebaute Datentypen verhalten.

## Ziel und Überblick

Der Schwerpunkt dieser Einheit liegt auf:

- **Verstehen der Dunder-Methoden:** Wir lernen, welche speziellen Methoden es gibt und wie sie zur Anpassung des Verhaltens unserer Klassen beitragen. Beispiele sind Methoden für den Containerzugriff (`__getitem__`, `__len__`, `__iter__`) oder für arithmetische Operationen (`__add__`, `__mul__`, `__matmul__`).
- **Praktische Anwendung:** Am Beispiel der *Vector*-Klasse werden grundlegende Operationen eines mathematischen Vektors implementiert, wie zum Beispiel:
  - Die Berechnung des Betrags, $$\|v\| = \sqrt{\sum_{i=1}^{n}v_i^2},$$
  - Vektoraddition und -subtraktion,
  - Skalare Multiplikation und elementweise Multiplikation,
  - Dot-Produkt (Skalarprodukt) und 
  - Vergleichsoperationen basierend auf der Vektormagnitude.

## Relevanz des Python Data Model

Das Verständnis des Python Data Model ist essenziell, um eigene Klassen so zu gestalten, dass sie sich in Python "pythonisch" verhalten. Mit Hilfe der Dunder-Methoden können Klassen:
 
- In Standardoperatoren eingebunden werden, z.B. Addition mit dem `+`-Operator oder Vergleiche mit `<` und `==`.
- Als Container verwendet werden, sodass sie mit Schleifen, der `in`-Syntax und weiteren Standardfunktionen (wie `len()`) interagieren.
- Als unveränderliche oder mutable Objekte gestaltet werden. In unserer Vector-Klasse wird beispielsweise die Immutabilität durch die Verwendung von Tuples und das Überschreiben der `__setitem__`-Methode sichergestellt.

## Vorstellung der Vector-Klasse

Die Vector-Klasse dient als praktisches Beispiel:
- **Mathematische Vektoren** werden hier durch eine Folge von Zahlen repräsentiert.
- Neben den grundlegenden Operationen (Addition, Subtraktion, Multiplikation, Division) nutzt die Klasse spezielle Operationen wie das Dot-Produkt (über `@`) und bietet Methoden zur Normierung und Berechnung von Distanzen und Winkeln.
- Durch den Einsatz von Methoden wie `__repr__` und `__str__` werden Vektoren für Debugging und Darstellung benutzerfreundlich aufbereitet.

Diese Einheit vermittelt Ihnen die Grundlagen, wie man das Python Data Model effektiv einsetzt, um robuste und intuitive Klassen zu erstellen. Im weiteren Verlauf werden wir jede Gruppe von Dunder-Methoden detailliert untersuchen und deren Implementierung und Einsatzmöglichkeiten anhand der Vector-Klasse erarbeiten.


### Mathematische Grundlagen



#### 1. Definition  
Ein Vektor $\mathbf v\in\mathbb R^n$ ist ein geordnetes $n$-Tupel seiner Komponenten
$$
\mathbf v = (v_1, v_2, \dots, v_n),\quad v_i\in\mathbb R.
$$  
- **Dimension**: $n$  
- **Komponente** $i$: $v_i$  

#### 2. Grundoperationen  
- **Addition** `u+v`
  $$
    \mathbf u + \mathbf v = (u_1+v_1,\dots,u_n+v_n) 
  $$  
- **Subtraktion** `u-v`
  $$
    \mathbf u - \mathbf v = \mathbf u + (-\mathbf v) =  (u_1-v_1,\dots,u_n-v_n)
  $$  
- **Skalarmultiplikation** `a*v`
  $$
    \lambda\,\mathbf v = (\lambda v_1,\dots,\lambda v_n),\quad \lambda\in\mathbb R
  $$  
- **Element-weise Multiplikation** `u*v`
  $$
    \mathbf u \odot \mathbf v = (u_1v_1,\dots,u_nv_n)
  $$  
- **Punkt-/Skalarprodukt** `u@v`
  $$
    \mathbf u \cdot \mathbf v
    =\sum_{i=1}^n u_i\,v_i
    
  $$  

#### 3. Länge (Norm)  
Euklidische Norm `abs(v)`
$$
  \|\mathbf v\| = \sqrt{\sum_{i=1}^n v_i^2}
  \quad\Longrightarrow\quad
  |\mathbf v| \;=\;\|\mathbf v\|.
$$  
- **Einheitsvektor** `v.normalize()`
  $$
    \hat{\mathbf v} = \frac{\mathbf v}{\|\mathbf v\|},\quad\|\mathbf v\|\neq 0.
  $$  

#### 4. Abstand & Winkel  
- **Abstand** 
  $$
    d(\mathbf u,\mathbf v) = \|\mathbf u - \mathbf v\|.
  $$  
- **Winkel**
  $$
    \cos\theta
    = \frac{\mathbf u\cdot\mathbf v}{\|\mathbf u\|\;\|\mathbf v\|},
    \quad
    \theta = \arccos(\cos\theta).
  $$  

#### 5. Vergleich & Immutability  
- **Gleichheit**: gleiche Komponenten  
- **Ordnung**: nach Magnitude $\|\mathbf u\|<\|\mathbf v\|$  
- Die Komponenten sind unveränderlich (immutable tuple).































# 2. Grundlagen des Python Data Model

Das Python Data Model legt fest, wie Objekte in Python intern funktionieren und wie sie mit den Sprachkonstrukten interagieren. Zentral dabei sind die sogenannten *Dunder-Methoden* (double underscore methods), die es erlauben, benutzerdefinierte Objekte wie native Python-Typen zu nutzen.

## Was sind Dunder-Methoden?

Dunder-Methoden sind spezielle Methoden, deren Name mit zwei Unterstrichen beginnt und endet, z. B. `__init__`, `__repr__` oder `__add__`. Sie definieren wichtige Verhaltensweisen von Objekten und werden automatisch von Python aufgerufen, wenn bestimmte Operatoren oder Funktionen verwendet werden. Zum Beispiel:

- `__init__`: Wird beim Erzeugen eines neuen Objekts ausgeführt.
- `__repr__`: Wird zur Darstellung des Objekts im Debugging- und Interpretermodus verwendet.
- `__str__`: Bestimmt, wie das Objekt mit `print()` ausgegeben wird.
- `__add__`: Ermöglicht das Überschreiben des `+`-Operators für benutzerdefinierte Addition.

Durch die Implementierung dieser Methoden in eigenen Klassen können Entwickler:innen das Verhalten ihrer Objekte fein abstimmen und sie in die Sprache „einbetten“.

## Bedeutung und Anwendung spezieller Protokolle

Python definiert verschiedene Protokolle, die von Dunder-Methoden abgedeckt werden. Diese Protokolle legen fest, wie Objekte sich verhalten sollen, wenn sie in bestimmten Kontexten verwendet werden:

- **Container-Protokoll:**  
  Mit Methoden wie `__len__`, `__getitem__`, `__setitem__` und `__contains__` wird definiert, wie Objekte als Container (ähnlich wie Listen oder Dictionaries) genutzt werden können. Beispielsweise ermöglicht `__getitem__` den Zugriff auf Elemente per Index, und `__iter__` erlaubt es, über die Elemente eines Objekts zu iterieren.
  
- **Iterator-Protokoll:**  
  Ein Objekt wird durch die Implementierung von `__iter__` (und gegebenenfalls `__next__`) zu einem Iterator. Damit können benutzerdefinierte Objekte direkt in Schleifen verwendet werden, z. B. mit `for`-Schleifen.
  
- **Numerisches Protokoll:**  
  Operatoren wie `+`, `-`, `*`, `/` und `@` (für das Dot-Produkt) können über Methoden wie `__add__`, `__sub__`, `__mul__`, `__truediv__` und `__matmul__` angepasst werden. Dadurch verhalten sich benutzerdefinierte numerische Objekte ähnlich wie eingebaute Zahlen oder Vektoren.
  
- **Vergleichsprotokoll:**  
  Durch die Implementierung von `__eq__`, `__lt__` und anderen Vergleichsoperatoren können Objekte miteinander verglichen werden. Oftmals wird auch der Dekorator `@total_ordering` genutzt, der anhand von wenigen definierten Vergleichsmethoden alle notwendigen Vergleiche ergänzt.
  
- **Sonstige Protokolle:**  
  Methoden wie `__hash__` (für die Verwendung als Schlüssel in Dictionaries) oder `__bool__` (für den Wahrheitswert eines Objekts) erlauben es, Objekte in weiter gefasste Python-Konzepte einzubetten.

Diese Protokolle ermöglichen eine nahtlose Integration benutzerdefinierter Klassen in allgemeine Python-Konzepte und -Funktionen, sodass sie auf natürliche Weise zusammenwirken.

## Erläuterung der Rollen von `__init__`, `__repr__` und `__str__`

Drei zentral wichtige Dunder-Methoden in jeder Klasse sind `__init__`, `__repr__` und `__str__`:

- **`__init__` (Initialisierungsmethode):**  
  Diese Methode wird aufgerufen, sobald ein neues Objekt einer Klasse erzeugt wird. Hier werden die initial notwendigen Werte gesetzt, Parameter geprüft und Ressourcen allokiert. In der Vector-Klasse beispielsweise werden die Komponenten des Vektors überprüft und in ein Tuple umgewandelt, um Immutabilität zu gewährleisten.

  Beispiel:
  ```python
  def __init__(self, *components):
      # Prüfung und Speicherung der Komponenten
      self._components = tuple(float(c) for c in components)
  ```

- **`__repr__` (offizielle Darstellung):**  
  Diese Methode soll eine möglichst genaue und rekonstruierbare String-Repräsentation des Objekts zurückgeben. Der Rückgabewert sollte so gestaltet sein, dass er, wenn er an `eval()` übergeben würde, ein äquivalentes Objekt erzeugen könnte. Dies ist besonders hilfreich beim Debuggen.

  Beispiel:
  ```python
  def __repr__(self):
      return f"Vector({', '.join(str(c) for c in self._components)})"
  ```

- **`__str__` (benutzerfreundliche Darstellung):**  
  Während `__repr__` vor allem für Entwickler:innen gedacht ist, liefert `__str__` eine leserlichere Darstellung des Objekts, die beim Ausgeben mit `print()` genutzt wird. Es handelt sich hierbei also um eine „schöne“ Version des Objekts.

  Beispiel:
  ```python
  def __str__(self):
      return f"<{', '.join(str(c) for c in self._components)}>"
  ```

Zusammengefasst bildet das Python Data Model mit seinen Dunder-Methoden und Protokollen die Grundlage, um eigene Klassen so zu gestalten, dass sie sich wie eingebaute Datentypen verhalten. Durch die Implementierung von Methoden wie `__init__`, `__repr__` und `__str__` wird sichergestellt, dass Objekte sowohl initialisiert, debuggt als auch benutzerfreundlich dargestellt werden können. Diese Konzepte werden im weiteren Verlauf anhand der Vector-Klasse vertieft und praktisch veranschaulicht.



# 3. Implementierung der Klasseninvarianz und Immutabilität

In objektorientierten Programmen ist es oft wichtig, dass Objekte nach ihrer Erstellung unveränderlich bleiben – sie sollen also einen bestimmten, konsistenten Zustand (Invarianz) behalten. Anhand unserer Vector-Klasse zeigen wir, wie man sowohl die Eingabedaten mittels des Konstruktors validiert als auch Maßnahmen zur Immutabilität ergreift.

## Konstruktor (`__init__`) und Validierung der Eingabedaten

Der Konstruktor `__init__` spielt eine zentrale Rolle bei der Erstellung eines Objekts. Hier erfolgt nicht nur die Initialisierung der benötigten Attribute, sondern auch eine Validierung der Eingabedaten. In unserer Vector-Klasse werden die Komponenten des Vektors auf ihre Gültigkeit geprüft. Dabei stellen wir sicher, dass alle Komponenten reale Zahlen sind, und konvertieren sie in Fließkommazahlen, um eine konsistente Darstellung zu gewährleisten.

Beispielcode:
```python
def __init__(self, *components: Union[numbers.Real, Sequence[numbers.Real]]) -> None:
    """
    Initialisiert den Vektor mit den gegebenen Komponenten. Es wird überprüft,
    ob die übergebenen Werte reale Zahlen sind und anschließend werden diese in ein Tuple konvertiert.
    """
    # Falls nur ein einzelnes Argument als Sequenz übergeben wird, wird diese entpackt.
    if len(components) == 1 and isinstance(components[0], Sequence):
        if all(isinstance(c, numbers.Real) for c in components[0]):
            components = components[0]
    # Validierung: Alle Komponenten müssen reale Zahlen darstellen.
    if not all(isinstance(c, numbers.Real) for c in components):
        raise TypeError("All components must be real numbers (int or float).")
    # Umwandlung der Komponenten in eine Immutable Collection (Tuple)
    self._components = tuple(float(c) for c in components)
```

In diesem Codeausschnitt:
- Wird überprüft, ob die Eingabe bereits in Sequenzform vorliegt und korrekt entpackt.
- Erfolgt eine umfassende Validierung, bei der sichergestellt wird, dass jede Komponente zur Klasse `numbers.Real` gehört.
- Werden die Komponenten in ein Tuple umgewandelt, was uns zum nächsten Punkt führt: der Immutabilität.

## Maßnahmen zur Unveränderlichkeit: Verwendung von Tuples und `__setitem__`

Ein wesentlicher Aspekt der Klasseninvarianz ist, dass einmal gesetzte Werte nicht mehr verändert werden können. Dies erhöht die Sicherheit des Programmcodes, da unvorhergesehene Seiteneffekte vermieden werden. Bei der Vector-Klasse erreichen wir das durch:

1. **Verwendung eines Tuples:**  
   Da Tuples in Python unveränderlich (immutable) sind, gewährleistet die Speicherung der Vektorkomponenten in einem Tuple, dass keine Komponente nach der Initialisierung verändert werden kann.

2. **Überschreiben von `__setitem__`:**  
   Selbst wenn der Zugriff auf einzelne Elemente über `__getitem__` möglich ist, verhindern wir mit einer definierten `__setitem__`-Methode, dass versucht wird, einzelne Komponenten zu modifizieren. Der Versuch, einen Wert zu ändern, führt zu einem Fehler.

Beispielcode:
```python
def __setitem__(self, index: int, value: float) -> None:
    """
    Verhindert die Zuweisung neuer Werte zu bestehenden Komponenten.
    Dies erzwingt die Unveränderlichkeit der Vektor-Objekte.
    
    >>> v = Vector(1.0, 2.0, 3.0)
    >>> v[0] = 5.0
    Traceback (most recent call last):
      ...
    TypeError: Vector objects are immutable and cannot be modified.
    """
    raise TypeError("Vector objects are immutable and cannot be modified.")
```

Mit dieser Methode wird jeder Versuch, über den Indexzugriff Werte zu verändern, sofort mit einem `TypeError` abgefangen. Dadurch bleibt der Zustand eines Vektor-Objekts nach dessen Erstellung konstant.

## Zusammenfassung

- Im Konstruktor `__init__` wird sichergestellt, dass alle Eingabedaten korrekt validiert und in eine Form gebracht werden, die die Invarianz garantiert.
- Die Speicherung der Vektorkomponenten als Tuple verhindert nachträgliche Änderungen.
- Durch das Überschreiben der `__setitem__`-Methode wird aktiv verhindert, dass einzelne Komponenten des Vektors modifiziert werden können.

Diese Maßnahmen zusammen führen zu einer robusten und unveränderlichen Implementierung der Vector-Klasse, die einen konsistenten Zustand während ihrer gesamten Lebensdauer beibehält.





# 4. Container-Protokoll in der Vector-Klasse

Das Container-Protokoll definiert, wie ein Objekt als Sammlung von Elementen behandelt wird. In der Vector-Klasse kommen mehrere Dunder-Methoden zum Einsatz, um den Zugriff und die Iteration über die Vektorkomponenten zu ermöglichen. Im Folgenden betrachten wir die Methoden `__len__`, `__getitem__`, `__iter__` und `__contains__`.

## `__len__`: Bestimmen der Dimensionalität

Die Methode `__len__` gibt die Anzahl der Komponenten des Vektors zurück. Dies entspricht der Dimensionalität des Vektors. Wenn ein Vektor $v$ beispielsweise drei Elemente hat, gilt:  
$$ \text{dim}(v) = 3. $$


Beispielimplementierung:
```python
def __len__(self) -> int:
    """
    Gibt die Anzahl der Komponenten im Vektor zurück.
    
    >>> len(Vector(1.0, 2.0, 3.0))
    3
    >>> len(Vector(1.0))
    1
    """
    return len(self._components)
```

## `__getitem__`: Zugriff auf Einzelkomponenten und Slicing

Mit der Methode `__getitem__` kann auf einzelne Komponenten zugegriffen werden. Dabei wird auch das Slicing unterstützt, sodass man z. B. einen Teilausschnitt des Vektors extrahieren kann. Wird ein Slice übergeben, so wird ein neuer Vector mit den ausgewählten Komponenten erstellt.

Beispielimplementierung:
```python
def __getitem__(self, index: Union[int, slice]) -> Union[float, "Vector"]:
    """
    Ermöglicht den Zugriff auf einzelne Komponenten über einen Index
    oder die Auswahl eines Teilsatzes (Slicing), welcher als neuer Vector zurückgegeben wird.
    
    >>> v = Vector(1.0, 2.0, 3.0)
    >>> v[0]
    1.0
    >>> v[1:3]
    Vector(2.0, 3.0)
    """
    result = self._components[index]
    if isinstance(index, slice):
        return Vector(result)
    return result
```

## `__iter__`: Ermöglichen der Iteration über die Komponenten

Die Methode `__iter__` macht es möglich, über die Bestandteile des Objekts zu iterieren. Dadurch können Vektoren in Schleifen (z. B. in einer `for`-Schleife) verwendet werden. Intern wird ein Iterator über das interne Tuple der Komponenten zurückgegeben.

Beispielimplementierung:
```python
def __iter__(self) -> Iterator[float]:
    """
    Gibt einen Iterator zurück, der über die Komponenten des Vektors iteriert.
    
    >>> v = Vector(1.0, 2.0, 3.0)
    >>> list(v)
    [1.0, 2.0, 3.0]
    """
    return iter(self._components)
```

## `__contains__`: Verwendung des „in“-Operators

Die Methode `__contains__` ermöglicht es, mit dem `in`-Operator zu prüfen, ob ein bestimmter Wert unter den Komponenten des Vektors existiert. Dies vereinfacht die Überprüfung, ob ein bestimmtes Element Teil des Vektors ist.

Beispielimplementierung:
```python
def __contains__(self, item: float) -> bool:
    """
    Überprüft, ob eine gegebene Komponente im Vektor vorhanden ist.
    
    >>> v = Vector(1.0, 2.0, 3.0)
    >>> 2.0 in v
    True
    >>> 4.0 in v
    False
    """
    return item in self._components
```

## Zusammenfassung

- Mit `__len__` erhalten wir die Dimensionalität des Vektors, d.h. die Anzahl seiner Komponenten.
  
- Über `__getitem__` können wir gezielt einzelne Komponenten oder sogar Teilausschnitte (Slicing) des Vektors abrufen.  
  Dabei wird im Falle eines Slices ein neuer Vector erzeugt.

- Die Methode `__iter__` stellt einen Iterator über alle Komponenten bereit, wodurch der Vektor in Schleifen oder anderen Iterationskontexten genutzt werden kann.

- Mit `__contains__` wird das Prüfen, ob ein bestimmter Wert im Vektor existiert, durch den `in`-Operator ermöglicht.

Diese Methoden sorgen zusammen dafür, dass unsere Vector-Klasse sich wie ein standardmäßiger Container verhält, was die Nutzung und Integration in Python-Anwendungen erheblich erleichtert.






# 5. Vergleichs- und Hash-Protokoll

In diesem Abschnitt betrachten wir, wie Objekte der Vector-Klasse untereinander verglichen werden können und wie sie als Schlüssel in Mengen oder Dictionaries verwendet werden. Dafür spielen die Dunder-Methoden `__eq__`, `__lt__` und `__hash__` sowie der Dekorator `@total_ordering` eine zentrale Rolle.

## `__eq__`: Vergleich auf Gleichheit der Komponenten

Die Methode `__eq__` definiert die Gleichheit zweier Vektor-Objekte, indem die jeweiligen Komponenten miteinander verglichen werden. Zwei Vektoren gelten als gleich, wenn sie exakt die gleichen Werte besitzen. Dies ist vor allem im Debugging und beim Vergleich von mathematischen Objekten von großer Bedeutung.

Beispielimplementierung:
```python
def __eq__(self, other: Any) -> bool:
    """
    Überprüft, ob zwei Vektoren gleich sind, d.h. ob alle ihre Komponenten übereinstimmen.

    >>> Vector(1.0, 2.0, 3.0) == Vector(1.0, 2.0, 3.0)
    True
    >>> Vector(1.0, 2.0, 3.0) == Vector(1.0, 2.0, 4.0)
    False
    """
    if not isinstance(other, Vector):
        return NotImplemented
    return self._components == other._components
```

## `__lt__`: Vergleich basierend auf der Vektormagnitude

Die Methode `__lt__` (less-than) ermöglicht den Vergleich zweier Vektoren anhand ihrer Magnitude (Betrag). Die Magnitude eines Vektors $v$ wird durch die Formel

$$
\| v \| = \sqrt{\sum_{i=1}^{n}v_i^2}
$$

berechnet. So kann festgestellt werden, ob ein Vektor "kleiner" als ein anderer ist, indem man ihre Beträge vergleicht.

Beispielimplementierung:
```python
def __lt__(self, other: "Vector") -> bool:
    """
    Vergleicht zwei Vektoren basierend auf ihrer Magnitude.

    >>> Vector(1.0, 2.0, 3.0) < Vector(3.0, 4.0)
    True
    """
    if not isinstance(other, Vector):
        return NotImplemented
    return abs(self) < abs(other)
```

## total_ordering-Dekorator: Automatische Ergänzung der Vergleichsoperatoren

Der Paket `functools.total_ordering` vereinfacht die Implementierung von Vergleichsoperatoren. Wenn mindestens die Methoden `__eq__` und eine der Methoden für die Ordnungsrelationen (z. B. `__lt__`) definiert sind, ergänzt der Dekorator automatisch die weiteren Vergleichsmethoden (`__le__`, `__gt__`, `__ge__`).  
Durch den Einsatz von `@total_ordering` müssen wir also nicht alle Operatoren explizit implementieren, was den Code übersichtlicher und wartungsfreundlicher macht.

Verwendung:
```python
from functools import total_ordering

@total_ordering
class Vector:
    # __eq__ und __lt__ (und damit auch die anderen Vergleichsoperatoren) sind implementiert
    ...
```

## `__hash__`: Verwendung in Mengen und als Dictionary-Schlüssel

Die Methode `__hash__` stellt sicher, dass Vector-Objekte einen konsistenten Hash-Wert besitzen. Damit können Vektoren als Schlüssel in Dictionaries oder Elemente in Mengen verwendet werden. Da in unserer Implementierung die Komponenten als Tuple gespeichert werden – welches von sich aus hashbar ist – lässt sich der Hash-Wert einfach aus diesem Tuple ableiten.

Beispielimplementierung:
```python
def __hash__(self) -> int:
    """
    Gibt einen Hash-Wert zurück, basierend auf den Vektorkomponenten.
    
    >>> hash(Vector(1.0, 2.0, 3.0))
    <eine Ganzzahl>
    """
    return hash(self._components)
```

## Zusammenfassung

- Mit `__eq__` vergleichen wir zwei Vektoren, indem wir überprüfen, ob ihre Komponenten identisch sind.
- Die Methode `__lt__` verwendet die Vektormagnitude, um zwei Vektoren hinsichtlich ihrer "Größe" zu ordnen.
- Der Dekorator `@total_ordering` sorgt dafür, dass aus `__eq__` und `__lt__` automatisch alle weiteren Vergleichsoperationen abgeleitet werden.
- `__hash__` ermöglicht die Benutzung von Vektoren als Schlüssel in Dictionaries und als Elemente in Mengen, indem ein konsistenter Hash-Wert basierend auf den unveränderlichen Komponenten erzeugt wird.

Diese Mechanismen stellen sicher, dass die Vector-Klasse nicht nur mathematische Operationen unterstützt, sondern auch vollständig in die Python-Datenmodelle integriert ist.




# 6. Numerische bzw. Arithmetische Operationen

Die Vector-Klasse unterstützt verschiedene arithmetische Operationen, die mathematisch sinnvolle Vektoroperationen ermöglichen. In diesem Abschnitt werden wir die Implementierung von Addition, Subtraktion, Multiplikation, Division, Dot-Produkt sowie Negation und Identitätsoperation betrachten.

## `__add__` und `__sub__`: Vektoraddition und -subtraktion

Mit der Methode `__add__` wird die Addition zweier Vektoren realisiert. Dabei erfolgt die Addition komponentenweise. Analog dazu wird in der Methode `__sub__` die Subtraktion zweier Vektoren implementiert. Wichtig ist, dass beide Vektoren dieselbe Anzahl an Komponenten (d.h. dieselbe Dimensionalität) haben.

Beispielimplementierung:
```python
def __add__(self, other: "Vector") -> "Vector":
    """
    Addiert zwei Vektoren komponentenweise.

    >>> Vector(1.0, 2.0, 3.0) + Vector(4.0, 5.0, 6.0)
    Vector(5.0, 7.0, 9.0)
    """
    if not isinstance(other, Vector):
        return NotImplemented
    if len(self) != len(other):
        raise ValueError("Vectors must have the same dimensionality for addition.")
    return Vector(*(a + b for a, b in zip(self, other)))

def __sub__(self, other: "Vector") -> "Vector":
    """
    Subtrahiert zwei Vektoren komponentenweise.

    >>> Vector(4.0, 5.0, 6.0) - Vector(1.0, 2.0, 3.0)
    Vector(3.0, 3.0, 3.0)
    """
    if not isinstance(other, Vector):
        return NotImplemented
    if len(self) != len(other):
        raise ValueError("Vectors must have the same dimensionality for subtraction.")
    return Vector(*(a - b for a, b in zip(self, other)))
```

## `__mul__` und `__rmul__`: Skalare Multiplikation und Element-weises Produkt

Die Methode `__mul__` ermöglicht zwei unterschiedliche Arten der Multiplikation:
- **Skalare Multiplikation:** Wenn der Operand eine reelle Zahl ist, wird jeder Vektorkomponente der Skalar multipliziert.
- **Element-weises Produkt:** Wenn der Operand ebenfalls ein Vector ist, erfolgt eine komponentenweise Multiplikation.

Darüber hinaus sorgt `__rmul__` dafür, dass die Multiplikation auch dann funktioniert, wenn die Zahl (Skalar) links vom Vektor steht.

Beispielimplementierung:
```python
def __mul__(self, other: Union[numbers.Real, "Vector"]) -> Union["Vector", float]:
    """
    Multipliziert einen Vektor entweder mit einem Skalar (Skalare Multiplikation)
    oder führt eine Element-weise Multiplikation mit einem anderen Vektor durch.

    >>> Vector(1.0, 2.0, 3.0) * 2
    Vector(2.0, 4.0, 6.0)
    >>> Vector(1.0, 2.0, 3.0) * Vector(4.0, 5.0, 6.0)
    Vector(4.0, 10.0, 18.0)
    """
    if isinstance(other, numbers.Real):
        return Vector(*(c * other for c in self._components))
    elif isinstance(other, Vector):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensionality for element-wise multiplication.")
        return Vector(*(a * b for a, b in zip(self, other)))
    else:
        return NotImplemented

def __rmul__(self, other: Union[numbers.Real, "Vector"]) -> Union["Vector", float]:
    """
    Ermöglicht die Multiplikation von links, z.B.:
    
    >>> 2 * Vector(1.0, 2.0, 3.0)
    Vector(2.0, 4.0, 6.0)
    """
    return self * other
```

## `__truediv__`: Division eines Vektors durch einen Skalar

Die Methode `__truediv__` definiert die Division eines Vektors durch einen reellen Skalar. Hierbei wird jede Komponente des Vektors durch den Skalar geteilt. Ein Versuch, durch Null zu teilen, führt zu einem Fehler.

Beispielimplementierung:
```python
def __truediv__(self, scalar: numbers.Real) -> "Vector":
    """
    Dividiert jeden Wert des Vektors durch den angegebenen Skalar.

    >>> Vector(2.0, 4.0, 6.0) / 2
    Vector(1.0, 2.0, 3.0)
    """
    if not isinstance(scalar, numbers.Real):
        return NotImplemented
    if scalar == 0:
        raise ValueError("Division by zero is not allowed.")
    return Vector(*(c / scalar for c in self._components))
```

## `__matmul__`: Berechnung des Skalarprodukts (Dot Product)

Die Methode `__matmul__` wird verwendet, um das Skalarprodukt (Dot Product) zweier Vektoren zu berechnen. Dabei werden die entsprechenden Komponenten multipliziert und die Produkte aufsummiert. Auch hier müssen die Vektoren dieselbe Anzahl an Komponenten haben.

Beispielimplementierung:
```python
def __matmul__(self, other: "Vector") -> float:
    """
    Berechnet das Skalarprodukt (Dot Product) zweier Vektoren.

    >>> Vector(1.0, 2.0, 3.0) @ Vector(4.0, 5.0, 6.0)
    32.0
    """
    if not isinstance(other, Vector):
        return NotImplemented
    if len(self) != len(other):
        raise ValueError("Vectors must have the same dimensionality for dot product.")
    return sum(a * b for a, b in zip(self, other))
```

## `__neg__` und `__pos__`: Negation und Identitätsoperation

Mit `__neg__` wird der Vektor negiert, d.h. jede Komponente wird mit -1 multipliziert. Dagegen gibt `__pos__` den Vektor selbst zurück (Identitätsoperation). Diese Methoden ermöglichen eine elegante Anwendung der unären Operatoren `-` und `+`.

Beispielimplementierung:
```python
def __neg__(self) -> "Vector":
    """
    Negiert den Vektor, indem alle Komponenten mit -1 multipliziert werden.

    >>> -Vector(1.0, 2.0, 3.0)
    Vector(-1.0, -2.0, -3.0)
    """
    return Vector(*(-c for c in self._components))

def __pos__(self) -> "Vector":
    """
    Gibt den Vektor unverändert zurück (Identitätsoperation).

    >>> +Vector(1.0, 2.0, 3.0)
    Vector(1.0, 2.0, 3.0)
    """
    return Vector(*self._components)
```

## Zusammenfassung

- Mit `__add__` und `__sub__` werden Vektoren komponentenweise addiert bzw. subtrahiert.
- Die Methoden `__mul__` und `__rmul__` ermöglichen sowohl die skalare Multiplikation als auch das elementweise Produkt zwischen Vektoren.
- `__truediv__` teilt jede Komponente eines Vektors durch einen Skalar.
- Mit `__matmul__` wird das Skalarprodukt (Dot Product) zweier Vektoren berechnet.
- `__neg__` negiert den Vektor, während `__pos__` ihn unverändert zurückgibt.

Diese Operationen erweitern die Funktionalität der Vector-Klasse und stellen sicher, dass mathematische Berechnungen auf intuitive und pythonische Weise durchgeführt werden können.









# 7. Weitere spezielle Methoden und Protokolle

Neben den grundlegenden arithmetischen Operationen bietet die Vector-Klasse noch weitere Methoden, die zusätzliche Funktionalitäten und Verhaltensweisen definieren:

## `__abs__`: Berechnung der Vektormagnitude

Die Methode `__abs__` berechnet die euklidische Norm (Magnitude) eines Vektors. Für einen Vektor $$v = (v_1, v_2, ..., v_n)$$ gilt:  
$$\| v \| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}.$$

Beispielimplementierung:
```python
def __abs__(self) -> float:
    """
    Berechnet die Magnitude (Betrag) des Vektors.

    >>> abs(Vector(3.0, 4.0))
    5.0
    >>> abs(Vector(1.0, 2.0, 2.0))
    3.0
    """
    return math.sqrt(sum(c ** 2 for c in self._components))
```

## `__bool__`: Bestimmung der Wahrheitswerteigenschaft

Die `__bool__`-Methode legt fest, ob ein Vektor als "wahr" oder "falsch" bewertet wird, wenn z. B. in Bedingungen geprüft. In der Vector-Klasse wird häufig definiert, dass ein Vektor dann als `False` gilt, wenn alle Komponenten den Wert 0 haben.

Beispielimplementierung:
```python
def __bool__(self) -> bool:
    """
    Bestimmt den Wahrheitswert des Vektors.

    >>> bool(Vector(1.0, 2.0, 3.0))
    True
    >>> bool(Vector(0.0, 0.0, 0.0))
    False
    """
    return any(c != 0 for c in self._components)
```

## Zusatzmethoden

Neben den standardisierten Dunder-Methoden bietet die Vector-Klasse auch spezielle Funktionen, die häufig in mathematischen Berechnungen benötigt werden:

### normalize

Die Methode `normalize` wandelt den Vektor in einen Einheitsvektor um, d. h. er wird auf die Länge 1 normiert.  
Formel:  
$$ u = \frac{v}{\|v\|} $$  
Dabei muss beachtet werden, dass die Normalisierung eines Nullvektors nicht durchgeführt werden kann.

Beispielimplementierung:
```python
def normalize(self) -> "Vector":
    """
    Normiert den Vektor zu einem Einheitsvektor.

    >>> Vector(3.0, 4.0).normalize()
    Vector(0.6, 0.8)
    """
    magnitude = abs(self)
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return self / magnitude
```

### distance_to

`distance_to` berechnet die euklidische Entfernung zwischen zwei Vektoren. Dies entspricht der Magnitude der Differenz beider Vektoren.  

Beispielimplementierung:
```python
def distance_to(self, other: "Vector") -> float:
    """
    Berechnet den euklidischen Abstand zwischen diesem und einem anderen Vektor.

    >>> Vector(1.0, 2.0, 3.0).distance_to(Vector(4.0, 5.0, 6.0))
    5.196152422706632
    """
    if not isinstance(other, Vector):
        return NotImplemented
    if len(self) != len(other):
        raise ValueError("Vectors must have the same dimensionality for distance calculation.")
    return abs(self - other)
```

### angle_to

Mit der Methode `angle_to` wird der Winkel (in Radiant) zwischen zwei Vektoren berechnet.  
Formel:  
$$ \cos(\theta) = \frac{v \cdot w}{\|v\|\|w\|} $$

Beispielimplementierung:
```python
def angle_to(self, other: "Vector") -> float:
    """
    Berechnet den Winkel zwischen diesem und einem anderen Vektor in Radianten.

    >>> from math import degrees
    >>> angle = Vector(1.0, 0.0).angle_to(Vector(0.0, 1.0))
    >>> degrees(angle)
    90.0
    """
    if not isinstance(other, Vector):
        return NotImplemented
    if len(self) != len(other):
        raise ValueError("Vectors must have the same dimensionality for angle calculation.")

    dot_product = self @ other
    magnitude_self = abs(self)
    magnitude_other = abs(other)
    
    if magnitude_self == 0 or magnitude_other == 0:
        raise ValueError("Cannot calculate angle with a zero vector.")
    
    # Berechnung und Clamping des Cosinuswerts
    cos_theta = dot_product / (magnitude_self * magnitude_other)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    return math.acos(cos_theta)
```

# 8. Fehlermanagement und Sonderfälle

Um robusten und vorhersehbaren Code zu schreiben, ist es unerlässlich, auch Fehlerbedingungen und Sonderfälle zu behandeln. Dies betrifft insbesondere:

## Behandlung von Dimensionsmismatches

Viele arithmetische Operationen (z. B. Addition, Subtraktion, Dot-Produkt) setzen voraus, dass zwei Vektoren dieselbe Anzahl an Komponenten haben. Wird dies nicht erfüllt, wird ein `ValueError` ausgelöst:

Beispiel bei der Vektoraddition:
```python
def __add__(self, other: "Vector") -> "Vector":
    if not isinstance(other, Vector):
        return NotImplemented
    if len(self) != len(other):
        raise ValueError("Vectors must have the same dimensionality for addition.")
    return Vector(*(a + b for a, b in zip(self, other)))
```

## Fehlerbehandlung bei unveränderlichen Elementen

Da die Vector-Klasse als immutable entworfen ist, ist es wichtig, Manipulationsversuche zu unterbinden. Versucht man über den Indexzugriff einen Wert zu ändern, wird ein `TypeError` ausgelöst:
```python
def __setitem__(self, index: int, value: float) -> None:
    raise TypeError("Vector objects are immutable and cannot be modified.")
```

## Umgang mit Sonderfällen

Weitere Sonderfälle, die explizit behandelt werden, sind:
- **Division durch Null:**  
  Bei der Division eines Vektors durch einen Skalar wird überprüft, ob der Skalar gleich 0 ist, um eine Division durch Null zu vermeiden:
  ```python
  def __truediv__(self, scalar: numbers.Real) -> "Vector":
      if not isinstance(scalar, numbers.Real):
          return NotImplemented
      if scalar == 0:
          raise ValueError("Division by zero is not allowed.")
      return Vector(*(c / scalar for c in self._components))
  ```
- **Normalisierung des Nullvektors:**  
  Versuch man, den Nullvektor zu normieren, wird das durch einen `ValueError` verhindert:
  ```python
  def normalize(self) -> "Vector":
      magnitude = abs(self)
      if magnitude == 0:
          raise ValueError("Cannot normalize a zero vector.")
      return self / magnitude
  ```

# 9. Zusammenfassung und Ausblick

## Wiederholung der wesentlichen Aspekte des Python Data Model

In dieser Einheit haben wir mithilfe der Vector-Klasse einen umfassenden Einblick in das Python Data Model gewonnen. Wesentliche Punkte waren:
- **Dunder-Methoden:**  
  Spezielle Methoden wie `__init__`, `__repr__`, `__str__`, `__eq__`, `__lt__` und weitere ermöglichen es, benutzerdefinierte Klassen in die Sprache zu integrieren.
- **Container- und Iterator-Protokolle:**  
  Mit `__len__`, `__getitem__`, `__iter__` und `__contains__` verhält sich ein Objekt wie ein Container.
- **Arithmetische Operationen:**  
  Durch Methoden wie `__add__`, `__sub__`, `__mul__`, `__truediv__` und `__matmul__` werden mathematische Operationen intuitiv unterstützt.
- **Vergleichs- und Hash-Protokoll:**  
  Mit `__eq__`, `__lt__`, und dem Einsatz des `@total_ordering`-Dekorators sowie `__hash__` kann der Vektor sowohl verglichen als auch in Mengen und Dictionaries verwendet werden.
- **Zusatzmethoden:**  
  Spezielle Funktionen wie `normalize`, `distance_to` und `angle_to` erweitern den Funktionsumfang der Klasse und decken viele mathematische Anwendungen ab.

## Diskussion: Pythonic Design durch die implementierten Protokolle

Durch die konsequente Implementierung der Dunder-Methoden wird die Vector-Klasse nahtlos in den Python-Sprachraum integriert und verhält sich wie ein eingebauter Datentyp:
- **Intuitive Nutzung:**  
  Benutzer können Vektoren addieren, subtrahieren, skalieren und miteinander vergleichen, ohne sich um implizite Konvertierungen oder spezielle Methodenaufrufe kümmern zu müssen.
- **Erweiterbarkeit:**  
  Die strukturierte Nutzung des Python Data Model ermöglicht es, die Klasse einfach zu erweitern oder in komplexe mathematische und datenorientierte Systeme zu integrieren.
- **Lesbarkeit und Wartbarkeit:**  
  Der Einsatz von Standards wie `__repr__` und `__str__` verbessert das Debugging und die Lesbarkeit, während Fehlerfälle gezielt abgefangen werden.

## Weiterführende Themen und mögliche Erweiterungen

Im Anschluss an diese Unterrichtseinheit bieten sich zahlreiche Erweiterungen an, beispielsweise:
- **Erweiterte Lineare Algebra:**  
  Implementierung weiterer Operationen wie Kreuzprodukt (für 3D-Vektoren) oder der Lösen linearer Gleichungssysteme.
- **Integration mit NumPy:**  
  Eine nahtlose Umwandlung in NumPy-Arrays (mittels der Methode `__array__`) für eine effiziente numerische Berechnung.
- **Erweiterte Validierung und Fehlerbehandlung:**  
  Dynamische Typüberprüfungen und optimierte Algorithmen zur Verbesserung der Robustheit und Leistung.
- **Interaktivität und Visualisierung:**  
  Anwendungen im Bereich der Datenvisualisierung oder interaktive Rechenumgebungen wie Jupyter Notebooks.

Diese Ansätze zeigen, wie das Verständnis des Python Data Models nicht nur zur Erstellung „pythonic“ gestalteter Klassen beiträgt, sondern auch den Grundstein für komplexe und erweiterbare Anwendungen legt.