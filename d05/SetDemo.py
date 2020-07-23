
import random as r
lotto = []  # list
while len(lotto) < 5:
    lotto.append(r.randint(1, 10))
print(lotto)

lotto2 = set()
while len(lotto2) < 5:
    lotto2.add(r.randint(1, 10))
print(lotto2)