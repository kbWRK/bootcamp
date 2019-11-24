# tekst = \
"ala ma <kota> a kot ma ale"


def policz_znaki(tekst, argumet1):
    l = []
    counter = 0
    for litera in tekst:
# if tekst.index(litera) > tekst.index(argumet1):
         counter += 1
    print(counter)

    # for litera in tekst:
    #     if tekst.index(litera) > tekst.index(argumet1) and tekst.index(litera) < tekst.index(argument2):


# def test_pojedyncze_znaczniki_domyslne():
#     assert policz_znaki("ala ma <kota> a kot ma ale") == 4


policz_znaki("ala ma <kota> a kot ma ale", "<")
