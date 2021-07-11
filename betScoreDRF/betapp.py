#program do obstawiania meczów

players = []
numberOfPlayers = int(input("Podaj liczbę graczy: "))

def imiona_graczy():
    for i in range(1, numberOfPlayers + 1):
        players.append(str(input(f"Podaj imię {i} gracza: ")))
    for el in players:
        print("Witajcie! " + ', '.join(players))

imiona_graczy()


    



