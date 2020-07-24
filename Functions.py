import random

def NuggetConverter():
    inguts = int(input("INGUTS: "))
    nuggets = int(input("NUGGETS: "))  
    return ((inguts*9) + nuggets)

def IngutsConverter(Nuggets):
    inguts = Nuggets // 9
    nuggets = Nuggets % 9
    return [inguts, nuggets]

def bal(Balance):
    Balance = print("HI")
    return

def Roll():
    Roll_1 = random.randint(1, 6)
    Roll_2 = random.randint(1, 6)
    return (Roll_1 + Roll_2)