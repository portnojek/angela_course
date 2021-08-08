import xml.etree.ElementTree as et
tree=et.parse('/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml')

#wyszukiwanie elementu po nazwie
root=tree.getroot()
imie=root.find('imie')
adres=root.find('adres')
miasto=adres.find('miasto')
print(miasto.text)
print(imie.text)
print(type(imie.text))

#wyszukiwanie elementu po pozycji
import xml.etree.ElementTree as et
drzewko=et.parse('/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml')
korzonek=drzewko.getroot()
drugi=korzonek[1].text
print(drugi)

#wyszukiwanie elementu po pozycji
import xml.etree.ElementTree as et
drzewko=et.parse('/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml')
korzonek=drzewko.getroot()
zag=korzonek[3][1].text
print(zag)

#wyszukiwanie wszystkich elementów wg tagów
import xml.etree.ElementTree as et
d=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml")
root=d.getroot()
for e in root.findall('jezyki'): # tylko po elementach "jezyki"
    print(e.text)

#więcej niż jeden element
import xml.etree.ElementTree as et
d=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml")
root=d.getroot()
print (root.findall('jezyki')[1].text)

#atrybuty
import xml.etree.ElementTree as et
tree=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml")
root=tree.getroot()
nazwisko=root.find('nazwisko')
print(nazwisko.attrib)

import xml.etree.ElementTree as et
tree=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml")
root=tree.getroot()
nazwisko=root.find('nazwisko')
print(nazwisko.attrib['param'])

#lub krócej
import xml.etree.ElementTree as et
print(et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot().find("nazwisko").attrib['param'])

#SZTUCZKI
#odczytywanie XML jako zwykły tekst - tostring
import xml.etree.ElementTree as et
drzewko= et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml")
korzen = drzewko.getroot()
print(et.tostring(korzen))

#sprawdzanie nazwy elementu
import xml.etree.ElementTree as et
r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag, e.attrib, e.text)

#Modyfikowanie  drzewka XML
#modyfikowanie zawartości element

import xml.etree.ElementTree as et

r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag,e.text)
r.find('nazwisko').text="Klusiewicz po zmianie"
print("-------------------")
for e in r:
    print(e.tag,e.text)

#dodawanie i modyfikowanie atrybutów element - za pomocą "attrib". Jeśli nie istnieje to doda, jeśli istnieje to nadpisze
import xml.etree.ElementTree as et
r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag,e.text,e.attrib)
r.find('nazwisko').attrib['encoding']="utf-8"
print("-------------------")
for e in r:
    print(e.tag,e.text,e.attrib)

#tworzenie nowych elementów - korzystamy z "SubElement" z modułu ElementTree
import xml.etree.ElementTree as et
r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag,e.text,e.attrib)
nowy=et.SubElement(r,"masa")
nowy.text=78
print("-------------------")
for e in r:
    print(e.tag,e.text,e.attrib)

#gdybyśmy chcieli dodać element w wybranym przez nas miejscu to użyjemy funkcji "insert". Przyjmuje dwa parametry: pozycja (w tym przypadku pierwsza), drugi to element który ma zostać dodany.
import xml.etree.ElementTree as et
r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag,e.text,e.attrib)
nowy=et.Element("samochod")
nowy.text="Renault"
r.insert(0,nowy)
print("-------------------")
for e in r:
    print(e.tag,e.text,e.attrib)

#usuwanie elementów
#kasować możemy wskazując pozycję
import xml.etree.ElementTree as et
r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag,e.text)
del r[0]
print("-------------------")
for e in r:
    print(e.tag,e.text)

#lub po nazwie
import xml.etree.ElementTree as et
r=et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml").getroot()
for e in r:
    print(e.tag,e.text)
naz =r.find('nazwisko')
r.remove(naz)
print("-------------------")
for e in r:
    print(e.tag,e.text)

#Zapis drzewa XML do pliku - właściwie tak samo się odbywa jak zapis do pliku tekstowego.
#Poniższy przykład wykorzystuje w funkcję write wbudowaną w element
import xml.etree.ElementTree as et
d = et.parse("/home/bartek/Dokumenty/Python/angela_course/PNL/dane.xml")
d.write("/home/bartek/Dokumenty/Python/angela_course/PNL/dane2.xls", encoding='utf-8')
