# file = open("/media/bartek/Nowy/dokumenty/Bartek/Rozliczenie_kredyty/spis_kredytów.txt", "r")
# cont = file.read()
# print(cont)
# print(file.read(16))
# print(file.read(4))
# print(file.read(4))
# print(file.read())
# file.close()

# file2 = open("/media/bartek/Nowy/dokumenty/Bartek/Rozliczenie_kredyty/new_file.txt", "w")
# file2.write(input("Wpisz swoje imię i nazwisko: \n"))
# file2.write(" \n")
# file2.write(input("Wpisz datę urodzenia: \n"))
# file2.close()
# file2 = open("/media/bartek/Nowy/dokumenty/Bartek/Rozliczenie_kredyty/new_file.txt", "r")
# file2.read()
# print(file2.read())
# file2.close()


#zwraca liczbę znaków
file3 = open("/media/bartek/Nowy/dokumenty/Bartek/Rozliczenie_kredyty/new_file2.txt", "w")
msg = "To jest testowa treść wiadomości..."
amount_written = file3.write(msg)
print(amount_written)
file3.close()

#zawsze jesteś pewny ze plik jest ostatecznie zamkniety
try:
    f = open("/media/bartek/Nowy/dokumenty/Bartek/Rozliczenie_kredyty/new_file2.txt", "r")
    print(f.read())

finally:
    f.close()

#to samo tylko że z funkcją 'with'

with open("/media/bartek/Nowy/dokumenty/Bartek/Rozliczenie_kredyty/new_file2.txt", "r") as f2:
    print(f2.read())
    f2.close()

