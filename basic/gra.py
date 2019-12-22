print("Chcę zagrać w grę")
x = int(input("podaj liczbe "))
y = int(input("jeszcze raz "))
if y > 90 and x > 90:
    print("prawy górny róg")
elif y < 10 and x > 90:
    print("prawy dolny róg")
elif y > 90 and x < 10:
    print("lewy górny")
elif y < 10 and x < 10:
    print("lewy dolny")
elif y >= 10 and y <= 90 and x >= 10 and x <= 90:
    print(" srodek")
elif x < 10 and y < 90 and y > 10:
    print("lewo")
elif x > 90 and y > 10 and y < 90:
    print("prawo")
elif x > 100 or y > 100 or x < 0 or y < 0:
    print("nie żyjesz")
