#GET
#Do obsługi usług sieciowych w Pythonie mamy moduł "requests" (wymaga importu).
import requests

odpowiedz = requests.get("http://jsystems.pl/static/blog/python/dane.json" , auth=('user','pass'))
print(odpowiedz.status_code)
dane = odpowiedz.json()
print(dane)

#odniesienie do konkretnych danych
import requests
odpowiedz=requests.get("http://jsystems.pl/static/blog/python/dane.json")
dane = odpowiedz.json()
print(dane['adres']['miasto'])

#POST
import requests
dane=dict()
odpowiedzWysylka=requests.post("http://jsystems.pl/static/blog/python/dane.json",data=dane,headers={"Content-Type":"application/json"})
print(odpowiedzWysylka.status_code)


