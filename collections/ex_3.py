L = [1, -2, 3, 4, -5, 65, 7]
P = 0
N = 0
for c in L:
    if c > 0:
        P += 1
    else:
        N += 1
print(f"jest {P} dodatnich i {N} ujemnych")
