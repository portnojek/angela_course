#PODSTAWOWE TESTY
'''pytest -v => widok wykonanego testu z postępem oraz tytułem testu
 uruchamianie testów"
 pytest - wiadomka, leci po całości
 pytest tests - uruchomi wszystkie testy z katalogu tests
 pytest -k dajCyfry -v => uruchamia testy, które zaiwerają określony ciąg znaków - służy do tego '-k' po którym wpisujemy fragment nazwy
 pytest -m szczegolwe -v => leci z testami po dekoratorach i zwraca testy które zostały wykonane z nazwy
 pytest test_modulik.py --cov --cov-report=html - tworzy katalog htmlcov a tam mamy plik index.html i możemy go sobie w przeglądarce odpalić - i jest fajnie, fajniusio

'''

#PARAMETRYZACJA TESTÓW
