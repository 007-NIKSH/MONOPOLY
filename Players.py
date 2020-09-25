class Player:
  def __init__(self, Name, Balance, Property, Position, Turn):
    self.Name = Name
    self.Balance = Balance
    self.Property = Property
    self.Position = Position
    self.Turn = Turn

# def Creat_Players(Players_list):
#   Start = True
#   while Start == True:
#     Number = int(input("\nENTER NUMBER OF PLAYERS: "))

#     if Number <= 4 and Number > 1:
#       x = 1
#       i = 0
#       while x <= Number:
#         print(f'\nENTER PLAYER {x} DETAILS: ')
#         Player_Name = input("NAME: ")
        
#         if Player_Name not in Players_list:
#           Players_list.append(Player(Player_Name, 405, '', 1, 0))
#           print("\nPLAYER CREATED")
#           print(f'\nPLAYER {x} NAME: {Player_Name}')
#           x += 1
#           i += 1
        
#         else:
#           print("PLAYER NAME TAKEN")

#         if x == Number:
#           Start = False
          
#         else:
#           continue

#     else:
#       print("INVALID NUMBER OF PLAYERS")
#       print("ONLY 2 - 4 PLAYERS ALLOWED")
#       continue

def Creat_Players(player_list, players):
  for i in range(0, len(player_list)):
    Player_Name = player_list[i]
    players.append(Player(Player_Name, 405, '', 1, 0))
    i += 1