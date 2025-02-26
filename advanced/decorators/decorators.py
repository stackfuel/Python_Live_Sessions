import time

from functools import wraps
from functools import lru_cache


def time_tracker(func):
    
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(end - start)
        
        return result
    
    return wrap


@lru_cache
def fib_rec(n):
    if n in (0, 1):
        return n
    return fib_rec(n-1) + fib_rec(n-2)

@time_tracker
def fib_2(n):
    """Recursive function to return the nth Fibonacci number."""
    return fib_rec(n)

@time_tracker
def fib_1(n):
    """Iterative function to return the nth Fibonacci number."""
    if n in (0, 1):
        return n
    a, b = 0, 1
    
    for _ in range(0, n-1):
        a, b = b, a+b
    return b

print(fib_1(30))

print(fib_2(50))
