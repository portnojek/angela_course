class Owoc:
    pass

jablko=Owoc()
pomarancza=Owoc()
print(jablko)
print(pomarancza)
if(jablko==pomarancza):
    print('to samo')
else:
    print('inne')

'''
Ponieważ obiekty te nie posiadają żadnych pół, toteż w porównaniu nie może być brana zawartość
obiektów. Jeśli porównujesz dwa obiekty w taki sposób, w rzeczywistości sprawdzasz czy chodzi o ten
sam obiekt - w skrócie czy oba obiekty odnoszą się do tego samego adresu w pamięci operacyjnej.
Oczywiście tak nie jest, dlatego kod zwraca nam informację że obiekty są różne.
'''