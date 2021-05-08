from tkinter import *
from Board import *

def Board_Display():
    Board_Layout = Tk()
    Board_Layout.title("MONOPOLY")
    Board_Layout.geometry("1500x900")
    Board_Layout.configure(bg = "black")

    All_Properties_Created = []
    Create_Board(All_Properties_Created)

    my_canvas = Canvas(Board_Layout, width = 1000, height = 800, bg = "orange")
    my_canvas.pack(side = "left")

    my_canvas.create_rectangle(200, 350, 800, 450, fill= "gray")
    my_canvas.create_text(500, 400, text = "MONOPOLY", font = ("Areal", 75))

    for x in range(len(All_Properties_Created)):
        # print(len(All_Properties_Created))
        print(All_Properties_Created[x].Name, "\t\t", All_Properties_Created[x].Cost)

    # TOP (10)
    my_canvas.create_rectangle(0, 0, 100, 100, fill = "gray")
    my_canvas.create_rectangle(100, 0, 200, 100, fill = "gray")
    my_canvas.create_rectangle(200, 0, 300, 100, fill = "gray")
    my_canvas.create_rectangle(300, 0, 400, 100, fill = "gray")
    my_canvas.create_rectangle(400, 0, 500, 100, fill = "gray")
    my_canvas.create_rectangle(500, 0, 600, 100, fill = "gray")
    my_canvas.create_rectangle(600, 0, 700, 100, fill = "gray")
    my_canvas.create_rectangle(700, 0, 800, 100, fill = "gray")
    my_canvas.create_rectangle(800, 0, 900, 100, fill = "gray")
    my_canvas.create_rectangle(900, 0, 1000, 100, fill = "gray")

    Label(my_canvas, text = All_Properties_Created[0].Name, bg = "gray", fg = "white", font = (1)).place(x = 10, y = 20)
    Label(my_canvas, text = All_Properties_Created[1].Name, bg = "gray", fg = "white", font = (1)).place(x = 110, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 230, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 330, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 430, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 530, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 630, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 730, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 830, y = 20)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 20)

    Label(my_canvas, text = All_Properties_Created[0].Cost, bg = "gray", fg = "white", font = (50)).place(x = 40, y = 50)
    Label(my_canvas, text = All_Properties_Created[1].Cost, bg = "gray", fg = "white", font = (50)).place(x = 135, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 230, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 330, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 430, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 530, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 630, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 730, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 830, y = 50)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 50)

    # BOTTOM (10)
    my_canvas.create_rectangle(0, 800, 100, 700, fill = "gray")
    my_canvas.create_rectangle(100, 800, 200, 700, fill = "gray")
    my_canvas.create_rectangle(200, 800, 300, 700, fill = "gray")
    my_canvas.create_rectangle(300, 800, 400, 700, fill = "gray")
    my_canvas.create_rectangle(400, 800, 500, 700, fill = "gray")
    my_canvas.create_rectangle(500, 800, 600, 700, fill = "gray")
    my_canvas.create_rectangle(600, 800, 700, 700, fill = "gray")
    my_canvas.create_rectangle(700, 800, 800, 700, fill = "gray")
    my_canvas.create_rectangle(800, 800, 900, 700, fill = "gray")
    my_canvas.create_rectangle(900, 800, 1000, 700, fill = "gray")

    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 130, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 230, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 330, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 430, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 530, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 630, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 730, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 830, y = 720)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 720)

    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 130, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 230, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 330, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 430, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 530, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 630, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 730, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 830, y = 750)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 750)

    # LEFT (7)
    my_canvas.create_rectangle(0, 100, 100, 200, fill = "gray")
    my_canvas.create_rectangle(0, 200, 100, 300, fill = "gray")
    my_canvas.create_rectangle(0, 300, 100, 400, fill = "gray")
    my_canvas.create_rectangle(0, 700, 100, 800, fill = "gray")
    my_canvas.create_rectangle(0, 400, 100, 500, fill = "gray")
    my_canvas.create_rectangle(0, 500, 100, 600, fill = "gray")
    my_canvas.create_rectangle(0, 600, 100, 700, fill = "gray")

    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 120)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 220)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 320)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 420)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 520)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 620)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 720)

    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 150)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 250)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 350)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 450)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 550)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 650)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 30, y = 750)

    # RIGHT (7)
    my_canvas.create_rectangle(900, 100, 1000, 200, fill = "gray")
    my_canvas.create_rectangle(900, 200, 1000, 300, fill = "gray")
    my_canvas.create_rectangle(900, 300, 1000, 400, fill = "gray")
    my_canvas.create_rectangle(900, 700, 1000, 800, fill = "gray")
    my_canvas.create_rectangle(900, 400, 1000, 500, fill = "gray")
    my_canvas.create_rectangle(900, 500, 1000, 600, fill = "gray")
    my_canvas.create_rectangle(900, 600, 1000, 700, fill = "gray")

    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 120)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 220)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 320)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 420)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 520)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 620)
    Label(my_canvas, text = "GO", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 720)

    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 150)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 250)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 350)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 450)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 550)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 650)
    Label(my_canvas, text = "100", bg = "gray", fg = "white", font = (50)).place(x = 930, y = 750)

    

    Board_Layout.mainloop()

Board_Display()