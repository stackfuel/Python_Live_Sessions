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
# # Decorators in Python
#

# %% [markdown]
# ## Vorbemerkung `*args` und `**kwargs`
# `*args` und `**kwargs` sind spezielle Syntaxelemente in Python, die es ermöglichen, eine variable Anzahl von Argumenten an eine Funktion zu übergeben.
#
# ### `*args` - Variable Positionale Argumente
# `*args` ermöglicht es, eine beliebige Anzahl von positionalen Argumenten an eine Funktion zu übergeben. Diese Argumente werden als Tupel in der Funktion verfügbar.
#

# %%
def sum_all(*args):
    """Summiert alle übergebenen Zahlen"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all())               # 0


# %% [markdown]
# ### `**kwargs**` - Variable Schlüsselwortargumente
# `**kwargs` ermöglicht es, eine beliebige Anzahl von benannten Argumenten (Schlüsselwortargumenten) an eine Funktion zu übergeben. Diese Argumente werden als Dictionary in der Funktion verfügbar.

# %%
def print_info(**kwargs):
    """Gibt alle Schlüssel-Wert-Paare aus"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Max", age=25, city="Berlin")
# name: Max
# age: 25
# city: Berlin

# %%
def flexible_function(required_arg, *args, **kwargs):
    """Demonstration einer flexiblen Funktionssignatur"""
    print(f"Pflichtargument: {required_arg}")
    
    if args:
        print(f"Zusätzliche Argumente: {args}")
    
    if kwargs:
        print("Schlüsselwort-Argumente:")
        for key, value in kwargs.items():
            print(f"  {key} = {value}")

# Verschiedene Aufrufe
flexible_function("Hallo")
flexible_function("Hallo", 1, 2, 3)
flexible_function("Hallo", 1, 2, name="Anna", age=30)


# %% [markdown]
# ## Funktionen als First-Class Citizens
# In Python sind Funktionen Objekte - sie können wie jedes andere Objekt behandelt werden. Das bedeutet:
#
# - Funktionen können Variablen zugewiesen werden
# - Funktionen können als Parameter an andere Funktionen übergeben werden
# - Funktionen können von anderen Funktionen zurückgegeben werden
# - Funktionen haben Attribute und Methoden

# %%
def greet(name):
    """Eine einfache Begrüßungsfunktion"""
    return f"Hallo, {name}!"

# Funktionen haben Attribute
print(greet.__name__)        # greet
print(greet.__doc__)         # Eine einfache Begrüßungsfunktion
print(type(greet))           # <class 'function'>

# Funktionen können Variablen zugewiesen werden
say_hello = greet
print(say_hello("Anna"))     # Hallo, Anna!

# Funktionen können in Listen/Dictionaries gespeichert werden
functions = [greet, say_hello]
func_dict = {"greeting": greet}

# %%
# Funktionen haben eie __call__-Methode die den Aufruf ermöglicht
greet.__call__("Alice")  # Aufruf der Funktion mit __call__


# %%
# Wir können eine eigene Classe definieren, die wie eine Funktion aufgerufen werden kann
class CallableClass:
    def __call__(self, name):
        return f"Hallo aus der Klasse, {name}!"
    
callable_object = CallableClass()
callable_object("Bob")  # Aufruf der Klasse wie eine Funktion


# %% [markdown]
# ### Higher order functions und Closures
#
# Eine **higher order function** ist eine Funktion, die mindestens eine der folgenden Eigenschaften hat:
# - Sie nimmt eine oder mehrere Funktionen als Argumente.
# - Sie gibt eine Funktion zurück.
#
# Typische Beispiele für Higher Order Functions sind `map()`, `filter()` und `reduce()`.
#

# %%
def add_5(x):
    return x + 5

def apply(func, x):
    return func(x)

print(apply(add_5, 10))


# %%
def square(x):
    return x * x

def negate(x):
    return -x

def compose(func1, func2):
    """Kombiniert zwei Funktionen, indem die Ausgabe von func1 als Eingabe für func2 verwendet wird."""
    def composed_function(x):
        return func2(func1(x))
    
    return composed_function

# Beispiel für die Verwendung von compose
composed = compose(square, negate)
print(composed(3))  # Ausgabe: -9, da (3 * 3) = 9 und dann negiert wird


# %% [markdown]
# Ein **Closure** ist eine Funktion, die auf Variablen aus ihrem umgebenden Kontext zugreifen kann, auch wenn dieser Kontext nicht mehr aktiv ist. Closures werden häufig verwendet, um Zustände zu kapseln und Funktionen zu erstellen, die sich an vorherige Aufrufe erinnern.
#

# %%
def create_add_n(n):
    def add_n(x):
        return x + n
    return add_n

add_5 = create_add_n(5)

print(add_5(10))


# %% [markdown]
# ## Decorators
# Ein **Decorator** ist ein Design-Pattern, bei dem eine Funktion eine andere Funktion modifiziert oder erweitert, ohne deren Quellcode zu ändern. Decorators werden häufig verwendet, um Funktionen zu protokollieren, zu überwachen oder zusätzliche Funktionalitäten hinzuzufügen.

# %%
def is_prime(n):
    '''A simple function to check if a number is prime.'''
    if n <= 1:
        return False
    return not any(n % i == 0 for i in range(2, n))

def log_function(func):
    def wrapper(n):
        print(f'Calling {func.__name__} with parameter {n}')
        return func(n)
    return wrapper



# %%
logged_is_prime = log_function(is_prime)

# call pure function
print(is_prime(17))

print("-"*20)
# call logged function
print(logged_is_prime(17))
    

# %% [markdown]
# Unser Decorator funktioniert gerade nur dann, wenn die zu dekorierende Funktion genau ein Argument erwartet.
# Wir können das Problem lösen, indem wir *args und **kwargs in der inneren Funktion verwenden.
# Das bedeutet, dass die dekorierte Funktion beliebig viele Argumente akzeptieren kann. Hier ist der aktualisierte Code:
#

# %%
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with parameters {args} and {kwargs}')
        return func(*args, **kwargs)
    return wrapper


# %%
is_prime_logged = log_function(is_prime)

print(is_prime_logged(17))


# %%
def filter_primes(*numbers):
    return [n for n in numbers if is_prime(n)]

print(filter_primes(4, 6, 9, 17, 18, 19, 22, 23))

print("-"*20)	    

filter_primes_logged = log_function(filter_primes)

print(filter_primes_logged(4, 6, 9, 17, 18, 19, 22, 23))


# %% [markdown]
# Python bietet uns eine weitere Möglichkeit an um Funktionen direkt bei der Definition zu dekorieren.
# Hierfür wird das @-Zeichen verwendet. Anstatt
#
# ```python
# decorated_function = decorator_function(original_function)
# ```
#
# Zu schreiben können wir auch einfach
# ```python
# @decorator_function
# def original_function():
#     pass
# ```
# bei der Funktionsdefinition Verwenden.

# %% [markdown]
# Hier nochmal beide Funktionen zusammen:

# %%
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with parameter {args} and {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def is_prime(n):
    '''A simple function to check if a number is prime.'''
    if n <= 1:
        return False
    return not any(n % i == 0 for i in range(2, n))


# %%
print(is_prime(17))

# %% [markdown]
# Da unsere Funktion durch diese syntax überschrieben wird ergeibt sich ein Problem:
# Möchten wir eigenschaften der Funktion abfrage, wie den Namen oder den Docstring, werden uns nun die Eigenschaften unserer wrapper Funktion zurückgegeben.

# %%
print(is_prime.__name__)
print(is_prime.__doc__)

# %% [markdown]
# Um dieses Problem zu beheben, können wir direkt einen decorator aus dem functools Modul aus der Standard Bibliothek von Python benutzen.

# %%
from functools import wraps

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling func with parameter {args} and {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def is_prime(n):
    '''A simple function to check if a number is prime.'''
    if n <= 1:
        return False
    return not any(n % i == 0 for i in range(2, n))


# %%
print(is_prime.__name__)
print(is_prime.__doc__)

# %%
from functools import update_wrapper

class CountCalls:
    """Zählt Funktionsaufrufe"""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        update_wrapper(self, func) # damit die Metadaten der Funktion erhalten bleiben
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
    
    def get_count(self):
        return self.count

@CountCalls
def fibonacci(n):
    """Berechnet die n-te Fibonacci-Zahl"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Testen
print(fibonacci(5))  # 5
print(f"Gesamtanzahl Aufrufe: {fibonacci.get_count()}")


# %% [markdown]
# # Property decorator

# %%
# demonstrate the property decorator

class B():
    
    def __init__(self, x):
        self.x = x
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be positive")
        self._x = value
        
        
b = B(5)
print(b.x)
b.x = 10
print(b.x)

b.x = -1



# %%
import math

class Circle:
    """Repräsentiert einen Kreis"""
    
    def __init__(self, radius):
        self._radius = radius  # Privates Attribut
    
    @property
    def radius(self):
        """Getter für den Radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter für den Radius mit Validierung"""
        if value <= 0:
            raise ValueError("Radius muss positiv sein")
        self._radius = value
    
    @property
    def area(self):
        """Berechnet die Fläche (read-only Property)"""
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """Berechnet den Umfang (read-only Property)"""
        return 2 * math.pi * self._radius

# Verwendung
circle = Circle(5)
print(f"Radius: {circle.radius}")           # 5
print(f"Fläche: {circle.area:.2f}")         # 78.54
print(f"Umfang: {circle.circumference:.2f}") # 31.42

# Radius ändern
circle.radius = 3
print(f"Neue Fläche: {circle.area:.2f}")    # 28.27

# Validierung testen
try:
    circle.radius = -1  # Fehler!
except ValueError as e:
    print(f"Fehler: {e}")

# %%
from datetime import date

class Person:
    def __init__(self, birth_date, death_date=None):
        self._birth_date = birth_date
        self._death_date = death_date

    @property
    def birth_date(self):
        """Get the birth date of the person."""
        return self._birth_date

    @property
    def death_date(self):
        """Get the death date of the person, if applicable."""
        return self._death_date

    @death_date.setter
    def death_date(self, value):
        """Set the death date of the person."""
        if value < self._birth_date:
            raise ValueError("Death date cannot be before birth date")
        self._death_date = value

    @property
    def age(self):
        """Calculate the age of the person based on birth and death date."""
        end_date = self._death_date if self._death_date else date.today()
        return end_date.year - self._birth_date.year - (
            (end_date.month, end_date.day) < (self._birth_date.month, self._birth_date.day)
        )

# Example usage
person = Person(date(1990, 5, 15))
print(f"Birth Date: {person.birth_date}")
print(f"Current Age: {person.age}")

# Set a death date
person.death_date = date(2020, 5, 14)
print(f"Death Date: {person.death_date}")
print(f"Age at Death: {person.age}")

person.death_date = date(1980, 5, 14)


# %% [markdown]
# # Classmethod und Staticmethod

# %%
class A:
    
    # method
    def m1():
        print("m1 of A called")
    
    # instance method
    def m2(self):
        print("m2 of A called with self", self)
        
    @staticmethod
    def m3():
        print("m3 of A called")
        
    @classmethod
    def m4(cls):
        print("m4 of A called with cls", cls)
        
        
a = A()


# a.m1()
a.m2()
a.m3()
a.m4()

print("-"*20)

A.m1()
A.m2(a)
A.m3()
A.m4()

# %% [markdown]
# # lru_cache

# %%
from functools import lru_cache

# Define a Fibonacci function with caching
@lru_cache(maxsize=None)  # maxsize=None means unlimited cache size
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(10))  # Output: 55
print(fibonacci(20))  # Output: 6765

# Calling fibonacci(10) again will use the cached result
print(fibonacci(10))  # Output: 55 (retrieved from cache)


# %% [markdown]
# # Data Class

# %%
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

# Creating an instance of Point
point1 = Point(1.5, 2.5)
print(point1)  # Output: Point(x=1.5, y=2.5)

# Accessing fields
print(point1.x)  # Output: 1.5
print(point1.y)  # Output: 2.5

# Comparing instances
point2 = Point(1.5, 2.5)
print(point1 == point2)  # Output: True

# Modifying fields
point1.x = 3.0
print(point1)  # Output: Point(x=3.0, y=2.5)

