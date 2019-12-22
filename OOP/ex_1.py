import datetime
class SwietyMikołaj:
    def __init__(self , imie="mikołaj"):
        self.imie = imie

    def przywitaj_sie(self):
        print(f"HoHoHo!!! jestem {self.imie}")


    def daj_prezent(self):
        return """
____$$$$$$_$$$$$$$
_____$ $$$$$$$$$$$$$$$
_____$$$$$$$_$$$$$$$$
______$$$_ _____$$$$
___$$$$$_______ _$$$$$$
___$$$$$$______$$$$$$$
____$$$$$$$$$$$$$ $$$$$
______$$$_$$$$$$$
__________$$$$$_$
_____ ____________$
_________________$
_______________ __$
__________________$___$$$$_
________________ $__$$$$$$$$
__$$$$$$$______$_$$$$$
_$$$$$$$$$____$$$$$
$______$$$$__$
_________$$ _$
__________$$$
__________$$
____________$
__ __________$
"""


prezent = SwietyMikołaj()

mikołaj1 = SwietyMikołaj("mikołajek")
print("ten swiety mikołaj nazywa sie", mikołaj1.imie)
inni_mikołajowie = [SwietyMikołaj("balti"),SwietyMikołaj(),SwietyMikołaj()]
mikołaj2 = SwietyMikołaj()
print("ten swiety mikołaj nazywa sie", mikołaj2.imie)
mikołaj1.przywitaj_sie()
mikołaj2.przywitaj_sie()

print(f"oto twój prezent {mikołaj2.daj_prezent()}")
