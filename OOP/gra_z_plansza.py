import random
class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

        # TODO umiesc skarb w losowym miejscu

    def przesun(self, kierunek, plansza_wymiar_x , plansza_wymiar_y):
        if kierunek == "w":
            if  plansza_wymiar_y and self.y + 1 >= plansza_wymiar_y:
               self.y += 1
        elif kierunek == "s":
            if self.y - 1 < 0:
             return
            self.y -= 1
        elif kierunek == "a":

            self.x -= 1
        elif kierunek == "d":
            if plansza_wymiar_x and self.y + 1 >= plansza_wymiar_x:
                self.x += 1
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

pionki = [WojownikNocy("krystian"), WojownikNocy("mareczek"), WojownikNocy("Adi"), BlekitnyJezdziec("komendant śmimigała")]
for pionek in pionki:
    print(f'{pionek.imie}:\t\t{pionek.x},{pionek.y}')
    print()
    for _ in range(10):
        for pionek in pionki:
            pionek.przesun(random.choice("wsad"),10,10)
for _ in range(10):
    for pionek in pionki:
        print(f'{pionek.imie}:\t\t{pionek.x}, {pionek.y}')




def plansza_jako_string(pionki, wymiar_x, wymiar_y):
    s = ""
    for x in range(wymiar_x):
        for y in range(wymiar_y):
            for pionek in pionki:
                if pionek[0].x == x and pionek.y == y:
                    s += pionek.imie[0]
                break
            else:
                s += "-"
if __name__ == "__main__" :
    pionki = [WojownikNocy("krystian"), WojownikNocy("mareczek"), WojownikNocy("Adi"),
              BlekitnyJezdziec("komendant śmimigała")]
    for pionek in pionki:
        print(f'{pionek.imie}:\t\t{pionek.x},{pionek.y}')
        print()
        for _ in range(10):
            for pionek in pionki:
                pionek.przesun(random.choice("wsad"), None, None)
    print(plansza_jako_string(pionki,10,10 ))
#TODO zrobic zeby byla plansza dodac fabułe ect.
