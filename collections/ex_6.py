from random import randrange

L = [123, 3, 456, 6, 54, 5, ]
Lmin = None
Lmax = None

# L=sorted(L)
# L=L[::-1]
# L[0]=L[5]
# L
# print(L)
print("przed:", L)
for x in L:
    if x == min(L):
        print(x)
for y in L:
    if y == max(L):
        print(y)


