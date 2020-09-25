from Players import *
from tkinter import *
from Board_layout_design import *

def Start_Screen():
    start_screen = Tk()
    start_screen.title("MONOPOLY")
    start_screen.configure(bg = "black")

    def Exit():
        start_screen.destroy()

    def Start_Game():
        player = [Player_1_Name, Player_2_Name, Player_3_Name, Player_4_Name]
        players_playing = []
        players = []

        for i in range(4):
            Name = player[i].get()
            if Name != "":
                players_playing.append(Name)
        Creat_Players(players_playing, players)
        Exit()
        # for i in range(0, len(players)):
        #     print(players[i].Name)
        #     print(players[i].Balance)
        #     print(players[i].Position)
        #     print(players[i].Turn)
        Board_Display()

    Player_1 = Label(start_screen, text = "PLAYER 1: ", fg = "black")
    Player_1.grid(row = 0)

    Player_1_Name = Entry(start_screen)
    Player_1_Name.grid(row = 0, column = 1)

    Player_2 = Label(start_screen, text = "PLAYER 2: ", fg = "black")
    Player_2.grid(row = 1)

    Player_2_Name = Entry(start_screen)
    Player_2_Name.grid(row = 1, column = 1)

    Player_3 = Label(start_screen, text = "PLAYER 3: ", fg = "black")
    Player_3.grid(row = 2)

    Player_3_Name = Entry(start_screen)
    Player_3_Name.grid(row = 2, column = 1)

    Player_4 = Label(start_screen, text = "PLAYER 4: ", fg = "black")
    Player_4.grid(row = 3)

    Player_4_Name = Entry(start_screen)
    Player_4_Name.grid(row = 3, column = 1)

    Start_Button = Button(start_screen, text = "START GAME", width = 13, height = 1, command = lambda:Start_Game())
    Start_Button.grid(row = 4, column = 0)

    Exit_Button = Button(start_screen, text = "EXIT", bg = "black", width = 6, height = 1, command = lambda:Exit())
    Exit_Button.grid(row = 4, column = 1)

    start_screen.mainloop()