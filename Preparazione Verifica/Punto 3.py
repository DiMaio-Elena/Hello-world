import random

Casuale=[]
for i in range(0,500):
    Casuale.append(i)

for x in Casuale :
    if x%2 == 0:
        Casuale.remove(x)
print(Casuale)