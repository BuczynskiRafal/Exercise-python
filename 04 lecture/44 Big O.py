# uszereguj podane złożoności obliczeniowe oagorytmów od najlepszej do najgorszej
# O(n * Log(n))
# O(Log(n))
# O(2 ** n)
# O(n ** 2)
# O(1)
# O(n)

# O od n oznacza ilość operacji jakie będzie musiał wykonać komputer na zbiorze o wielkości n

# O(1) - na przykład wyszykiwanie w set lub dict - tablice haszujące
# O(Log(n)) - na przykład wyszukiwanie bibarne - ta złożoność oznacza że należy wykonać znacznie mniej operacji niż jest elementów w zbiorze
# O(n) - tyle operacji ile jest elementów w zbiorze - na przykład algorytm iterujacy po liście
# O(n * Log(n)) - iloczyn złożoności dwóch powyzej - te złożoność mają wydajne algorytmy sprtowania na przykład team sort który jest stosowany w pythonie lub quick sort
# O(n ** 2) - mao wydajne algorytmy na przykład bubble sort lub operacja pomnożenia każdego elementu listy przez każdy element listy
# O(2 ** n) - bardzo zła złożonosć - liczna operacji 2 do potęgi n

import math       # poniższy kod wyświetla wykres przedstawiający porównanie różnych złożoności obliczeniowych
                  # przy użyciu popularnej bibliteki matplotlib
import matplotlib.pyplot as plt

seria0 = [1] * 10
seria1 = list(range(1,11))
seria2 = [math.log(x) for x in seria1]
seria3 = [math.log(x) * x for x in seria1]
seria4 = [x**2 for x in seria1]
seria5 = [2**x for x in seria1]

plt.plot(seria0, label="O(1)")
plt.plot(seria2, label="O(log(n))")
plt.plot(seria1, label="O(n)")
plt.plot(seria3, label="O(n * log(n))")
plt.plot(seria4, label="O(n**2)")
plt.plot(seria5, label="O(2**n)")

plt.legend()
plt.show()