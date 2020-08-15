from Players import Creat_Players
from Properties import Property
import Colours
import Players
import random
from Functions import NuggetConverter, IngutsConverter, Roll, Upper
from Board import Go, Location, Create_Board
from Chance_Community import Chance, Community_Chest


#STEP 1: CREATE BOARD WITH ALL PROPOERTIES

#STEP 2: PRINT MONPOLY GAME WELCOME MESSAGE 
# 
# STEP 3: ADD PLAYERS AND ALL PLAYERS GET DEFAULT BALANCE AND POSTION AT GO. 
# 
# STEP 4: START GAME 
# 
# STEP 5: PRINT DEFAULT PLAYER SATAUS TO BEGIN 
# 
# STEP 6: PRINT BAORD DEATILS 
# 
# STEP 7 : START GAME LOOP WITH PLAYER 1 
# 
# STEP 7.1 : PLAYER 1 GETS TO ROLL DICE 
# STEP 7.2 : UPDATE PLAYER 1 POSTION ON BAORD
# STEP 7.3 : UPDATE ALL PLAYER STATUS AND BALANCES 
# STEP 7.4 : PRINT BOARD STATUS .. 
# 
# STEP 8 : EXIT GAME IF A PLAYER IS BRANKRUPT OR ALL PLAYERS CHOOSE TO EXIT THE GAME.  
# 
#   
# Players_list = []
# Creat_Players(Players_list)
# print(Players_list)

# for Player in Players_list:
#     print(Player.Name)

Board = []
Create_Board(Board)

x = 0

print(f'Postition      | Prpoerty      | Colour      | Cost')
for x in range((len(Board) - 1)):
    print(f'{x + 1}            | {Board[x].Name}            | {Board[x].Colour}            | {Board[x].Cost}')