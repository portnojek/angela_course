#Klasy pozwalają nam deklarować własne obiekty złożone posiadające wbudowane pola a także funkcje.
'''Klasę dodajemy w zasadzie w
dowolnym miejscu pliku, jednak korzystać z niej będziemy mogli tylko w liniach znajdujących się pod
jej deklaracją. Jeśli chesz by do jakiegoś pola nie zostało
przypisane nic, wystarczy przypisać "None"'''

class Osoba:
    imie='Bartek'
    nazwisko='Kociecki'
    wiek=37
    pustePole=None

#Aby stworzyć obiekt takiej klasy używamy tak zwanego konstruktora:

o=Osoba()
print(o.imie, o.nazwisko, o.wiek, o.pustePole)

#Klasę możesz umieścić również w innym module i zwyczajnie zaimportować:

from inna import Osoba2
o=Osoba2()
print(o.imie, o.nazwisko, o.wiek, o.pustePole)

#zawartość pola mozna oczywiście zmienia c
class Osoba:
    imie='Andrzej'
    nazwisko='Klusiewicz'
    wiek=33
    pustePole=None

o=Osoba()
o.imie='Krzysztof'
o.nazwisko='Jarzyna'
print(o.imie,o.nazwisko)

#a to dowód na elastyczność języka Python (zaskoczenie dla programistów innych języków)
#Krótko mówiąc, takie odniesienie "Klasa.pole" oznacza odwołanie do wartości domyślnej tego pola.
class Osoba:
    imie=None
    nazwisko=None
    ksywka=None
o1=Osoba()
o1.imie='Jerzy'
o1.nazwisko='Kiler'
o1.ksywka='Killer'
o2=Osoba()
o2.imie='Stefan'
o2.nazwisko='Siarzewski'
o2.ksywka='Siara' #i wszystko jasne
Osoba.imie='zamienione...'
print(o1.imie,o2.imie)
o3=Osoba()
print(o3.imie)

#kolejny przykład
#w chwili przypisania wartości do "nieistniejącego" pola w obiekcie, takie pole po prostu w nim powstało.
class Osoba:
    imie=None
    nazwisko=None
    ksywka=None
o1=Osoba()
o1.imie='Jerzy'
o1.nazwisko='Kiler'
o1.ksywka='Killer'
o1.wtf='omg!'
print(o1.imie,o1.nazwisko,o1.ksywka,o1.wtf)