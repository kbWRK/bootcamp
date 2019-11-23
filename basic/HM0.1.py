import random
from random import randrange
x = randrange(0, 10)
y = randrange(0, 10)
g = [x, y]
s = [1, 5]
print(x, y)
while g != s:
    ruch = input('rusz sie ')
    if ruch == "w":
        x = x + 1
        g = [x, y]
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
    elif ruch == "s":
        x = x - 1
        g = [x, y]
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
    elif ruch == "a":
        y = y - 1
        g = [x, y]
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
    elif ruch == "d":
        y = y + 1
        g = [x, y]
        if x > 10 or x < 0 or y > 10 or y < 0:
            break
if g==s:
    print("wygrałes")
else:
    print('gnijesz smieciu')
