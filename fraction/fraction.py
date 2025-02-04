from math import gcd

class Fraction:
    
    def __init__(self: "Fraction", numerator: int | float | str, denominator: int = 1) -> None:
        """
        Initializes a Fraction object.
        Args:
            numerator (int | float | str): The numerator of the fraction. It can be an integer, float, or string.
            denominator (int, optional): The denominator of the fraction. Defaults to 1.
        Raises:
            ValueError: If the denominator is 0.
        Notes:
            - If the numerator is a float, it will be converted to a fraction using its integer ratio.
            - If the numerator is a string, it will be parsed into a fraction.
        """
        
        if denominator == 0:
            raise ValueError("Denominator can't be 0")
        
        if isinstance(numerator, float):
            numerator, denominator = numerator.as_integer_ratio()
            
        if isinstance(numerator, str):
            frac = Fraction.from_string(numerator)
            numerator, denominator = frac.numerator, frac.denominator
            
        self.numerator = numerator
        self.denominator = denominator

    
    @staticmethod
    def from_string(value: str) -> "Fraction":
        """
        Create a Fraction from a string.

        This method supports three types of string inputs:
        1. A string representing a fraction in the form "numerator/denominator".
        2. A string representing a decimal number.
        3. A string representing an integer.
        """
        
        if "/" in value:
            numerator, denominator = map(int, value.split("/"))
            return Fraction(numerator, denominator)
        if "." in value:
            before_decimal, after_decimal = value.split(".")
            denominator = 10 ** len(after_decimal)
            numerator = int(before_decimal + after_decimal)
            return Fraction(numerator, denominator).simplify()
        return Fraction(int(value))

    
    def simplify(fraction: "Fraction") -> "Fraction":
        """Simplify a fraction."""
        
        common_divisor = gcd(fraction.numerator, fraction.denominator)
        return Fraction(fraction.numerator // common_divisor, fraction.denominator // common_divisor)

    
    def __eq__(self: "Fraction", other: "Fraction") -> bool:
        """
        Check if two Fraction instances are equal.
        """
        
        a = self.simplify()
        b = other.simplify()
        return a.numerator == b.numerator and a.denominator == b.denominator


    def __add__(a: "Fraction", b: "Fraction") -> "Fraction":
        """Add two fractions."""
        
        new_numerator = a.numerator * b.denominator + b.numerator * a.denominator
        new_denominator = a.denominator * b.denominator
        return Fraction(new_numerator, new_denominator).simplify()


    def __sub__(a: "Fraction", b: "Fraction") -> "Fraction":
        """Subtract the second fraction from the first fraction."""
        
        new_numerator = a.numerator * b.denominator - b.numerator * a.denominator
        new_denominator = a.denominator * b.denominator
        return Fraction(new_numerator, new_denominator).simplify()


    def __mul__(a: "Fraction", b: "Fraction") -> "Fraction":
        """Multiply two fractions."""
        
        new_numerator = a.numerator * b.numerator
        new_denominator = a.denominator * b.denominator
        return Fraction(new_numerator, new_denominator).simplify()


    def __truediv__(a: "Fraction", b: "Fraction") -> "Fraction":
        """Divide the first fraction by the second fraction."""
        
        new_numerator = a.numerator * b.denominator
        new_denominator = a.denominator * b.numerator
        return Fraction(new_numerator, new_denominator).simplify()
    
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    
    
    def __float__(self):
        return self.numerator / self.denominator
    
    
    def __int__(self):
        return self.numerator // self.denominator
    
    
    
if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    f3 = Fraction(3, 4)
    f4 = Fraction(1, 2)
    
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 == f4)
    print(f1 == f2)
    print(f1)
    print(repr(f1))
    print(float(f1))
    print(int(f1))
    print(Fraction.from_string("1/2"))
    print(Fraction.from_string("0.5"))
    print(Fraction.from_string("1"))
    print(Fraction.from_string("2/3"))