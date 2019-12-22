import random
class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

        # TODO umiesc skarb w losowym miejscu

    def przesun(self, kierunek):
        if kierunek == "w":
            self.y += 1
        elif kierunek == "s":
            self.y -= 1
        elif kierunek == "a":
            self.x -= 1
        elif kierunek == "d":
            self.x += 1


class WojownikNocy(Pionek):
    def __init__(self,imie):
        super().__init__()
        self.imie = imie
        self.HP = 100

class BlekitnyJezdziec(WojownikNocy):
    def __init__(self, imie, HP=200):
        super().__init__(imie)
        self.HP = HP

pionki = [WojownikNocy("krystian"), WojownikNocy("mareczek"), WojownikNocy("Adi     "), BlekitnyJezdziec("komendant śmimigała")]
for pionek in pionki:
    print(f'{pionek.imie}:\t\t{pionek.x},{pionek.y}')
    print()
    for _ in range(10):
        for pionek in pionki:
            pionek.przesun(random.choice("wsad"))
for _ in range(10):
    for pionek in pionki:
        print(f'{"~"*21}\n{pionek.imie}:\t\t{pionek.x}, {pionek.y}\n{"~"*21}')



