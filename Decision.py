def decisionInput():
    print("A subject has entered the lab.....\n\n")
    
    while(True):
        print("What do you want to do?\n\n")
        print("1. Ask the subject questions")
        print("2. Display the Entry list")
        print("3. Let the subject enter the sanctuary")
        print("4. Declare the subject as an entity")

        userInput = int(input("Enter your choice as a number: "))
        if userInput == 1:
            pass
        elif userInput == 2:
            pass
        elif userInput == 3:
            break
        elif userInput == 4:
            break
        else:
            print("\n\nInvalid input. Please enter a valid number.\n\n")
            continue