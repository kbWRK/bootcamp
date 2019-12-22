def obsługa_kantoru():
    operacja = input("chcesz kupic albo sprzedac? [s/k]")
    if operacja == "k":
        ...
    elif operacja == "s":
        ...
    else:
        raise Exception("podana nie wałasciwa operacja")
print("poczatek programu")
try:
    kwota = obsługa_kantoru()
    print("kolejna linijka w try")
except ValueError:
    print("podana zła wartosc")
print("koniec")

