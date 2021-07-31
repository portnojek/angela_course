#WYRAŻENIA REGULARNE
'''pozwala odnaleźć i wyciąć wszystkie pasujące elementy wg zadanych wzorcow'''
#funkcja findall

import re
teskt = 'siała baba mak i dostała 10 lat'
wzorzec = 'baba'
print(re.findall(wzorzec, teskt))

#typy znaków
'''
zestawienie symboli, które pozwalają nam odnajdować elementy

Symbol Opis
\d Cyfry
\D Znaki nie będące cyfrą
\w Alfanumeryki
\W Wszystko co nie jest alfanumerykiem
\s Białe znaki
\S Wszystko co nie jest białym znakiem
. Dowolny znak
[a-f] Małe litery z zakresu a-f
[A-F] Duże litery z zakresu A-F
[0-3] Cyfry z zakresu 0-3
[a-z0-6] Małe litery z zakresu a-z lub cyfry z zakresu 0-6
[^a-f] Elementy nie zawierające się w zbiorze małych liter w zakresie a-f

'''
#kwantyfikatory ilościowe 
'''
Poniżej zestawienie symboli określających krotność wystąpień poszukiwanego elementu
Kwantyfikator Opis
* Dowolna ilość znaków - w tym zero!
+ Co najmniej jedno wystąpienie - ale może być też więcej!
? Jedno lub zero wystąpień - ale nie więcej
{1,5} Od jednego do pięciu wystąpień
{5,} Co najmniej 5 wystąpień
{,5} Nie więcej niż 5 wystąpień

'''

#wykorzystanie symboli i kwantyfikatorów do wyszukiwania elementów według wzorca
import re

tekst='Badanie statystyczne 565 dzieł sztuki różnych wielkichmalarzy, przeprowadzone w 1999, wykazało, że ci artyści nie użyli złotego podziału w wymiarach swoich płócien.' \
'Badanie stwierdziło, że średni stosunek dwóch boków badanych obrazów wynosi 1,34, ze średnimi dla poszczególnych malarzy obejmującymi od 1,04 (Goya) do 1,46 (Bellini)[35].' \
'Z drugiej strony, Pablo Tosto wymienił ponad 350 dzieł znanych artystów, z których ponad 100 miało płótna o proporcjach złotego prostokąta i pierwiastka z 5, natomiast inne' \
' proporcje takie jak pierwiastki z 2, 3, 4 i 6[36]. '

wzorzec='\d'

print(re.findall(wzorzec, tekst))

#a teraz wyciągnięcie liczb bez przecinków, które mają 3 i 4 cyfry w sobnie
'''We wzorcu mamy symbol "\d" oznaczający wyszukiwanie cyfr, oraz kwantyfikator
ilościowy "{3,4}" określający ilość wystąpień od 3 do 4. Kwantyfikator ilościowy odnosi się do
poprzedzającego elementu.'''

wzorzec='\d{3,4}'
print(re.findall(wzorzec, tekst))

#i kolejne
'''znajdz element składający się z jednej cyfry, po którym następuje przecinek, po którym następują dwie kolejne cyfry'''

wzorzec='\d,\d{2}'

print(re.findall(wzorzec, tekst)) #niby ok ale nic mi tu nie wychodzi (a jednak wychodz, po przecinku nie może być spacji)

#a teraz wyciągnięcie nr telefonu
'''Co oznacza wzorzec "[\d ]{9,}"? Element składający się z cyfr albo spacji o długości co najmniej 9
znaków. Może się też pojawić sytuacja w której mamy do wyszukania jakieś znaki mogące być
potraktowane jako znaki specjalne np. ".". W takie sytuacji należy wyłączyć ich specjalne znaczenie za
pomocą znaku "\".'''

import re
tekst='''Pod tym numerem możesz zamówić kebsika: 22 299 53 69. Trzeba
prosić do telefonu Panią Bożenkę. '''
wz='[\d ]{9,}'
print(re.findall(wz, tekst))
