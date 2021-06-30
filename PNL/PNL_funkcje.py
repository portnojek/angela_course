'''Wartości parametrów można podmieniać wewnątrz funkcji - nie są tylko do odczytu jak w
niektórych językach programowania. Przykładowo poniższa funkcja zawsze będzie witała
Czesława, niezależnie od tego co podamy przy wywołaniu:'''


def sayHello(imie):
    imie="Czesław"
    print("Hello my friend {}!".format(imie))

sayHello("Bogna")

def sprawdz_typ(x):
    if(isinstance(x, int)):
        print("to jest liczba całkowita")
    else:
        print("to nie jest liczba całkowita")

sprawdz_typ("BaRTEK")

print(type(True))

def domyslne_wartosci(a="brak",b="brak"):
    print('a='+a)
    print('b='+b)
domyslne_wartosci()
domyslne_wartosci("X","Y")
domyslne_wartosci()
domyslne_wartosci("coś")
domyslne_wartosci(b="coś innego")

def oddaj0():
    return 0

print(oddaj0())
x=oddaj0()
print(x)

def dajcyferki():
    l=list(range(10))
    return l

dajcyferki()

#lambda
fun = lambda a, b: a + b
print(fun(10, 20))

#funkcja jako argument innej funkcji
def razy2(a): # funkcja która będzie użyta jako argument
    return a*2


def funkcja_jako_argument(f,x):
    print(f(x))
funkcja_jako_argument(razy2,33)

def powieksz(x):
    return x.upper()

def zastosuj_dla_wszystkich(fun,*args):
    for a in args:
        print(fun(a))
zastosuj_dla_wszystkich(powieksz,'siała','baba','mak')


#Funkcje jako listy
def pomnoz_razy_dwa(x):
    return x*2

def podziel_przez_trzy(x):
    return x/3

def dodaj_piec(x):
    return x+5

funkcje=[pomnoz_razy_dwa,podziel_przez_trzy,dodaj_piec]

def obrob(wartosc,*funkcs):
    for f in funkcs:
        wartosc=f(wartosc)
    return wartosc
print(obrob(2,pomnoz_razy_dwa,podziel_przez_trzy,dodaj_piec))

#Funkcja w funkcji
def zewnetrzna(x):
    def wewnetrzna(x):
        return x*2
    print(wewnetrzna(x))
zewnetrzna(50)

#Zwracanie funkcji z funkcji
def wybierz(tryb):
    def powieksz(x):
        return x.upper()
    def pomniejsz(x):
        return x.lower()
    if tryb==1:
        return powieksz
    elif tryb==2:
        return pomniejsz

funkcja=wybierz(1)
print(funkcja('Witaj Świecie!'))
funkcja=wybierz(2)
print(funkcja('Witaj Świecie!'))

#Zwracanie funkcji z funkcji pt. 2
def daj_funkcje(x):
    def podwoj(a):
        return a*2
    def polowa(a):
        return a/2
    if x==1:
        return podwoj
    elif x==2:
        return polowa
fun=daj_funkcje(1)
print (fun(6))

#Rekurencja - wywołanie funkcji przez samą siebie aż do uzyskania określonego wyniku
def silniaRek(n):
    if n==0:
        return 1
    else:
        return n*silniaRek(n-1)

print(silniaRek(8))

def rekurencyjny_wypisywacz(n):
    print(n)
    if n>0:
        rekurencyjny_wypisywacz(n-1)
    else:
        return n
    return n
rekurencyjny_wypisywacz(10)

#*args - dane z dowolna liczbą argumentów pozycyjnych
def args(*args):
    for a in args:
        print(f'{a}')

args(1, 2, 3, 4, 5)

def powiekszacz(*slowa):
    for s in slowa:
        print(s.upper())

powiekszacz("twoja", "rzecz", "mój", "problem")

def dlakazdego(param1,*args):
    print(f'param1={param1}')
    for a in args:
        print(a)
dlakazdego('pierwsza wartość','pierwszy arg','drugi arg', 3)

def argi(*args):
    for e in args:
        print(e)
argi(*[1,2,3,4],'coś')

#kwargs - jeśli chcemy wpisać dowolną ilość parametrów klucz - wartość
def parameter_kwargs(**kwargs):
    for k in kwargs:
        print(k, kwargs[k])

parameter_kwargs(pierwszy=48, kolejny=43, jeszczekolejny=12)

def kwargs(**parametry):
    print(parametry)
kwargs(param1=1,param2=2,param3=3)

#jesli do kwargs chcemy jeszcze dodatkowe parametry przekazac to musimy wymienić je jako pierwsze
def kwargs_parametr(argument, **kwargs):
    print(argument)
    print(kwargs)

kwargs_parametr(argument=10,param1='Andrzej',param2='Klusiewicz')

def zapisz_parametry_do_pliku(nazwa_pliku,**parametry):
    plik=open("/home/bartek/Dokumenty/test.csv",mode='w', encoding='utf-8')
    for p in parametry:
        plik.write(f'{p};{parametry[p]}\n')
    plik.close()
zapisz_parametry_do_pliku('mojplik.csv',parametr1='wartość 1',parametr2=2)

from datetime import datetime
import time

def czekacz():
    time.sleep(1)
    return 1

poczatek = datetime.now()
for x in range (10):
    czekacz()
koniec = datetime.now()
print(koniec-poczatek)
