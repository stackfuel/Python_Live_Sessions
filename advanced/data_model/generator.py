from itertools import chain
from copy import copy

class Range:
    def __init__(self, start, step, stop, precision=6):
        self._precision = precision
        self._start = start
        self._step = step
        self._stop = stop
        
    
    def __iter__(self):
        new = copy(self)
        new.i = self._start - self._step
        return new
    
    def __next__(self):
        if self.i == self._start:
            
            self.i += self._step
            return round(self.i, self._precision)
        
        if self.i <= round(self._stop - self._step, self._precision): 
            self.i += self._step
            return round(self.i, self._precision)
        
        raise StopIteration
    
    def __add__(self, other):
        return chain(self, other)

    def __radd__(self, other):
        if isinstance(other, Range):
            return chain(self, other)
        if other is None:
            return self
            
        raise TypeError(f"Unsupported operand type(s) for +: '{type(other).__name__}' and 'Range'")
    
    def __mul__(self, other: int):
        if isinstance(other, int):
            return sum([self]*other, start=None)
        raise TypeError(f"Unsupported operand type(s) for *: 'Range' and '{type(other).__name__}'")
        
r1 = Range(0, 0.2, 2)
r2 = Range(0, 0.5, 2)
r3 = Range(0, 0.1, 2)
    
for i in r2*5:
    print(i)
    
    
    
