import modulik

def test_podepnijBaze():
    bazy=['Oracle', 'PosgreSQL', 'MS SQL', 'MySQL']
    for b in bazy:
        modulik.podepinijBaze(b)
        assert modulik.wykonajZapytanie()=='ok'
    pass


import modulik
import pytest
dbs = ["Oracle", 'PostgreSQL', 'MS SQL', 'MySQL']
@pytest.mark.parametrize('baza',dbs)
def test_podepnijBaze(baza):
    modulik.podepinijBaze(baza)
    print('{}\n'.format(baza))
    assert modulik.wykonajZapytanie()=='ok'