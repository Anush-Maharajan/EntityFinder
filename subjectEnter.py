import random
from PeopleList import peopleAge, peopleName

def subjectName():
    return random.choice(peopleName)

def subjectAge():
    return random.choice(peopleAge)

def subjectStatus():
    return random.choice(["human", "entity"])

def checkName(subjectName,subjectStatus):
    peopleName = []
    # Check if the name is in the list
    if subjectName in peopleName and subjectStatus == "human":
        # Make the subject an Entity if the previous one was Human
        return "Entity"
    else:
        # add the name in the list if the previous one had entered the scanctuary
        peopleName.append(subjectName)

    return subjectName


