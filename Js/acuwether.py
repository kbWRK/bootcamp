import json
import urllib.request
import time
import json
import urllib.request


def main():
    lokalizacja = input("podaj lokalizacje")
#/ api / location / search /?query = (query)
    url = 'https://www.metaweather.com//api/location/search/?query=' + lokalizacja
    with urllib.request.urlopen(url) as r:
        data = r.read()
    found_locations = json.loads(data)
    if not found_locations:
        print('sory')
        return
    woeid = found_locations[0]["woeid"]

    url = f"https://www.metaweather.com/api/location/{woeid}/"
    with urllib.request.urlopen(url) as r:
        data = r.read()
    weather_today = json.loads(data)["consolidated_weather"][2]

    print("temp", {weather_today['the_temp']},"c")
    time.sleep(30)






if __name__ == '__main__':
    main()


