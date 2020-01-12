
from pojazd_1 import tororwe,kolowe
import przystanki

def main():

    linie = [
        kolowe.Autobus(520),
        kolowe.Autobus(530),
        kolowe.Autobus(540),
        tororwe.Tramwaj(21),
        tororwe.Tramwaj(14),
        tororwe.Tramwaj(7)
         ]
    print (zbuduj_rozklad(linie))


if __name__ == " __main__":
    main()
