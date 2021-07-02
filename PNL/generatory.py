'''Generator jest funkcją która może zostać wstrzymana i wznowiona od miejsca w którym została
wstrzymana. Generatory cechują się leniwą ewaluacją. Tworzą kolejne elementy dopiero w momencie
odwołania się do generatora. Pozwala nam to wydajniej wykorzystywać pamięć operacyjną i zwracać z
generatora nieskończoną liczbę elementów'''

'''Słowo kluczowe „yield” odpowiada za przerwanie wykonania funkcji, zapisanie jej aktualnego stanu i
zwrócenie kolejnej wartości.'''

def myrange(n):
    for x in range(n):
        yield x*10

for x in myrange(10):
    print(x)

#Generator, który podaje tyle potęg kolenych liczb ile otrzyma przez argument:
def potegi2(n):
    for x in range(1, n + 1):
        yield pow(2, x)

for p in potegi2(5):
    print(p)

def dziesieci():
    i=1
    while True:
        yield i*10
        i+=1

dz=dziesieci()
print(dz.__next__())
print(dz.__next__())
print(dz.__next__())   

dz=dziesieci()
print(next(dz))
print(next(dz))
print(next(dz))

def poryRoku():
    pory = [
            'styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec',
            'sierpień', 'wrzesień', 'październik',
            'listopad', 'grudzień'
            ]
    for e in pory:
        yield e

for p in poryRoku():
    print(p)

def parzyste(n):
    for x in range(n + 1):
        yield 2 * x
for p in parzyste(10):
    print(p)

def literki():
    for x in range(97,123):
        yield(chr(x))
for l in literki():
    print(l)

#fajny przykład generatora, który zczytuje plik csv i rozbija wartości
def rozbijacz_csv(np,r):
    plik=open(np,encoding='utf-8')
    while True:
        linia=plik.readline()
        if not linia:
            break
            yield linia.strip().split(r)

rc=rozbijacz_csv('plik.csv',';')
print(next(rc))
print(next(rc))