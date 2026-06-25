import time as t


def add(num1 , num2):
    return num1 + num2


def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2


def divide(num1 , num2):
    return num1 / num2


def operators(num1, num2 , operation):
    return operation(num1 ,num2)



while True:
    # 1. Ask upfront if the user wants to continue or exit
    print("\n--- Main Menu ---")
    print("1. Run Calculator")
    print("2. Exit")
    
    main_choice = input("Enter your choice (1 or 2): ").strip()

    if main_choice == "2":
        t.sleep(0.5)
        print("Exiting Calculator ,Gooodbye!")
        t.sleep(0.5)
        break
    elif main_choice != "1":
        print("Invalid choice. Please enter 1 to run or 2 to exit.")
        continue  # Restarts the loop to ask again    
    num1 = int(input("Enter first Number : "))
    num2 = int(input("Enter second Number : "))

    choice =  ("\nChoose an operation\n")
    print(choice)
    operators_choice =("Given numbers are : \n" \
    "1 For addition\n" \
    "2 For subtraction\n" \
    "3 For multiplication\n" \
    "4 For division\n"
    "5 To Exit" )
    print (operators_choice)

    print("Choose an option (1-4)")

    selection = int(input("Enter a choice :"))

    if selection == 1:
        result = operators(num1 , num2 , add)
        print(f"The sum of {num1} and {num2} is : " ,result)

    elif selection == 2:
        result = operators(num1 , num2 , subtract)
        print(f"The difference of {num1} and {num2} is : " ,result)


    elif selection == 3:
        result = operators(num1 , num2 , multiply)
        print(f"The product of {num1} and {num2} is : " ,result)

    elif selection == 4:
        result = operators(num1 , num2 , divide)
        print(f"The Quotion of {num1} and {num2} is : " ,result)

    elif selection == 5:
        t.sleep(1.5)
        print("Exiting Calculator ,Gooodbye!")
        break
    else :
        print("Invalid syntax \n Please choose from given number : ")



