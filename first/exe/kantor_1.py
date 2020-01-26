import json
import urllib.request
import time


def kantor():
    # kursy = {"USD": 3.4, 'EUR': 4.4, 'PAB': 3.8}
    # print(f"""kursy walut
    #       USD ➤ {3.4}
    #       EUR ➤ {4.4}
    #       PAB ➤ {3.8}""")

    waluta = input("podaj walute").upper().strip()
    url = 'http://api.nbp.pl/api/exchangerates/rates/a/' + waluta + '/?format=json' + waluta + '?format=json'
    data = 0
    with urllib.request.urlopen(url) as j:
            raw_data = json.loads(j.read().decode())
            data += raw_data.get('rates')[0].get('mid')
    action = input(['k/s'])
    if action == 'k':
        print(f'{waluta} kosztuje {data}')
        a = int(input('jaka kwote chcesz zakupic?'))
        dozaplaty = a * data
        print(f'do zaplaty {dozaplaty} PLN')
    if action == 's' :
        a = int(input('jaka kwote chcesz sprzedac?'))
        dozaplaty = a * data
        print(f'dostajesz {dozaplaty} PLN')
    # if action == 'super_tajna_funkcja':
    #      = int(input())
# TODO: Add "marża" and change somthig to class and make from it website or something but its for "A+"

    time.sleep(360)

if __name__ == '__main__':
    print(kantor())


