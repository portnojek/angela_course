#Dekorator to jeden ze strukturalnych wzorców projektowych. Pozwala na dynamiczne dodanie nowej funkcjonalności do istniejącej klasy podczas działania programu.

#Przypomnienie - funkcja jako argument

def obrob(fun,a,b):
    print (fun(a,b))

def dodaj(a,b):
    return a+b

def odejmij(a,b):
    return a-b

obrob(dodaj,10,5)
obrob(odejmij,10,5)

#Przypomnienie - fnkcja w funkcji

def zewnetrzna():
    def wewnetrzna(a,b):
        return a*b
    x=wewnetrzna(4,5)
    return x
print(zewnetrzna())

#Przypomnienie - zwracanie funkcji z funkcji

def zewnetrzna():
    def wewnetrzna(a, b):
        return a * b
    return wewnetrzna

x = zewnetrzna()
print(x(9, 4))

'''Dekorator to funkcja, która przyjmuje przez argment dekorowaną funkcję, tworzy wewnętrzną funkcję, która nadpisuje działanie fnkcji dekorowanej
a następnie zwraca tą funkcją wewnętrzną:'''

def doopakowania():
    print('do opakowania')

def dekorator(fun):
    def opakowujaca():
        print('opakowujaca')
        fun()
    return opakowujaca

#kolejny dekorator
def dekorator(fun):
    def wewnetrzna():
        print('jakieś dodatkowe działania')
        fun()
    return wewnetrzna

@dekorator
def funkcja():
    print('jestem funkcją')

funkcja()

#Dekorowanie funkcji z parametrami
def dekorowana(x):
    print(f'siema {x}')

def dekorator(fun):
    def wewn(x):
        print('przed')
        fun(x)
        print('po')
    return wewn

d=dekorator(dekorowana)
d('Andrzej')

#Dekorator może przyjmować argumentu również jako *args lub **kwargs

def funkcja(imie):
    print(f"Hello {imie}!")

def dekorator(fun, *args):
    def wewn():
        print('dekoracja')
        fun(*args)
    return wewn

f=dekorator(funkcja, 'Andrzej')
f()

#Alternatywny sposób tworzenia dekoratora:

def dekorator(fun, *args):
    def wewn(*args):
        print('dekoracja')
        fun(*args)
    return wewn

@dekorator
def funkcja(imie):
    print(f"hello {imie}!")

def zdokomuentacja():
    """to jest dokumentacja tej funkcji"""
    pass

help(zdokomuentacja)
print(zdokomuentacja.__doc__)