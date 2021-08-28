class Osoba:
    imie='Bartek'
    nazwisko='Kociecki'
    wiek=37
    def wypiszMnie(self):
        print(self.imie,self.nazwisko,self.wiek)

o=Osoba()
o.wypiszMnie()

class Witacz:
    def przywitaj(self,imie,nazwisko):
        print("Witaj " + imie + " " + nazwisko)

w=Witacz()
w.przywitaj("Jerzy","Ryba")

#"self" to wskaźnik do obiektu w którym się znajdujemy i pozwala się np. odwoływać do jego pól. Np:

class Programista():
    jezyk="Python"
    def funkcja(self):
        print("programuje w języku " + self.jezyk)

p=Programista()
p.funkcja()

class Polska():
    def roszczenie(self):
        return "Mienie bezspadkowe"

p=Polska()
p.roszczenie()