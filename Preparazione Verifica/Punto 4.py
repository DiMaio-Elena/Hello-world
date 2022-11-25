
import random
casuale = []
valore=0

for i in range (50):
    casuale.append(random.randint(0,100))
for x in casuale :
    if x>50 or x<10 :
        print(x)
valore=valore+1
