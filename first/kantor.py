def kantor():
    kursy = {"USD": 3.4, 'EUR': 4.4, 'PAB': 3.8}
    print(f"""kursy walut
          USD ➤ {3.4} 
          EUR ➤ {4.4}
          PAB ➤ {3.8}""")

    b = input('podaj nazwe waluty').upper().strip()
    action = input('co chcesz zrobic[k/s]').lower().strip()

    if action == 'k':
        a = int(input('jaka kwote chcesz zakupic?'))
        dozaplaty = a * kursy.get(b)
        print(f'do zaplaty {dozaplaty} PLN')
    else:
        a = int(input('jaka kwote chcesz sprzedac?'))
        dozaplaty = a * kursy.get(b)
        print(f'dostajesz {dozaplaty} PLN')



if __name__ == '__main__':
    kantor()