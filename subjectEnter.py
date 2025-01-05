import random
from PeopleList import peopleAge, peopleName

def subjectEnter():
    # Randomly select a name and age from the lists
    subjectAge = random.choice(peopleAge)
    subjectName = random.choice(peopleName)

    return subjectName, subjectAge

def checkName(subjectName,subjectStatus):
    peopleName = []
    # Check if the name is in the list
    if subjectName in peopleName and subjectStatus == "human":
        # Make the subject an Entity if the previous one was Human
        return "Entity"
    else:
        # add the name in the list if the previous one had entered the scanctuary
        peopleName.append(subjectName)
        
    return