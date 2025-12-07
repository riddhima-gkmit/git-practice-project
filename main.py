def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")

    choice = input("Choose an option (1 or 2): ")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(x, y))
    elif choice == "2":
        print("Result:", subtract(x, y))
    else:
        print("Invalid choice")
