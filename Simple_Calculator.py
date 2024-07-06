def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y

    else:
        return "Error! Division by zero."

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("\nEnter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator....\n")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print(f"{a} + {b} = {add(a, b)}")
            elif choice == '2':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif choice == '3':
                print(f"{a} * {b} = {multiply(a, b)}")
            elif choice == '4':
                result = divide(a, b)
                print(f"{a} / {b} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice! Please select a valid operation.")
