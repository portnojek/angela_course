#weryfikacja domyślnego kodowania
# import locale
# print(locale.getpreferredencoding)

# plik = open('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt', encoding='utf-8')

#Mamy takie możliwości odczytu zawartości pliku:

import os

#wskaże w bajtach jak duży jest plik

ile = os.path.getsize('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt')
print(ile)

'''
read() - odczytuje plik jako jeden ciągły tekst typu 'str'
readlines() - podobna do read bo zczytuje cały plik z tą różnicą, że każda linika znajdzie się w kolejnym elemencie listy
readline() - słuzy do odczytania pliku linia po linii. Przydaje się jesli nie chcesz całego pliku wertować.
'''
#read
pl = open('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt', encoding='utf-8')
linie = pl.read()
pl.close()
print(linie)
print(type(linie))

#możemy też wskazać ile znaków ma być wczytanych

plik = open('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt', encoding='utf-8')
linie = plik.read(20)
print(linie)
print("----------------")
linie = plik.read(20)
print(linie)

#readlines
pl = open('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt', encoding='utf-8')
linie = pl.readlines()
pl.close()
print(linie)
print(type(linie))

#jeśli nie chcemy znaku końca linii - funkcja read
pl=open('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt', encoding='utf-8')
linie=pl.read().splitlines()
pl.close()
print(linie)
print(type(linie))

#readline()
#taka o konstrukacja pozwalająca czytać plik linia po linii

with open('/home/bartek/Dokumenty/pythonowe_pliczki/dane.txt', encoding='utf-8') as f:
    for l in f:
        print(l)
f.close()

#funkcja seek() - funkcja ta przesuwa kursor do wskazanej pozycji - numer znaku w pliku. Jeśli podamy bez parametr przyjmie domyślnie wartość 0.


