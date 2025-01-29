# calculator.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def find_max(a, b):
    """Returns the maximum of two numbers."""
    return max(a, b)

# Main function to test the calculator
if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiplication: {multiply(x, y)}")
    print(f"Division: {divide(x, y)}")
    print(f"Maximum: {find_max(x, y)}")