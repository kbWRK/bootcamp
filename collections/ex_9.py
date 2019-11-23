p = {"marchewki": 10, "ziemniaki": 5}
print('''
    DOSTEPNE PRODUKTY
    -m
    -z
    ''')
a = [input("    co kupujesz: ")]
b = input("    ile kilogramów:")
if a == "m":
    print(p[a] * int(b))
