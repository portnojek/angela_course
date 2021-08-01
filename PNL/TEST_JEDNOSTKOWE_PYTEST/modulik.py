podpietaBaza=None
def podepinijBaze(nazwa):
    global podpietaBaza
    podpietaBaza=nazwa

def wykonajZapytanie():
    global podpietaBaza
    print("Wykonuję zapytanie z użyciem bazy {}")
    if (podpietaBaza=='MS SQL'):
        raise Exception('FU')
    return "ok"

    
