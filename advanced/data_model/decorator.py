from time import perf_counter, sleep
from random import random
from functools import wraps
 

def decorator(f):
    
    @wraps(f)
    def wrapper(*args, **kwargs):
        before = perf_counter()
    
        result = f(*args, **kwargs)
    
        after = perf_counter()
        print(after - before)
        
        return result
    
    return wrapper

@decorator
def f(a):
    print(f"f: {a}")
    sleep(random())

@decorator
def h(a):
    print(f"h: {a}")
    sleep(random())


# f = decorator(f)
# h = decorator(h)


f(1)
f(2)
f(3)
f(4)
f(5)

h(1)
h(2)
h(3)
h(4)
h(5)


