import Decision

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
            questionAsked()
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

def questionAsked():
    print("What do you want to ask the subject?\n\n")
    print("1. What is your name?")
    print("2. What is your age?")
    print("3. What is your ID number?")
    print("4. Why did you leave the sanctuary?")
    print("5. Back To Decision Menu")

    while(True):
        userQuestion = int(input("Enter your question as a number: "))
        if userQuestion == 1:
            break
        elif userQuestion == 2:
            break
        elif userQuestion == 3:
            break
        elif userQuestion == 4:
            break
        elif userQuestion == 5:
            decisionInput()
        else:
            print("Invalid input. Please enter a valid number.\n\n")
            continue