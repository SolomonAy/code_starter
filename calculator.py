# a useful calculator app

import math

class Calculator:
    """A basic calculator with arithmetic and advanced mathematical operations."""

    def add(self, a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Returns the quotient of two numbers. Raises error if dividing by zero."""
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def square_root(self, a: float) -> float:
        """Returns the square root of a number. Raises error if negative."""
        if a < 0:
            raise ValueError("Square root of negative number is not allowed.")
        return math.sqrt(a)

    def modulo(self, a: float, b: float) -> float:
        """Returns the remainder of a divided by b. Raises error if b is zero."""
        if b == 0:
            raise ValueError("Modulo by zero is not allowed.")
        return a % b

    def exponentiation(self, a: float, b: float) -> float:
        """Returns a raised to the power of b."""
        return a ** b

    def logarithm(self, a: float, base: float = math.e) -> float:
        """Returns the logarithm of a with given base. Raises error if invalid."""
        if a <= 0:
            raise ValueError("Logarithm of non-positive number is not allowed.")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base.")
        return math.log(a, base)

    def sine(self, a: float) -> float:
        """Returns the sine of a (in radians)."""
        return math.sin(a)

    def cosine(self, a: float) -> float:
        """Returns the cosine of a (in radians)."""
        return math.cos(a)

    def tangent(self, a: float) -> float:
        """Returns the tangent of a (in radians). Raises error if undefined."""
        if math.cos(a) == 0:
            raise ValueError("Tangent is undefined at this angle.")
        return math.tan(a)

def main():
    calc = Calculator()
    operations = {
        '+': calc.add,
        '-': calc.subtract,
        '*': calc.multiply,
        '/': calc.divide,
        'sqrt': calc.square_root,
        '%': calc.modulo,
        '**': calc.exponentiation,
        'log': calc.logarithm,
        'sin': calc.sine,
        'cos': calc.cosine,
        'tan': calc.tangent
    }

    print("Basic Calculator (type 'exit' to quit)")
    print("Operations: +, -, *, /, sqrt, %, **, log, sin, cos, tan")
    print("Format: <operation> <number1> [<number2>] (e.g., + 5 3 or sqrt 16)")

    while True:
        try:
            user_input = input("Enter operation: ").strip().split()
            if user_input[0].lower() == 'exit':
                print("Goodbye!")
                break

            op = user_input[0]
            if op not in operations:
                print("Invalid operation.")
                continue

            # Single operand operations
            if op in ['sqrt', 'sin', 'cos', 'tan']:
                if len(user_input) != 2:
                    print("Single operand operation requires one number.")
                    continue
                num1 = float(user_input[1])
                result = operations[op](num1)
            # Logarithm (optional base)
            elif op == 'log':
                if len(user_input) not in [2, 3]:
                    print("Log requires one number and optional base.")
                    continue
                num1 = float(user_input[1])
                base = float(user_input[2]) if len(user_input) == 3 else math.e
                result = operations[op](num1, base)
            # Dual operand operations
            else:
                if len(user_input) != 3:
                    print("Operation requires two numbers.")
                    continue
                num1 = float(user_input[1])
                num2 = float(user_input[2])
                result = operations[op](num1, num2)

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()


# this calculator is a basic calculator. I hope it will be useful for learners. Good luck.