print("What do you want to ask the subject?\n\n")
print("1. What is your name?")
print("2. What is your age?")
print("3. What is your ID number?")
print("4. Why did you leave the sanctuary?")

userQuestion = int(input("Enter your question as a number: "))
while(True):
    if userQuestion == 1:
        print("What is your name?")
        break
    elif userQuestion == 2:
        print("What is your age?")
        break
    elif userQuestion == 3:
        print("What is your ID number?")
        break
    elif userQuestion == 4:
        print("Why did you leave the sanctuary?")
        break
    else:
        print("Invalid input. Please enter a valid number.\n\n")
        continue