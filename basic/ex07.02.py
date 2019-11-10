A=float(input(("podaj długosc")))
B=float(input(("podaj szerokosc")))
H=float(input(("podaj wyskosc")))
ODP=H*B*A/1000
print(f"twój kartonik ma {round(ODP,2)} l ")
if ODP < 1:
    print("niestety masz za mało")
else:
    print("no masz szczescie")
if ODP > 1:
    print(f"masz o {round(float(ODP-1),2)}")