
import random
x = random.randint(0,500)
y = random.randint(0,500)
z = random.randint(0,500)
if x<y and x<z:
    print (x)
    if y<z:
        print(y)
        print (z)
    else:
        print(z)
        print(y)
elif y<z:
    print (y)
    if z<x:
        print(z)
        print(x)
    else:
        print (x)
        print(z)
else:
    print (z)
    if x<y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)
