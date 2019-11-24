def lpier(b):
    if b == 2:
        return True

    else:
        if b > 1:
            for a in range(2, b):
                if b % a == 0:
                    return False
                else:
                    return True
        else:
            return False
print(lpier(21))
#      else:
#         return "to jest liczba 1"

# szer = 8
def test_wieksza1():
   assert (lpier(1)) == False
def test_nieprzysta():
    assert (lpier(9)) == True
def test_parzysta():
    assert (lpier(10)) == False
def test_pierwsza():
    assert (lpier(2)) == True
def test_wieksza_2_pierwsza():
    assert (lpier(3)) == True
