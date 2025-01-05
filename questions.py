print("What do you want to ask the subject?\n\n")
print("1. What is your name?")
print("2. What is your age?")
print("3. What is your ID number?")
print("4. Why did you leave the sanctuary?")

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
    else:
        print("Invalid input. Please enter a valid number.\n\n")
        continue