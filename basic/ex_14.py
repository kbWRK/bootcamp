LMn = 0
LMx = 0
LZ = False
while True:
    Lp ="koniec"
    Lp = input(f"wpisz liczbe lub 'koniec': ")
    if Lp.lower() == "koniec":
        break
    if Lp == "":
        print("nic nie wpisałes")
        continue

    Lcz = int(Lp)
    if Lcz < LMn or not LZ:
        LMn=Lcz
    if Lcz > LMx or not LZ:
        LMx=Lcz
    LZ=True

if LZ:
    print(f"maksymalna liczba to {LMx} a min to {LMn}")
else:
    print("niepodałes zadnych liczb")
