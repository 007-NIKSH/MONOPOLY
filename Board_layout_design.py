from tkinter import *

def Board_Display():
    Board_Layout = Tk()
    Board_Layout.title("MONOPOLY")
    Board_Layout.geometry("1440x880")
    Board_Layout.configure(bg = "black")

    my_canvas = Canvas(Board_Layout, width = 1000, height = 800, bg = "orange")
    my_canvas.pack(side = "left")

    my_canvas.create_rectangle(200, 350, 800, 450, fill= "gray")
    my_canvas.create_text(500, 400, text = "MONOPOLY", font = ("Areal", 100))

    # TOP
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

    # BOTTOM
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

    # LEFT
    my_canvas.create_rectangle(0, 100, 100, 200, fill = "gray")
    my_canvas.create_rectangle(0, 200, 100, 300, fill = "gray")
    my_canvas.create_rectangle(0, 300, 100, 400, fill = "gray")
    my_canvas.create_rectangle(0, 700, 100, 800, fill = "gray")
    my_canvas.create_rectangle(0, 400, 100, 500, fill = "gray")
    my_canvas.create_rectangle(0, 500, 100, 600, fill = "gray")
    my_canvas.create_rectangle(0, 600, 100, 700, fill = "gray")

    # RIGHT
    my_canvas.create_rectangle(900, 100, 1000, 200, fill = "gray")
    my_canvas.create_rectangle(900, 200, 1000, 300, fill = "gray")
    my_canvas.create_rectangle(900, 300, 1000, 400, fill = "gray")
    my_canvas.create_rectangle(900, 700, 1000, 800, fill = "gray")
    my_canvas.create_rectangle(900, 400, 1000, 500, fill = "gray")
    my_canvas.create_rectangle(900, 500, 1000, 600, fill = "gray")
    my_canvas.create_rectangle(900, 600, 1000, 700, fill = "gray")

    Board_Layout.mainloop()