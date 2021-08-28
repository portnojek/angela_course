'''metody statyczne to takie, które możemy wywołać nie tworząc obiektu klasy'''

class Ms:
    def zwykla(self):
        print('hej, jestem zwykla metodą')
        pass

    @staticmethod
    def statyczna():
        print('hej, jestem statyczną metodą')
        pass

ms=Ms()
ms.zwykla()
Ms.statyczna()

'''Aby wywołać metodę "zwykla", musimy powołać do życia obiekt klasy Ms i z niego dopiero wywołać
tę metodę. Klasa Ms może jednak mieć bardzo wiele pól, lub pola które są od razu inicjalizowane dużą
ilością danych, a to nie koniecznie musi być pożądany przez nas skutek. My chcemy tylko wywołać
metodę która akurat znajduje się w tej klasie. W takiej sytuacji możemy wykorzystać właśnie metodę
statyczną. Przyjrzyj się wywołaniu "Ms.statyczna()" - wywołuję tę metodę z klasy a nie z obiektu (!!)
"ms", który odróżnić można po wielkości liter. Zwykłej metody w ten sam sposób wywołać nie mogę.
Metoda statyczna staje się taką za sprawą 2 rzeczy - adnotacji "staticmethod", oraz faktu nie podania
parametru "self".'''

'''W zasadzie to jest jedna sztuczka na wywołanie metody niestatycznej tak jak statycznej, może nawet
warto ją znać, ale raczej nie będziesz jej często stosować. By tak się dało zrobić, przy wywołaniu
metody zwykłej z klasy (a nie z obiektu!) jako jej parametr podajemy "None":'''
class Ms:
    def zwykla(self):
        print('hej, jestem zwykłą metodą')
        pass

    @staticmethod
    def statyczna():
        print('hej, jestem metodą statyczną')
        pass

Ms.zwykla(None)

'''i wszystko działa poprawnie, ale tylko dlatego że w metodzie "zwykla" nie odwołuję się do żadnych
atrybutów ani metod obiektu.'''