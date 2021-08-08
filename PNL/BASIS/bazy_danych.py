#łączenie z postgresem

import psycopg2
polaczenie=psycopg2.connect(host="jsystems.pl",database="demo",user="demo",password="demo",port=5432)

# #łączenie z Oracle
# import cx_Oracle
# polaczenie = cx_Oracle.connect('uzytkownik/haslo@host/baza_danych')

#wykorzystanie SELECT - wynikiem takiego zapytania (ciekawe czy każdego) są krotki
import psycopg2
polaczenie=psycopg2.connect(host="jsystems.pl",database="demo",user="demo",password="demo",port=5432)
kursor = polaczenie.cursor()
sql="select * from owoce"
kursor.execute(sql)
for w in kursor:
    print(w)
kursor.close()

#odczytanie tylko 2 kolumny:
import psycopg2
polaczenie=psycopg2.connect(host="jsystems.pl",database="demo",user="demo",password="demo",port=5432)
kursor = polaczenie.cursor()
sql="select * from owoce"
kursor.execute(sql)
for w in kursor:
    print(w[1])
kursor.close()

#Wstawianie, zmiana i kasowanie danych, oraz operacje DDL
import psycopg2
polaczenie=psycopg2.connect(host="jsystems.pl",database="demo",user="demo",password="demo",port=5432)
kursor = polaczenie.cursor()
sql="insert into owoce(nazwa) values ('Granat')"
kursor.execute(sql)
polaczenie.commit() #commit służy do zatwierdzania transakcji. Jeśli tego nie wstawimy to nie bedzie widoku na tabeli utrwalone
kursor.close()

#dynamicznie generowana wartość
kursor = polaczenie.cursor()
sql="insert into owoce(nazwa) values ('Arbuz') returning numer"
kursor.execute(sql)
id=str(kursor.fetchone()[0])
print('id='+id)
polaczenie.commit()
kursor.close()