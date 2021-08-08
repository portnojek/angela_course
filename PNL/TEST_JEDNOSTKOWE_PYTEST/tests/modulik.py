'''Test zgodnie z oczekiwaniami nie przeszedł, mamy też informację w którym miejscu pojawił się
wyjątek. Same testy jednak nie mówią nam dla jakiej wartości nastąpił ten wyjątek. Dodałem sobie
drukowanie informacji o podpiętej bazie, i tylko po tym mogę ewentualnie poznać na której bazie się
wyłożył test. Ponadto, jeśli na jednej bazie testy polegną, to nie przejdą do sprawdzania kolejnych,
tylko zostaną przerwane'''

podpietaBaza=None
def podepinijBaze(nazwa):
    global podpietaBaza
    podpietaBaza=nazwa

'''zmodyfikowany temat - Aby rozwiązać oba te problemy, wykorzystamy dekorator
"@pytest.mark.parametrize". Mała przeróbka modułu testowego:'''


def wykonajZapytanie():
    global podpietaBaza
    print("Wykonuję zapytanie z użyciem bazy {}")
    if (podpietaBaza=='MS SQL'):
        raise Exception('FU')
    return "ok"

'''Powyższa funkcja będzie testowana tylukrotnie, ile wartości znajdzie się na liście "dbs". Dla każdej
wartości pytest wygeneruje osobny test. Tym razem funkcja przyjmuje bazę danych przez parametr (w
miejsce iteracji po liście baz wewnątrz funkcji). Wartość dla tego parametru zostaje podana dzięki
dekoratorowi "@pytest.mark.parametrize". Pierwszym parametrem tego dekoratora jest nazwa
parametru do którego wstrzykujemy wartość, drugim lista (lub inna kolekcja po której da się iterować)
z której będą pobierane wartości do testów. Pytest dla każdej wartości w kolekcji "dbs" wywoła funkcję
test_podepnijBaze raz, podając przez argument funkcji tę wartość.'''    


