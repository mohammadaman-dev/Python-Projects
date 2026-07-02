print("=== Loop Calculator ===")

while True:
    num1 = 15
    num2 = 5

    print("\nFirst Number :", num1)
    print("Second Number:", num2)

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Addition =", num1 + num2)

    elif choice == "2":
        print("Subtraction =", num1 - num2)

    elif choice == "3":
        print("Multiplication =", num1 * num2)

    elif choice == "4":
        print("Division =", num1 / num2)

    elif choice == "0":
        print("Thank you!")
        break

    else:
        print("Invalid Choice! Please try again.")
