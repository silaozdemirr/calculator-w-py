print("===Simple Calculator===")

while True:
    print("\n1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")

    choice = input("Select an operation: ")

    if choice == "5":
        print("Program terminated.")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice!")
        continue

    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: "))

    if choice == "1":
        result = number1 + number2

    elif choice == "2":
        result = number1 - number2
    
    elif choice == "3":
        result = number1 * number2

    elif choice == "4":
        if number2 == 0:
            print("Error: Division by zero is not allowed!")
            continue

        result = number1 / number2

    print(f"Result: {result}")



