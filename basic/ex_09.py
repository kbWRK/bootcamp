import time
print(f"witaj sprawdze czy jestes pelnoletni")
R = int(input('podaj swóją date urrodzenia'))
time.sleep(1)
W=2019 - R
if W>=18:
    print("jestes pelnoletni")
else :
    print(f"no jeszcze został ci {18-W} rok")

