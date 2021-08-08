#Makiety (Mocks) - służą zastępowaniu danych na czas testów.
from unittest import mock
makieta=mock.Mock()
makieta.pole1=20
makieta.pole2='Element tekstowy'
print('pole1={}, pole2={}'.format(makieta.pole1, makieta.pole2))

#Dynamicznie można tworzyć również metody:
from unittest import mock
makieta=mock.Mock()
makieta.pole1=20
makieta.pole2='Element tekstowy'
print('pole1={}, pole2={}'.format(makieta.pole1, makieta.pole2))

makieta.dawajPi.return_value=3.14
print(makieta.dawajPi)

'''Wyświetlenie zawartości dynamicznie tworzonych pól nikogo nie zaskakuje, to już ustaliliśmy. W
ostatnich dwóch linijkach odwołuję się jednak do czegoś co się nazywa "dawajPi". Jest to funkcja którą
dynamicznie tworzę dla obiektu makiety. Z pomocą linii:
makieta.dawajPi.return_value=3.14
Tworzę i deklaruję zwracaną wartość tejże funkcji. Takie obiekty możesz teraz użyć do testów, w
miejsce danych pobieranych np. z bazy w której w ramach testów nie chcielibyśmy mieszać.'''

#Dane testowe - biblioteka Faker

from unittest import mock
import faker

m=mock.Mock()
f=faker.Faker()

m.losowaOsoba=f.name()
m.losowaSentencja=f.sentence()
m.losowaData=f.date()

print(m.losowaOsoba)
print(m.losowaSentencja)
print(m.losowaData)

import faker
bull=faker.Faker()
plik = open('/home/bartek/Desktop/fakeDane.csv', encoding='utf-8', mode='w')
dane = []
for i in range(100):
    plik.writelines("{} {}\n".format(bull.name(), bull.date()))
plik.close()