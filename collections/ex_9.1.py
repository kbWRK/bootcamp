pry = {
    "z": 2.2,
    "m": 4.4,
    "k": 5.5,
}
print("dostepne produkty")
for pr in pry:
    print(f"-{pr}")
produkt = input("co kupujesz")
if pr in pry:
 ilosc = float(input("ile kg"))
 print("należy sie ", pry[pr] * ilosc)
else:
 print("nie ma takiego czegos")


