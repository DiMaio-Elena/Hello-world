listaAnimali = ["cane", "gatto", "pappagallo", "pantera", "leopardo"]
listaNumeri = [368, 8763, 830, 592, 289]
listaAnimaliNumeri= listaAnimali + listaNumeri
for x in listaAnimaliNumeri:
    if isinstance(x, int) and  x>5:
     print(x)