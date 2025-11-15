"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def logarithm(a, b):
    # log base a of b
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("invalid values for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

git add calculator.py
git commit -m "modified calculator p1"
git push



