def otworz_walizke(szyfr):
    return szyfr == "dudda68"

def kolejna_literka(lista_podejrzen,czesc_hasla,krok):
    print("funkcja wywołana z",czesc_hasla)
    if krok == len(lista_podejrzen):
       print("proboje otworzyc walizke z haslem",czesc_hasla)
       if otworz_walizke(czesc_hasla):
           return czesc_hasla
       else:
           return None

    for literka in lista_podejrzen[krok]:
        kolejna_literka(lista_podejrzen,czesc_hasla+literka,krok+1)
        temp=kolejna_literka(lista_podejrzen,czesc_hasla,krok+1)
        if temp:
            return temp


def otwieracz(lista_podejrzen):
    return kolejna_literka(lista_podejrzen,"",0)
    ...
podejrzenia =["sdf", "yui8j", "dscf","aq","6","89"]
print("hasło to",otwieracz(podejrzenia))
