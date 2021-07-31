import narzedzia as n
import pytest


@pytest.mark.podstawowe
def test_sumuj():
    assert n.sumuj(5, 3) == 8

@pytest.mark.szczegolowe
def test_dajCyfryMin():
    tab=n.dajCyfry()
    assert min(tab)==1

@pytest.mark.szczegolowe
def test_dajCyfryMax():
    tab=n.dajCyfry()
    assert max(tab)==10

@pytest.mark.podstawowe
def test_dajCyfryLen():
    tab=n.dajCyfry()
    assert len(tab)==10