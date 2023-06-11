# MAIN MENU
menu = {
    "1": "ADDITION",
    "2": "SUBTRACTION",
    "3": "MULTIPLICATION",
    "4": "DIVISION",
    "Q": "Exit"
}

# WELCOME MESSAGE
print("WELCOME TO THE CALCULATOR APP!\n")

# MENU OPTIONS
for option in menu:
    print(f"{option}. {menu[option]}")

# USER CHOOSES TO EXIT
while True:
    # ASKING TO THE USER FOR THEIR CHOICE
    choice = input("\nENTER YOUR CHOICE ::> ")

    # USER WANTS TO EXIT
    if choice.upper() == "Q":
        print("\nTHANK YOUR FOR COMING AND USING THE CALCULATOR APP!")
        break

    # IF VALID CHOICE
    if choice not in menu:
        print("\nINVALID CHOICE, PLEASE ENTER THE VALID OPTION.")
        continue

    # ASKING THE USER FOR  THEIR NUMBERS 
    num1 = float(input("ENTER YOUR 1ST NUMBER: "))
    num2 = float(input("ENTER YOUR 2ND NUMBER: "))

    # CALCULATION ON THE USER'S BASED CHOICE
    if choice == "1":
        result = num1 + num2
        operation = "+"
    elif choice == "2":
        result = num1 - num2
        operation = "-"
    elif choice == "3":
        result = num1 * num2
        operation = "*"
    elif choice == "4":
        result = num1 / num2
        operation = "/"
    else:
        result = None

    # RESULT
    if result is not None:
        print(f"\n{num1} {operation} {num2} = {result}\n")