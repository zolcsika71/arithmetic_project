def add(a, b):
    """Add two numbers and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numbers.")
    return a + b


def subtract(a, b):
    """Subtract the second number from the first and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numbers.")
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numbers.")
    return a * b


def divide(a, b):
    """Divide the first number by the second and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numbers.")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_user_input():
    """Get two numbers from the user."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def perform_operations(num1, num2):
    """Perform arithmetic operations and display results."""
    print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    try:
        result = divide(num1, num2)
        print(f"Division: {num1} / {num2} = {result}")
    except ValueError as e:
        print(f"Division Error: {e}")


def main():
    print("Welcome to the Arithmetic Operations Calculator!")
    num1, num2 = get_user_input()
    perform_operations(num1, num2)


if __name__ == "__main__":
    main()
