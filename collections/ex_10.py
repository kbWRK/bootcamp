napis = "oko za oko ząb za ząb"
literki = {}
for literka in napis:
    literki[literka] = literki.get(literka, 0) + 1
# if literka in literki:
#     literki[literka] += 1
# else:
#     literki[literka] = 1
# print("literki")
for literka, ilosc in literki.items():
    print(f"- {literka!r} : {ilosc}")
