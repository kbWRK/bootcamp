import random
from random import randrange

x = 1  # pion
xs = int(randrange(1, 10))  # skarb
y = 5  # poziom
ys = int(randrange(1, 10))  # skarb
g = [x, y]
s = [xs, ys]
Lr = 0  # liczba ruchów
print(abs(x - xs), abs(y - ys))
print(x, y)
print(xs, ys)
while g != s:
    ruch = input('rusz sie ')
    if ruch == "w":
        x = x + 1
        g = [x, y]
        Lr += 1
        print(f"to twój: {Lr} ruch")
        print(abs(x - xs), abs(y - ys))
        print(x, y)
        print(xs, ys)
        if x-xs <= abs(3) or y-ys <= abs(3):
            print("jestes blisko")
        else:
            print("daleko jeszcze!!!")
        if x > 10 or x < 1 or y > 10 or y < 1:
            break
    elif ruch == "s":
        x = x - 1
        g = [x, y]
        Lr += 1
        print(f"to twój: {Lr} ruch")
        print(abs(x - xs), abs(y - ys))
        print(x, y)
        print(xs, ys)
        if x-xs <= abs(3) or y-ys <= abs(3):
            print("jestes blisko")
        else:
            print("daleko jeszcze!!!")
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
    elif ruch == "a":
        y = y - 1
        g = [x, y]
        Lr += 1
        print(f"to twój: {Lr} ruch")
        print(abs(x - xs), abs(y - ys))
        print(x, y)
        print(xs, ys)
        if x-xs <= abs(3) or y-ys <= abs(3):
            print("jestes blisko")
        else:
            print("daleko jeszcze!!!")
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
    elif ruch == "d":
        y = y + 1
        g = [x, y]
        Lr += 1
        print(f"to twój: {Lr} ruch")
        print(abs(x - xs), abs(y - ys))
        print(x, y)
        print(xs, ys)
        if x-xs <= abs(3) or y-ys <= abs(3):
            print("jestes blisko")
        else:
            print("daleko jeszcze!!!")
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
if g == s:
    print("wygrałes")
else:
    print('nie udało ci sie')

