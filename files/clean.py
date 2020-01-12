import sys


# tablica poprawna (@..,@...,@...)
# lista która czytam po niej chodze i patrze czy jest to ..
# wrzuczam poprawne do poprawnej listy
def main(args):
    right_adres = set()
    with open(sys.argv[1], 'r', encoding="utf-8") as f:
        for email_adres in f:
            email_adres = email_adres.strip()
            if email_adres.count('@') == 1:
                user, mail = email_adres.split('@')
                if mail == "email.com":
                    right_adres.add(email_adres)

    with open(sys.argv[2], 'w', encoding="utf-8") as f:
        for email_adres in sorted(right_adres) :
            f.write(email_adres + "\n")

if __name__ == '__main__':
    main(sys.argv[1:])
