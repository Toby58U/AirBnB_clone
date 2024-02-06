#!/usr/bin/python3

def greet(name):
    """Greet the person with the given name."""
    print(f"Hello, {name}!")

def calculate_sum(x, y):
    """Calculate the sum of two numbers."""
    return (x + y)

def main():
    """Main function to demonstrate the beautiful code."""
    person_name = input("Enter your name: ")
    greet(person_name)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

