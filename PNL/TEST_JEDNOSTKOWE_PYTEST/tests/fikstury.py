import nibyDB

def test_getData():
    nibyDB.loadDB()
    assert len( nibyDB.getData()    )>0
    pass

def test_getOne():
    nibyDB.loadDB()
    assert nibyDB.getOne(0)[1]=='Marian'
    pass

def setup_module():
    print("\n############## setup ##############")
    nibyDB.loadDB()

def teardown_module():
    print("\n############## bye ##############")

def test_getData():
    assert len( nibyDB.getData())>0
    pass

def test_getOne():
    assert nibyDB.getOne(0)[1]=='Marian'
    pass

'''Pojawiły się dwie nowe funkcje - "setup_module" i "teardown_module". Nazwy nie są przypadkowe -
pytest wywoła te funkcje automatycznie odpowiednio przed wszystkimi testami w danym module, oraz
po nich. Możemy to wykorzystać do wstępnej inicjalizacji na początku i np. wyczyszczenia danych na
końcu. Kod modułu testującego przerobiłem w taki sposób, że wywołanie funkcji "loadDB" pojawia
się tylko raz - w funkcji setup_module() zamiast w każdej funkcji testującej.'''

#Dekorator @pytest.fixture

'''Przyjrzyj się poniższemu przykładowi. W miejsce funkcji "setup_module" pojawia się funkcja
"load_stuff" - tym razem jest to nazwa wymyślona przeze mnie. Nad tą funkcją mamy dekorator
"@pytest.fixture". Ten dekorator powoduje automatyczne wywołanie funkcji "load_stuff" przed
uruchomieniem każdej z funkcji testujących która ma podane w argumencie nazwę funkcji
"load_stuff":'''

import nibyDB
import pytest

@pytest.fixture
def load_stuff():
    print("\n############## load ##############")
    nibyDB.loadDB()

def test_getData(load_stuff):
    assert len( nibyDB.getData())>0
    pass

def test_getOne(load_stuff):
    assert nibyDB.getOne(0)[1]=='Marian'
    pass

'''W powyższym przykładzie wróciliśmy do wielokrotnego ładowania bazy. Wystarczy do naszego
dekoratora dodać atrybut "scope=module" by działało to tak jak setup_module:'''

@pytest.fixture(scope='module')
def load_stuff():
    print("\n############## load ##############")
    nibyDB.loadDB()

'''Tak więc jeśli chcesz by jakaś funkcja przygotowująca dane (lub jakakolwiek inna, to przecież bez
znaczenia) była wykonywana każdorazowo przed każdą funkcją testującą to dodajesz do niej
"@pytest.fixture", a do funkcji testującej dodajesz do argumentów nazwę funkcji przygotowującej (bez
podania argumentów czy nawiasów). Jeśli zaś chcesz uruchomić funkcję przygotowującą na przed
wszystkimi testami jednorazowo, do dekoratora dodajesz ponadto "(scope="module")['''

'''Jeśli drażni Cię (podobnie jak i mnie) konieczność podawania nazwy funkcji przygotowującej jako
argument funkcji testującej, możesz wykorzystać przełącznik "autouse":'''

import nibyDB
import pytest

@pytest.fixture(autouse=True)
def load_stuff():
    print("\n############## load ##############")
    nibyDB.loadDB()
def test_getData():
    assert len( nibyDB.getData()    )>0
    pass

def test_getOne():
    assert nibyDB.getOne(0)[1]=='Marian'
    pass


'''Autouse powoduje po prostu że funkcja której dekorator dotyczy zostanie wywołana przed każdą
funkcją testującą (co stałoby się również po prostu po dodaniu tego dekoratora bez żadnych
przełączników), z tą różnicą że teraz nie będzie trzeba podawać nazwy funkcji przygotowującej jako
argument funkcji testującej. Możesz również użyć obu przełączników : autouse=True i scope='module'
w jednym dekoratorze. Skutek jest łatwy do przewidzenia. Nie trzeba będzie modyfikować
argumentów funkcji testujących, a funkcja przygotowująca zostanie wywołana raz przed wszystkimi
testami. I to jest chyba najbardziej sensowny wariant w tego typu sytuacjach. Kod całego modułu
testującego będzie wyglądał ostatecznie w ten sposób:'''

import nibyDB
import pytest
@pytest.fixture(autouse=True,scope="module")
def load_stuff():
    print("\n############## load ##############")
    nibyDB.loadDB()

def test_getData():
    assert len( nibyDB.getData())>0
    pass

def test_getOne():
    assert nibyDB.getOne(0)[1]=='Marian'
    pass

'''Po przebrnięciu przez te wszystkie przykłady czas odpowiedzieć sobie na podstawowe pytanie: Czym
więc jest fikstura? Fikstura to funkcja która przygotowuje dane, lub wykonuje czynności
inicjalizacyjne na potrzeby testów.'''

