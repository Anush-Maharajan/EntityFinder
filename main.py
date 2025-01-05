from Decision import decisionInput
from subjectEnter import subjectEnter, checkName
import random


def main():
    # Basic defination of the game!!
    print("""Welcome to the sanctuary. You are required to detect if the subject that has entered to the lab
          is a human or an entity. You have to make a decision based on the questions that you will ask the subject.
          Your decisions is essential for the survival of the people in the sanctuary. Good luck!\n\n\n""")
    
    playCount = random.randint(2, 6)
    peopleEntered = {}
    while(playCount > 0):
        playCount -= 1
        subjectName, subjectAge = subjectEnter()
        checkName(subjectName)
        decisionInput()

if __name__ == "__main__":
    main()