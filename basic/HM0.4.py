gracz_x = 1
gracz_y = 1

skarb_x = 4
skarb_y = 3
krok = 0
while True:
    # ...
    odległosc_przed_ruchem = abs((gracz_x - skarb_x)) + abs((gracz_y - skarb_y))
    kierunek = input("podaj kierunek")
    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == "a":
        gracz_x -= 1
    elif kierunek == "d":
        gracz_x += 1
    else:
        print("nie tym razem")
        continue
    odległosc_po_ruchu = abs(gracz_x - skarb_x) + abs((gracz_y - skarb_y))
    krok += 1
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f"znalazłes skarb w {krok} krokach")
    if odległosc_przed_ruchem > odległosc_po_ruchu:
        print ("ciepło")
    else:
        print("zimno")
