from Functions import NuggetConverter, IngutsConverter, Roll

NC = NuggetConverter()
print("NUGGETS:", NC)
ICinput = int(input("\nNUGGETS: "))
IC = IngutsConverter(ICinput)
print(IC)
roll = Roll()
print("Roll: {}" .format(roll))