def polo_trapezu(wysokosc, podstawa1, podstwa2):
    return wysokosc * (podstawa1 + podstwa2) / 2

def pole_elipsy(promien=1, rozciagniecie=1):
    return (3.14*promien**2)*rozciagniecie

def test_argumenty_pozycyjne():
    assert polo_trapezu(10, 3, 6) == 45

def test_elipsa_Z_rozciagnieciem():
    assert pole_elipsy(1,2) == 3.14*2
def test_elipsa_Z_rozciagnieciem_0():
    assert pole_elipsy() == pole_elipsy(1,1)

def test_nazwane():
    assert polo_trapezu(wysokosc=10, podstawa1=3, podstwa2=6) == 45


def test_nazwane_pomiesznae():
    assert polo_trapezu(wysokosc=10, podstwa2=6, podstawa1=3) == 45


def test_argumenty_nazwane_i_nie_nazwane():
    assert polo_trapezu(10, 3, podstwa2=6) == 45
    assert polo_trapezu(10, podstawa1=3, podstwa2=6 ) == 45
