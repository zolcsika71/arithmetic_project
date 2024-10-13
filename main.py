def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide the first number by the second and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Welcome to the Arithmetic Operations Calculator!")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform operations and display results
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")

    # Handle division by zero
    try:
        result = divide(num1, num2)
        print(f"Division: {num1} / {num2} = {result}")
    except ValueError as e:
        print(f"Division Error: {e}")


if __name__ == "__main__":
    main()
