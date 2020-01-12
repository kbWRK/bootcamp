
def vowels(s):
    # zobacz czy masz a
    # jesli tak to mi je daj
    # zabacz czy masz y jesli ta to je daj
    for c in s :
        if c in "aeouiy":
            yield c

for char in vowels("ala ma kota a kot ma ale"):
    print(char)