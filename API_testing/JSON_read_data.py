import json
import pprint


with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)

#print(json.dumps(wynik, indent=4, ensure_ascii=False, sort_keys=True))
pprint.pprint(wynik)