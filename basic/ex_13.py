Ld = 1
Su = 0
st=0
while Ld <= 7:
    Su += float(input(f"podaj temperature dla dnia {Ld}"))
    Ld += 1
print(f"Srednia temperatur to {Su/(Ld-1):.2f}^c")

print(Su)
print(Ld)