def policz_znaki(napis, znak_start="<", znak_stop=">"):
    licznik = 0
    czy_liczymy = False
    for znak in napis:
        if znak == znak_start:
            czy_liczymy = True
        elif znak == znak_stop:
            czy_liczymy = False
        elif czy_liczymy:
            licznik += 1
    return licznik

def test_pojedyncze_znaczniki_domyslne():
    assert policz_znaki("ala ma <kota> a kot ma ale") == 4
