# 2D Vektoren Cheat Sheet

## Beispielvektoren
$\vec{u} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}, \quad \vec{v} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}, \quad \vec{w} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$

## Definition
Ein 2D-Vektor ist ein Tupel aus zwei Komponenten:
$\vec{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$
wobei $v_1, v_2 \in \mathbb{R}$.

## Arithmetik

| Operation | Formel | Python Dunder |
|-----------|--------|---------------|
| **Addition** | $\vec{u} + \vec{v} = \begin{pmatrix} u_1 + v_1 \\ u_2 + v_2 \end{pmatrix}$ | `__add__`, `__radd__` |
| **Subtraktion** | $\vec{u} - \vec{v} = \begin{pmatrix} u_1 - v_1 \\ u_2 - v_2 \end{pmatrix}$ | `__sub__`, `__rsub__` |
| **Skalarmultiplikation** | $k \cdot \vec{v} = \begin{pmatrix} k \cdot v_1 \\ k \cdot v_2 \end{pmatrix}$ | `__mul__`, `__rmul__` |
| **Komponentenweise Multiplikation** | $\vec{u} \odot \vec{v} = \begin{pmatrix} u_1 \cdot v_1 \\ u_2 \cdot v_2 \end{pmatrix}$ | `__mul__` |

## Vektoroperationen (Vector Operations)

| Operation | Formel | Python Dunder |
|-----------|--------|---------------|
| **Skalarprodukt (Dot Product)** | $\vec{u} \cdot \vec{v} = u_1 \cdot v_1 + u_2 \cdot v_2$ | `__matmul__` |
| **Norm (Magnitude)** | $\|\vec{v}\| = \sqrt{v_1^2 + v_2^2}$ | `__abs__` |
| **Normalisierung (Normalization)** | $\hat{\vec{u}} = \frac{\vec{u}}{\|\vec{u}\|} = \frac{1}{\|\vec{u}\|} \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}$ | - |
| **Winkel (Angle)** | $\theta = \arccos\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \cdot \|\vec{v}\|}\right)$ | - |

## Wichtige Eigenschaften (Important Properties)

| Eigenschaft | Bedeutung |
|-------------|-----------|
| **Nullvektor (Zero Vector)** | $\vec{0} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ |
| **Einheitsvektoren (Unit Vectors)** | $\vec{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ |
| **Orthogonalität (Orthogonality)** | $\vec{u} \perp \vec{v} \Leftrightarrow \vec{u} \cdot \vec{v} = 0$ |
| **Parallelität (Parallelism)** | $\vec{u} \parallel \vec{v} \Leftrightarrow \vec{u} = k \cdot \vec{v}$ für ein $k \in \mathbb{R}$ |
| **Normierter Vektor (Normalized Vector)** | $\|\hat{\vec{u}}\| = 1$ |

## Weitere Python Dunder Methods (Additional Python Dunder Methods)

| Method | Zweck (Purpose) |
|--------|-----------------|
| `__init__` | Konstruktor (Constructor) |
| `__repr__` | String-Repräsentation (String Representation) |
| `__str__` | Benutzerfreundliche Ausgabe (User-friendly Output) |
| `__eq__` | Gleichheit (Equality) |
| `__ne__` | Ungleichheit (Inequality) |
| `__neg__` | Negation (Negation) |
| `__pos__` | Positiv (Positive) |
| `__len__` | Länge/Dimension (Length/Dimension) |
| `__getitem__` | Index-Zugriff (Index Access) |
| `__setitem__` | Index-Zuweisung (Index Assignment) |
| `__iter__` | Iteration (Iteration) |