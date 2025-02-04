# Dynamisch typisierte Sprache - Python

# Zuweisung eines Integers
variable = 10
print(variable)  # Ausgabe: 10

# Zuweisung eines Strings zur selben Variable
variable = "Hallo, Welt!"
print(variable)  # Ausgabe: Hallo, Welt!

# Zuweisung einer Liste zur selben Variable
variable = [1, 2, 3]
print(variable)  # Ausgabe: [1, 2, 3]




import random

def generate_random_hex_sequence(length):
    hex_sequence = ''.join(random.choice('0123456789ABCDEF') for _ in range(length))
    return hex_sequence

def format_hex_sequence(hex_sequence, group_size=2, line_length=4):
    groups = [hex_sequence[i:i+group_size] for i in range(0, len(hex_sequence), group_size)]
    formatted_lines = [' '.join(groups[i:i+line_length]) for i in range(0, len(groups), line_length)]
    return '\n'.join(formatted_lines)

# Beispiel: Generiere eine zufällige Folge von 24 Hexadezimalzahlen
length = 256
random_hex_sequence = generate_random_hex_sequence(length)
formatted_hex_sequence = format_hex_sequence(random_hex_sequence)
print(f"Zufällige Hexadezimalfolge:\n{formatted_hex_sequence}")



def sum_imperative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = 10
result = sum_imperative(n)
print(f"Imperative Sum of first {n} natural numbers: {result}")



from functools import reduce

def sum_functional(n):
    return reduce(lambda x, y: x + y, range(1, n + 1))

n = 10
result = sum_functional(n)
print(f"Functional Sum of first {n} natural numbers: {result}")
