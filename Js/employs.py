import json


def main():
    employees = []
    try:
        with open("baza_danych.json", "r") as f:
            employees = json.load(f)
    except json.decoder.JSONDecodeError:
        employees = []

    a = input("co chcesz zrobic[d-dodaj  w-wypisz] ")

    if a.lower().strip() == 'd':
        imie = input("imie: ").lower().strip()
        nazwisko = input("nazwisko: ").lower().strip()
        rok_urodzenia = input("rok urodzenia: ").lower().strip()
        email = input("email: ").lower().strip()
        pensja = input("pensja: ").lower().strip() + " PLN"
        employ = {
            "imie": imie,
            "nazwisko": nazwisko,
            "rok_urodzenia": rok_urodzenia,
            "email": email, "pensja": pensja
        }
        employees.append(employ)
        with open('baza_danych.json', 'a') as f:
            json.dump(employees, f)

    elif a.lower().strip() == "w":
        for numer, employ in enumerate(employees):
            print(f"~[{numer + 1}]~{employ['imie']} {employ['nazwisko']}")

if __name__ == '__main__':
    main()
