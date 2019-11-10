RP = int(input("podaj rok urodzenia sie twoeje postaci "))
RB = int("2019")
Lpo = int((RB - RP) // 30)
odp = Lpo * "pra" + 'babka'
if RB - RP < 60:
    print("towja postac jest zamłoda")
if Lpo > 5:
    odp = ("nie wiem ale jest stara")
elif Lpo < 60:
    odp = (" matka")
print(f"""twoja postac urodziła sie przed {RB - RP}
twoja postac mogła by byc towją {odp} """)
