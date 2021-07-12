#Aplikacja służy do typowania wyników meczów oraz kalkulacji wyniku na podstawie wygranej

from tkinter import *

root = Tk()
root.title("Obstawianie meczów. v.1.0")

players = []
numberPlayers= []

numberOfPlayers = Entry(root, width=20, borderwidth=3)
numberOfPlayers.pack()


def dodaj_liczbe_graczy():
    numberPlayers.__delitem__
    currentLiczba = int(numberOfPlayers.get())
    label1 = Label(root, text="Liczba graczy wynosi: " + str(currentLiczba) + "\n" + "Imiona graczy: ")
    label1.pack()
    numberPlayers.append(currentLiczba)
    


button1 = Button(text="Wprowadź liczbę graczy biorących udział w grze", fg="White", bg="grey", command=dodaj_liczbe_graczy)
button1.pack()

labelPrzerwa = Label(text="                                             ")
labelPrzerwa.pack()

nameOfPlayer = Entry(root, width=20, borderwidth=3)
nameOfPlayer.pack()

def imiona_graczy():
    # for i in range(1, numberPlayers[0]+1):
    currentPlayer = nameOfPlayer.get()
    # label2 = Label(text=f"Imię gracza: ")
    # label2.pack()
    label3 = Label(root, text=currentPlayer)
    label3.pack()

dodajGracza = Button(root, text = "Dodaj gracza", command=lambda: imiona_graczy())
dodajGracza.pack()

root.mainloop()