# Objektorientierung in Python

class Fraction:
    
    def __init__(self, numerator, denominator):
        """Create a fraction from numerator and denominator."""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator


    def __add__(self, other):
        """Add two fractions."""
        numerator1, denominator1 = self.numerator, self.denominator
        numerator2, denominator2 = other.numerator, other.denominator
        numerator = numerator1 * denominator2 + numerator2 * denominator1
        denominator = denominator1 * denominator2
        return Fraction(numerator, denominator)
    
    def add(fraction1, fraction2, simplify=True):
        """Add two fractions."""
        numerator1, denominator1 = fraction1.numerator, fraction1.denominator
        numerator2, denominator2 = fraction2.numerator, fraction2.denominator
        numerator = numerator1 * denominator2 + numerator2 * denominator1
        denominator = denominator1 * denominator2
        if simplify:
            return Fraction(numerator, denominator).simplify()
        return Fraction(numerator, denominator)

    def __sub__(fraction1, fraction2):
        """Subtract two fractions."""
        numerator1, denominator1 = fraction1.numerator, fraction1.denominator
        numerator2, denominator2 = fraction2.numerator, fraction2.denominator
        numerator = numerator1 * denominator2 - numerator2 * denominator1
        denominator = denominator1 * denominator2
        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        """Multiply two fractions."""
        numerator1, denominator1 = self.numerator, self.denominator
        numerator2, denominator2 = other.numerator, other.denominator
        numerator = numerator1 * numerator2
        denominator = denominator1 * denominator2
        return Fraction(numerator, denominator)
    
    def __truediv__(self, other):
        """Divide two fractions."""
        numerator1, denominator1 = self.numerator, self.denominator
        numerator2, denominator2 = other.numerator, other.denominator
        if numerator2 == 0:
            raise ValueError("Cannot divide by zero.")
        numerator = numerator1 * denominator2
        denominator = denominator1 * numerator2
        return Fraction(numerator, denominator)

    def simplify(self):
        """Simplify a fraction."""
        numerator, denominator = self.numerator, self.denominator
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        divisor = gcd(numerator, denominator)
        return Fraction(numerator // divisor, denominator // divisor)
    
    def __str__(self):
        """String representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        """Official string representation of the fraction."""
        return f"Fraction({self.numerator}, {self.denominator})"


    
if __name__ == "__main__":
    f1 = create_fraction(1, 2)
    f2 = create_fraction(3, 5)

    print(f"Summe von {f1} und {f2} ist {simplify(add(f1, f2))}")