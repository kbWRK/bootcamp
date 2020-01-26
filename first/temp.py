import urllib.request, json

waluta = 'usd'  # input("podaj walute").upper().strip()
url = 'http://api.nbp.pl/api/exchangerates/rates/a/' + waluta + '/?format=json' + waluta + '?format=json'
with urllib.request.urlopen(url) as j:
    raw_data = json.loads(j.read().decode())
    data = raw_data.get('rates')[0].get('mid')
    # print(data[0].get('mid'))


