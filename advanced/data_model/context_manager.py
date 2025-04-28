from contextlib import contextmanager


class C:
    def __enter__(self):
        print("enter")
        return self
        
    def __exit__(self, *args):
        print("exit")
        print(*args)
        
    def __repr__(self):
        return "C()"

@contextmanager
def cm():
    try:
        print("enter")
        yield
    finally:
        print("exit")
        
        
with cm() as c:
    print(c)
    raise RuntimeError
    
    

