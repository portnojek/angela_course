#funkcja os.walk - funkcja pozwalająca na przeszukiwanie katalogów. Jako argument przyjmuje ścieżkę startową. Otrzymujemy krotki: pierwsza wartość (str) w elemencie to ścieżka katalogu którego dotyczą dane w krotce.
import os
from time import strftime
for p in os.walk("/home/bartek/Desktop"):
    print(p)

#można też zmienić kierunek przeszukiwania katalogów
import os
for p in os.walk("/home/bartek/Desktop", False):
    print(p)

#a tu fajna opcja jak to wyświetlić w drzewie
import os
for katalog,podkatalogi, pliki in os.walk("/home/bartek/Desktop"):
    print(f'KATALOG: {katalog}:')
    if(len(podkatalogi)>0):
        print(f'PODKATALOGI: ')
        for po in podkatalogi:
            print(f'     {po}')
    if(len(pliki)>0):
        print(f'   PLIKI: ')
        for pl in pliki:
            print(f'     {pl}')

#PORUSZANIE SIĘ PO SYSTEMIE PLIKÓW
#Zmiana i sprawdzanie aktualnego katalogu

import os
os.chdir("/home/bartek/Dokumenty/pythonowe_pliczki")
print(os.getcwd)

#listowania zawartości katalogu
print(os.listdir)

#sprawdzenie czy katalog istnieje
import os
if os.path.exists("/home/bartek/Dokumenty/pythonowe_pliczki"):
    print("jest taki katalog")
else:
    print("brakuje takiego katalogu")

#sprawdzanie czy mamy do czynienia z plikiem czy z katalogiem
import os
if os.path.isdir("/home/bartek/Dokumenty/pythonowe_pliczki"):
    print("to jest katalog")
else:
    print("to jest plik")

if os.path.isfile("/home/bartek/Dokumenty/pythonowe_pliczki"):
    print("to jest plik")
else:
    print("to jest katalog")

#sprawdzanie wielkości plików
import os
size = os.path.getsize("/home/bartek/Dokumenty/pythonowe_pliczki/nowy.txt")
print(f"Ten plik ma pojemność {size} bajtów")

#taka próbczeka jak ogarnąć czas
import datetime

czas = datetime.datetime.now()
rok = czas.year
print(czas)
print(rok)
print(czas.strftime("%A"))
print(datetime.date(2020, 5, 24))

#tworzenie i kasowanie katalogów
#os.rmdir("/home/bartek/Dokumenty/pythonowe_pliczki/żyj_i_żryj")
#os.mkdir("/home/bartek/Dokumenty/pythonowe_pliczki/żyj_i_żryj")

#kasowanie pliku
open("/home/bartek/Dokumenty/pythonowe_pliczki/żyj_i_żryj/gniocchi.txt", encoding='utf-8', mode="w")
os.remove("/home/bartek/Dokumenty/pythonowe_pliczki/żyj_i_żryj/gniocchi.txt")
