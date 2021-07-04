from Properties import Property
import random
from Functions import IngutsConverter

All_Properties = ['Go', 'Motor Drive', 'Gardget Wharf', 'Speed Breaker', 'Surfers Cove', 'Chance', 'Aqua Park', 'Lake Side Marina', 'Rail Way', 'Castle View', 'Just Visiting (or) Jail', 'Dream Avenue', 'Palace Gardens', 'Community Chest', 'Adventure Park', 'Theme Park City', 'Movie District', 'Ender Pearl', 'Style Square', 'Air Way', 'Party Plaza', 'Show Time Boulevard', 'Chance', 'Sunshine Bay', 'Bling Beach', 'Water Way', 'Yatch Harbour', 'Go To The End', 'Tree Top Retreat', 'Ski Mountain', 'Diamond Hill', 'Fortune Valley', 'Over Speeding', 'Paradise Island']

Properties = ['Motor Drive', 'Gardget Wharf', 'Surfers Cove', 'Aqua Park', 'Lake Side Marina', 'Rail Way', 'Castle View', 'Dream Avenue', 'Palace Gardens', 'Adventure Park', 'Theme Park City', 'Movie District', 'Style Square', 'Air Way', 'Party Plaza', 'Show Time Boulevard', 'Sunshine Bay', 'Bling Beach', 'Water Way', 'Yatch Harbour', 'Tree Top Retreat', 'Ski Mountain', 'Diamond Hill', 'Fortune Valley', 'Paradise Island']
Colour = ['Brown', 'Brown', 'Light Blue', 'Light Blue', 'Light Blue', 'White', 'Pink', 'Pink', 'Pink', 'Orange', 'Orange', 'Orange', 'Red', 'White', 'Red', 'Red', 'Yellow', 'Yellow', 'White', 'Yellow', 'Green', 'Green', 'Green', 'Dark Blue', 'dark Blue']
Cost = [8, 11, 18, 23, 27, 36, 45, 50, 54, 63, 68, 72, 81, 36, 86, 90, 99, 104, 36, 108, 117, 122, 126, 144, 162]

def Create_Board(Board):
  x = 0
  for x in range(len(Properties)):
      Board.append(Property(Name = Properties[x], Colour = Colour[x], Owned = False, Cost = Cost[x], House = 0))
      C = IngutsConverter(Board[x].Cost)
      # print(f'{x + 1}: {Board[x].Name} \t\t\t | {Board[x].Colour} \t\t | {C[0]}, {C[1]}')
      x += 1

def Go(player_Name):
    player_Name.Balance = player_Name.Balance + 45
    return player_Name.Balance

def Location(player_Name):
  player_Name.Balance = player_Name.Balance - 23
  return player_Name.Balance

def Jail(player_Name):
    t = 1
    while t == 1:
        print("1 - MISS 3 TURNS")
        print("2 - PAY 1 INGOT 5 NUGGETS")
        print("3 - DOUBLES")
        Choice = int(input("OPTION: "))

        if Choice == 1:
            Jail_Miss(player_Name)
            t = 0

        elif Choice == 2:
            Jail_Pay(player_Name)
            t = 0

        elif Choice == 3:
            Jail_Doubles(player_Name)
            t = 0

        else:
            print("INVALID POTION")
            continue

def Jail_Miss(player_Name):
  player_Name.Turn += 3

def Jail_Pay(player_Name):
  player_Name.Balance = player_Name.Balance - 14

def Jail_Doubles_Roll():
  Roll_1 = random.randint(1, 6)
  Roll_2 = random.randint(1, 6)
  return [Roll_1, Roll_2]

def Jail_Doubles(player_Name):
  Turn = 1
  while Turn <= 3:
    Roll = Jail_Doubles_Roll()
    Die_1 = Roll[0]
    Die_2 = Roll[1]
    
    if Die_1 == Die_2:
      print(f'DOUBLES SUCCESFULL !!')
      print(f'YOU GOT THE NUMBERS {Roll}')
      break
    
    else:
      if Turn == 3:
        print(f'YOU FAILED THE DOULES')
        print(f'YOU GOT THE NUMBERS {Roll}')
        Jail_Pay(player_Name)
        break

      else:
        print(f'YOU GOT THE NUMBERS {Roll}')
        Turn += 1
        continue