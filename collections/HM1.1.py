liczby = []

while len(liczby) < 10:
    dana = (input(f"podaj liczbe lub wipisz koniec"))
        print("nie podałes liczby lub koniec")
        continue
    if dana.lower() == "koniec":
        break
    dana = int(dana)
    liczby.append(dana)
if liczby:
    print("srednia to", sum(liczby) / len(liczby))
