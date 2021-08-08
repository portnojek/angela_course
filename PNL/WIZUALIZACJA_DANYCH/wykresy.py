# #pierwszy wykres liniowy

# from types import LambdaType
# import matplotlib.pyplot as plt
# from random import random

# y=[random()*100 for e in range(100)]
# plt.plot(y)
# plt.show()

# #nanoszenie dodatkowych serii
# import matplotlib.pyplot as plt
# from random import random

# y=[random()*100 for e in range(10)]
# x=[random()*100 for i in range(10)]
# plt.plot(y)
# plt.plot(x)
# plt.show()

# #dodawanie legendy do wykresu
# import matplotlib.pyplot as plt
# from random import random
# y=[random()*100 for e in range(10)]
# x=[random()*100 for i in range(10)]
# plt.plot(y, label='seria y')
# plt.plot(x, label='seria x')
# plt.legend()
# plt.show()

# #etykiety osi x i y
# import matplotlib.pyplot as plt
# from random import random
# y=[random()*100 for e in range(12)]
# x=[random()*100 for i in range(12)] 
# plt.plot(y, label='seria y')
# plt.plot(x, label='seria x')
# plt.ylabel('oś y')
# plt.xlabel('oś x')
# plt.legend()
# plt.show()

# #zmiana koloru i rodzaju linii
# import matplotlib.pyplot as plt
# from random import random
# a=[random()*100 for e in range(10)]
# b=[random()*100 for e in range(10)]
# c=[random()*100 for e in range(10)]
# plt.plot(a,'b-',label='seria a')
# plt.plot(b,'r--',label='seria b')
# plt.plot(c,'g:',label='seria c')
# plt.legend()
# plt.grid()
# plt.show()

# #zmiana koloru jako argument

# import matplotlib.pyplot as plt
# from random import random
# a=[random()*100 for e in range(10)]
# plt.plot(a,'#FFAA00')
# plt.show()

# #lub

# import matplotlib.pyplot as plt
# from random import random
# a=[random()*100 for e in range(10)]
# plt.plot(a,color='#FFAABB')
# plt.show()

# #siatka na wykresie - funkcja 'grid'
# import matplotlib.pyplot as plt
# from random import random
# y=[random()*100 for e in range(10)]
# plt.plot(y)
# plt.grid()
# plt.show()

#zapisywanie wykresu do pliku
import matplotlib.pyplot as plt
from random import random
a=[random()*100 for e in range(10)]
plt.plot(a)
plt.savefig('/home/bartek/Desktop/wykres.png')
plt.show()

#wykresy słupkowe
import matplotlib.pyplot as plt
from random import random
x=list(range(12))
y=[random()*10000 for e in range(12)]
plt.bar(x,y)
plt.show()

#zmiana koloru słupków
import matplotlib.pyplot as plt
from random import random
x=list(range(12))
y=[random()*10000 for e in range(12)]
wykres=plt.bar(x,y)
wykres[0].set_color('r')
plt.show()

#kolor słupków dla wszystkich - musimy zastosować iterację
import matplotlib.pyplot as plt
from random import random
x=list(range(12))
y=[random()*10000 for e in range(12)]
wykres=plt.bar(x,y)
for i in range(len(wykres)):
    wykres[i].set_color('r')
plt.show()

#nakładanie serii słupkowych i liniowych na siebie

import matplotlib.pyplot as plt
from random import random
x=list(range(12))
y=[random()*10000 for e in range(12)]
z=[random()*10000 for e in range(12)]
plt.bar(x,y)
plt.plot(z,'r')
plt.show()