import json

dane={
    "imie":"Andrzej",
    "nazwisko": "Klusiewicz",
    "adres": {
             "miasto": "Warszawa",
             "kod": "02-019"
             },
    "jezyki": ["polski","angielski","Java","R","Python","PL/SQL"]
    }

plik = open('/home/bartek/Dokumenty/Python/angela_course/PNL/dane.json', encoding='utf-8')
obj=json.load(plik) 
print(obj)
print(type(obj))
plik.close()

print(obj['imie'])

for k in obj.keys():
     print(k)

#co jesli JSON jest bardziej zlozony?
print(obj['adres']['miasto'])

for j in obj['jezyki']:
    print(j)

print(obj['jezyki'][2])

#Tworzenie i zapisywanie danych JSON do pliku
obj = dict()
obj['ksiazka']='Finansowy Ninja'
obj['film_na_wieczor']='https://www.youtube.com/watch?v=sCNrK-n68CM'
obj['banknoty']=[10,20,50,100,200,500]
plik = open('/home/bartek/Dokumenty/Python/angela_course/PNL/jsonout.json', encoding='utf-8', mode='w')
json.dump(obj, plik)
plik.close()

#Alternatywnie mogę po prostu ręcznie zadeklarować sobie słownik i zainicjalizować go danymi pisanymi jako całość:
import json
dane={
    "ksiazka": "Finansowy Ninja",
    "film_na_wieczor": "https://www.youtube.com/watch?v=sCNrK-n68CM",
    "banknoty": [10,20,50,100,200,500]
}
plik=open('/home/bartek/Dokumenty/Python/angela_course/PNL/jsonout2.json',encoding='utf-8',mode="w")
json.dump(dane,plik)
plik.close()