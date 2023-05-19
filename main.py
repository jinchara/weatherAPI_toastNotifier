import requests
import json
import sqlite3
from win10toast import ToastNotifier
import time
key = 'b0382a9da8d31051dd5eecdc220673dc'
lat = 41.716667
lon = 44.783333
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
info=requests.get(url, params={'units': 'metric'})

cont=info.content
get_url = info.url
st_code = info.status_code
if st_code==200:
    print('სტატუს კოდია 200, წარმატებით დაკავშირდა')
else:
    print(f'სამწუხაროდ სტატუს კოდია {st_code}')
hd=info.headers

weather = json.loads(info.text)
x=json.dumps(weather, indent=4)

db_lat=weather['coord']['lat']
db_lon=weather['coord']['lon']
db_temp = weather['main']['temp']
# conn = sqlite3.connect('weather1.sqlite')
# cur = conn.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS weather
#             (lat INTEGER
#             lon INTEGER,
#             temperature FLOAT)
# ''') #შევქმენი ცხრილი პითონის საშუალებით და ბაზის სვეტის სახელებს დავარქვი lat lon და temperature
# cur.execute("INSERT INTO weather (lat, lon, temperature) VALUES (?,?,?)", (db_lat, db_lon, db_temp))#APIდან წამოღებული ინფორმაცია ტემპერატურას, latსა და lonს ჩასვამს ბაზის ცხრილში
#
# conn.commit()
# conn.close()
print(db_temp)

prev_temp = None
while True:
    info = requests.get(url, params={'units': 'metric'})
    weather = json.loads(info.text)
    db_temp = weather['main']['temp']
    if db_temp != prev_temp:
        toast = ToastNotifier()
        toast.show_toast(
            title=str(db_temp),  # Convert the temperature to a string
            msg="Tbilisi's temperature",
            duration=10
        )
        prev_temp = db_temp
    time.sleep(10)



#print(f'API-ს URL არის : {get_url}')
#print(hd)
#print(x)