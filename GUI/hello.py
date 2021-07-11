from tkinter import *

root = Tk()
myLabel1 = Label(root, text="Witaj w programie do obstawiania meczów!")
myLabel2 = Label(root, text="Pamiętajcie, że najważniejsza jest zabawa!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

# myLabel1.pack()
# myLabel2.pack()

root.mainloop()
