def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    # Added a quick safety check to prevent crashing on division by zero
    if num2 == 0:
        return "Error (Cannot divide by zero)"
    return num1 / num2

def operators(num1, num2, operation):
    return operation(num1, num2)


while True:
    # 1. Ask upfront if the user wants to continue or exit
    print("\n--- Main Menu ---")
    print("1. Run Calculator")
    print("2. Exit")
    
    main_choice = input("Enter your choice (1 or 2): ").strip()

    if main_choice == "2":
        print("Exiting calculator. Goodbye!")
        break
    elif main_choice != "1":
        print("Invalid choice. Please enter 1 to run or 2 to exit.")
        continue  # Restarts the loop to ask again

    # 2. If they chose to run, ask for the numbers
    print("\n" + "="*20)
    try:
        num1 = int(input("Enter first Number : "))
        num2 = int(input("Enter second Number : "))
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        continue

    # 3. Ask for the specific operation
    operators_choice = (
        "\nChoose an operation:\n"
        "1 For addition\n"
        "2 For subtraction\n"
        "3 For multiplication\n"
        "4 For division"
    )
    print(operators_choice)

    try:
        selection = int(input("Enter a choice (1-4): "))
    except ValueError:
        print("Invalid choice. Returning to main menu.")
        continue

    # 4. Perform the calculation
    print("-" * 20)
    if selection == 1:
        result = operators(num1, num2, add)
        print(f"The sum of {num1} and {num2} is : ", result)

    elif selection == 2:
        result = operators(num1, num2, subtract)
        print(f"The difference of {num1} and {num2} is : ", result)

    elif selection == 3:
        result = operators(num1, num2, multiply)
        print(f"The product of {num1} and {num2} is : ", result)

    elif selection == 4:  # Fixed: Changed from 2 to 4
        result = operators(num1, num2, divide)
        print(f"The quotient of {num1} and {num2} is : ", result)

    else:
        print("Invalid selection. Returning to main menu.")