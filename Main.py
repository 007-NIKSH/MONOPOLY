from Functions import NuggetConverter, IngutsConverter, Roll, Upper
from Board import Go, Location
from Chance_Community import Chance, Community_Chest


while True:
    inguts = int(input("\nINGUTS: "))
    nuggets = int(input("NUGGETS: ")) 
    
    if inguts == 0 and nuggets == 0:
        break

    else:
        NC = NuggetConverter(inguts, nuggets)
        print("\nNUGGETS:", NC)
        continue

ICinput = int(input("\nNUGGETS: "))
IC = IngutsConverter(ICinput)
print(IC)

roll = Roll()
print("Roll: {}" .format(roll))

Player_1 = input("ENTER PLAYER NAME: ")
go = Go(Player_1)
print(f'BALANCE: {go}')

Player_2 = input("ENTER PLAYER NAME: ")
location = Location(Player_2)
print(f'BALANCE: {location}')

B = input("\nTEXT: ")
print(Upper(B))

print(Chance())
print(Community_Chest())