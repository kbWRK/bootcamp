produkty = {
    "z": 2.2,
    "m": 4.4,
    "k": 5.5,
}
print("dostepne produkty")
for produkt in produkty:
    print(f"-{produkt}")
produkt = input("co kupujesz")
if produkt in produkty:
 ilosc = float(input("ile kg"))
 print("należy sie ", produkty[produkt] * ilosc)
else:
 print("nie ma takiego czegos")


