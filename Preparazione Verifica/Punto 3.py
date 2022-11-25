import random

Casuale=[]
for i in range(50):
    Casuale.append(random.randint(0,500))

for x in Casuale :
    if x%2 == 0:
        Casuale.remove(x)
print(Casuale)