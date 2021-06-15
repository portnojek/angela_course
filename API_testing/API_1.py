import requests
import json
"""

API - Application Programming Interface

Inter - pmiędzy
face - twarz

bankomat

"""



r = requests.get("https://api.suredbits.com/nba/v0")


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("jest ok")    