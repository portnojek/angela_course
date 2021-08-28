'''Dziedziczenie to rozszerzanie klas, dla przykładu możemy przyjąć że mamy klasę
"Samochod" posiadającą funkcje "jedz", "skrec", "hamuj". Nastepnie tworzymy klasę
"SuperSamochod". Chcemy by klasa "SuperSamochod" zawsze posiadała to co klasa "Samochod", plus
jakieś dodatkowe funkcje np "turbo". To jest właśnie miejsce na zastosowanie dziedziczenia.
Przeanalizujmy taki właśnie przykład:'''

class Samochod:
    def jedz(self):
        print("no to jedziemy...")
    def hamuj(self):
        print("khhhhh.....")
    def skrec(self):
        print("na ręcznym!")


class SuperSamochod(Samochod):
    def turbo(self):
        print("włączamy podtlenek gazotu w 1.6 i mamy turbo na miarę'Szerszenia'")

s=Samochod()
s.jedz()
s.hamuj()
s.skrec()
ss=SuperSamochod()
ss.jedz()
ss.hamuj()
ss.skrec()
ss.turbo()

'''A więc... Mam klasę
"Samochod", oraz klasę "SuperSamochod" dziedziczącą po klasie Samochod. Skąd wiemy że klasa
"SuperSamochod" dziedziczy po klasie "Samochod" - z zapisu:

class SuperSamochod(Samochod):'''

#dziedziczenie po wielu klasach
class Pojazd:
    def jedz(self):
        print("wroom!")

class Armata:
    def strzelaj(self):
        print("jeb, jeb, jeb!")
class Czolg(Pojazd,Armata):
    pass

c=Czolg()
c.jedz()
c.strzelaj()

'''Mamy klasę "Pojazd" która posiada funkcję "jedz" i klasę "Armata" która posiada funkcję "strzelaj".
Na końcu stworzyłem klasę Czołg dziedziczącą po obu wymienionych. Obiekty klasy "Czolg" będą
więc posiadały obie metody. Uruchomienie spowoduje wyświetlenie obu komunikatów z obu funkcji.
Co jednak gdyby okazało się że obie klasy posiadają funkcję o takiej samej nazwie? Którą z nich
będziemy w takiej sytuacji wywoływać? Czy to w ogóle możliwe? Tak, jest to możliwe a wszystko
sprowadza się do kolejności wymieniania klas po których dziedziczymy. Poniżej deklaracja trzech klas.
Klasa C dziedziczy zarówno po klasie B jak i A. Klasy B i A posiadają taką samą funkcję "hello".'''

class A:
    def hello(self):
        print('siema, tu A')
class B:
    def hello(self):
        print('siema, tu B')
class C(B,A):
    pass

c=C()
c.hello()

class C(A,B):
    pass
c=C()
c.hello()