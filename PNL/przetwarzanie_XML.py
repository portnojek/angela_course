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