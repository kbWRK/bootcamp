n = "ala ma kota kot ma ale ala go kocha kot ją wcale"


# litera = {}


def wn(n, l):
    ilosc_wystapien = {}
    for litera in n:
        ilosc_wystapien[litera] = ilosc_wystapien.get(litera, 0) + 1
    wybrane = set()
    for litera, wystapienia in ilosc_wystapien.items():
        if wystapienia > l:
            wybrane.add(litera)
    return wybrane
    # for liT,
    # for lit, il in liT.items():
    #     print(f"- {lit!r} : {il}")


print(wn(n, 3))


def test_funkcja_chodzi():
    assert wn("ala ma kota kot ma ale ala go kocha kot ją wcale", 2) == {'a', 'l', 'k', 'o', ' '}
