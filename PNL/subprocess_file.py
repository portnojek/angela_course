#MODUŁ SUBPROCESS I WYWOŁANIE KOMEND SYSTEMU OPERACYJNEGO
''' ten moduł zastępuje os.system(), os.spawn*(), commands.*(), os.popen*(), popen2.*() i jest
wygodniejszy w użytkowaniu. Wykorzystane zostaną tu dwie funkcje: call i Popen. Pierwsza powoduje 
wykonanie liniowe wywołanej komendy, druga generuje osobny proces w systemie operacyjnym'''

#Funkcja call
import subprocess
result=subprocess.call(['ping', '-n', '10', 'onet.pl'])
print(f"result = {result}")
print("koniec")

import subprocess
result=subprocess.Popen(['ping', '-n', '10', 'onet.pl'])
print(f"result = {result}")
print("koniec")
