def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print("Simple Calculator - Choose an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = input("Choose an option (1 or 2): ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(x, y))
    elif choice == "2":
        print("Result:", subtract(x, y))
    elif choice == "3":
        print("Result:", multiply(x, y))

    else:
        print("Invalid choice")
