from tkinter import *
from Board import *

def Board():
    Board_Layout = Tk()
    Board_Layout.title("MONOPOLY")
    Board_Layout.geometry("1900x900")
    Board_Layout.configure(bg = "black")

    # BOARD
    my_canvas = Canvas(Board_Layout, width = 1000, height = 900, bg = "orange")
    my_canvas.pack(side = "left", padx = 60, pady = 50)

    # LOGO
    my_canvas.create_rectangle(270, 400, 730, 500, fill= "yellow", outline = "grey")
    my_canvas.create_text(500, 450, text = "MONOPOLY", font = ("Areal", 55), fill = "red")

    # TOP (1 - 4)
    my_canvas.create_rectangle(200, 0, 400, 180, fill = "gray")
    my_canvas.create_rectangle(400, 0, 600, 180, fill = "gray")
    my_canvas.create_rectangle(600, 0, 800, 180, fill = "gray")
    my_canvas.create_rectangle(800, 0, 1000, 180, fill = "gray")

    # RIGHT (5 - 9)
    my_canvas.create_rectangle(800, 180, 1000, 360, fill = "gray")
    my_canvas.create_rectangle(800, 360, 1000, 540, fill = "gray")
    my_canvas.create_rectangle(800, 540, 1000, 720, fill = "gray")
    my_canvas.create_rectangle(800, 720, 1000, 900, fill = "gray")

    # BOTTOM (10 - 14)
    my_canvas.create_rectangle(0, 720, 200, 900, fill = "gray")
    my_canvas.create_rectangle(200, 720, 400, 900, fill = "gray")
    my_canvas.create_rectangle(400, 720, 600, 900, fill = "gray")
    my_canvas.create_rectangle(600, 720, 800, 900, fill = "gray")

    # LEFT (15 - 19)
    my_canvas.create_rectangle(0, 0, 200, 180, fill = "gray")
    my_canvas.create_rectangle(0, 180, 200, 360, fill = "gray")
    my_canvas.create_rectangle(0, 360, 200, 540, fill = "gray")
    my_canvas.create_rectangle(0, 540, 200, 720, fill = "gray")

    Board_Layout.mainloop()

# Board()