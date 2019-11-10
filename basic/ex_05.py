mA = float(input("miasto a"))
mB = float(input("miasto b"))
cP = float(input("podaj cene paliwa"))
oD = float(input("podaj odległosc"))
s = float(input("podaj spalanie"))
koszt = round((oD/100*s)*float(cP))
print(f"koszt przejazdu pomieddzy {mA} a  {mB} wynosi:{koszt}PLN ")

