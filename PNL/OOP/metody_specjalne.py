'''W klasach Pythona możemy deklarować metody specjalne - czyli taki które spełniają specjalną
funkcję. Umożliwiają one na przykład określenie na przykład co ma się wydarzyć gdy dodasz do siebie
dwa obiekty (przeciążanie operatorów), gdy zechcesz je zamienić na ciąg tekstowy, czy co ma się stać
gdy obiekt jest tworzony. Wszystkie funkcje specjalne zaczynają się i kończą podwójnym znakiem "_".'''

#__init__

'''Funkcja wywoływana automatycznie przy tworzeniu obiektu. Pozwala ona na inicjowanie np
atrybutów tworzonego obiektu. Programistom innych języków może się to skojarzyć z konstruktorami,
słusznie - choć funkcja "__init__" konstruktorem nie jest. Może być wykorzystywany jako
konstruktor, ale warto pamiętać że funkcja "__init__" wywoływana jest już PO stworzeniu obiektu.
Taka drobna różnica, ale powodująca że ta funkcja nie jest konstruktorem formalnie.'''


class Samochod():
    def __init__(self):
        print('to jest samochod')

s=Samochod()

'''Tym razem moja klasa ma dwa pola: "marka" i "model". Wewnątrz funkcji "__init__" inicjalizuję
wartości tych pól. Po stworzeniu obiektu i wypisaniu zawartości pól na konsoli widzimy że pola
przybrały wartości określone w funkcji "__init__".
"__init__" musi otrzymywać przez parametr obiekt reprezentujący "siebie". Nie musi się on nazywać
akurat "self", możesz go nazwać choćby "ja". Jest on potrzebny by móc się odnosić do atrybutów i
"Python na luzie" v. 1.6 - Andrzej Klusiewicz - www.jsystems.pl
173/269funkcji obiektu. Podajemy go tylko na etapie deklaracji funkcji "__init__", nie przekazujemy przy
wywołaniu konstruktora ( s=Samochod() ), jest on podstawiany automagicznie.'''

class Samochod:
    marka=None
    model=None
    def __init__(self):
        self.marka="nie podano"
        self.model="nie podano"

s = Samochod()
print(s.marka,s.model)

class Samochod:
    marka=None
    model=None
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
        
s = Samochod("Renault","Kadjar")
print(s.marka,s.model)

#__str__
'''jej zadaniem jest zwracanie obiektu w postaci tekstowej'''

class Samochod:
    marka=None
    model=None
    def __str__(self):
        return "marka={} model={}".format(self.marka,self.model)

s=Samochod()
print(s)


#__add__ i przeciążanie operatorów

class Samochod:
    marka=None
    model=None
    def __add__(self, other):
        return "Kraksa 2 Sebastianów w dresie. Jeden jechał {}, drugi {}".format(self, other)
    def __init__(self, marka, model):
        self.marka=marka
        self.model=model
    def __str__(self):
        return "marka={} model={}".format(self.marka,self.model)

s=Samochod("Audi","A4")
print(s)
s2=Samochod("Bmw","e46")
s3=s+s2
print(s3)

#__getitem__ i __setitem__
'''Funkcje __getitem__ i __setitem__ umożliwiają stworzenie własnego tworu zbliżonego do list czy
słownika.'''

class MyDictionary:
    dict=dict()
    def add_element(self,key,value):
        self.dict[key]=value
    def get_element(self,key):
        return self.dict[key]

md=MyDictionary()
md.add_element('A',1000)
print(md.get_element('A'))


class MyDictionary:
    dict=dict()
    def __setitem__(self,key,value):
        self.dict[key]=value
    def __getitem__(self,key):
        return self.dict[key]

md=MyDictionary()
md['klucz']='wartość'
print(md['klucz'])
'''Teraz możemy naszą klasę wzbogacić o elementy których w tradycyjnych słownikach nie ma'''




