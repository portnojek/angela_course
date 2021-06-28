#append, insert, del, itemgetter (po imporcie modułu operator)

import operator

from operator import itemgetter
furki=[[3,"Renault"],[2,"Citroen"],[1,"Audi"],[4,"Zaporożec"]]
furki.sort(key=itemgetter(1))
print(furki)


#Funkcja map - każdy element listy przetwarzany - do listy parzyste wpadają elementy listy liczby pomnożone przez 2
liczby = [i for i in range(1, 11)]
parzyste = list(map(lambda x:x*2, liczby))
print(parzyste)

# Zasadniczo zapis:
# lambda x:x*2
# Byłby odpowiednikiem
# def funkcja(x):
# return x*2

#Funkcja filter jak sama nazwa wskazuje, służy do filtrowania zawartości list.
liczby2 = [i for i in range(1, 21)]
parzyste2 = list(filter(lambda x: x%2==0, liczby2))
print(parzyste2)

krotkaParzyste2 = tuple(parzyste2)
print(krotkaParzyste2)

#słowniki
slownik={}
slownik2=dict()
info={
"LG123": "Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam",
"SONY666": "Piekielnie dobry telewizor",
"SZAJSUNG999": "Telewizor świetnie nadający się do zakrycia dziury w ścianie (i niczego więcej)"
}
print(info["SZAJSUNG999"])

for i in info:
    print(info[i])

for k in info.keys():
    print(info[k])

#dodawania wartości do słownika (jeśli istnieje taki klucz to zostanie nadpisany)

info["KLUCZ"]="WARTOŚĆ"

print(info)

#kasowanie elementu
del info["LG123"]

print(info)

#zestawy - zbiory elementów bez powtórzeń w zestawie żadna wartośc nie może się powtórzyć, są użyteczne do usuwania duplikatów, automatycznie się sortują...
z={}
z2=set()

z3={1,3,2,1,5,1}
print(z3)

z4={(1,"A"),(2,"B"),(1,"C"),(1,"A")}
print(z4)


#modyfikowanie zawartości zestawów

s={1,2,3,4}
s.add(5)
s.remove(1)
print(s)
s.clear()
print(s)
s.add(34)
print(s)
s.add(12)
print(s)
s.add(12)
print(s)
print(list(s))
lista_krotka = list(s)
print(lista_krotka)
print(set(lista_krotka))

#obsluga wyjatkow
try:
    print(1/0)
except:
    print("nie zabanglało")
print("dalej")

try:
    print(1/0)
except ZeroDivisionError:
    print("nie można dzielić przez zero!")

try:
    print(1/0)
except ZeroDivisionError:
    print("nie można dzielić przez zero!")
except:
    print("jakiś inny błąd")

try:
    print(1/0)
except(ZeroDivisionError,IOError):
    print("albo to, albo to")

try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)

#Może się też tak zdarzyć że będziemy chcieli wykonać jakąś czynność niezależnie od wystąpienia lub nie wyjątku. Wtedy wykorzystujemy klauzulę finally:
try:
    print(1/0)
except:
    print("wyjątek")
finally:
    print("co by się nie działo to ja się uruchamiam")

try:
    raise TypeError()
except TypeError:
    print("to było do przewidzenia...")