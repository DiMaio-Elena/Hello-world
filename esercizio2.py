
#creo una lista contente diverse variabili, le stampo digitando il nome della lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

#della lista creata stampo il numero di elementi presenti con la funzione len
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#le liste sono definite come oggetti dunque con il data tipo list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#creo una lista con il costruttore list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#creo una lista con diverse variabili e stampo solo l'elemento posto alla posizione 1 (la numerazione degli elementi parte da 0)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#l'ultimo elemento viene numerato a partire da -1
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#stampo i valori dalla posizione 2 alla 5 esclusa con la dicitura 2:5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#stampo i valori dal primo fino al quarto escluso scrivendo :4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#stampo i valori dal secondo all'ultimo scrivendo 2:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#posso numerare le variabili a partire dal fondo quindi assegnandole una numerazione negativa
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#se si vuole controllare se è presente un certo valore, qua apple, in una apple uso la keyword in, poi stampo qualora presente
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#sostituisco il valore alla posizione 1 scrivendo il nome della lista [numero posizione elemento] = al nuovo valore
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#sostituisco i valori dal 1 al 3 escluso con 1:3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#se inserisco più valori di quelli che sostituisco, gli elementi aggiuntivi si posizioneranno in seguito a quello sostituito
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# se inserisco meno valori di quelli che sostituisco, gli elementi da sostituire spariscono e si inserisce il nuovo valore
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert permette di inserire un valore nella posizione desiderata senza sostituire nessuno valore, scrivendo nomelista.insert(numero posizione, valore)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append permette di inserire un valore alla fine della lista, scrivendo scrivendo nomelista.append(valore)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#unisco due liste con la funzione extend, nomelista.extend(nome lista), gli elementi sono aggiunti alla fine della lista
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#posso unire qualunque oggetto con extend
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove permette di rimuovere un certo valore, scrivendo nomelista.remove valore)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop rimuove un specifico valore utilizzando numero della posizione, scrivendo nomelista.pop(numero posizione, valore)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#se non specifico il numero della posizione rimuove l'ultimo
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del elimina un specifo valore utilizzando il numero della posizione
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#può anche eliminare tutta la lista
thislist = ["apple", "banana", "cherry"]
del thislist

#clear elimina tutti valori all'interno della lista, mantenedo la lista creata
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#con il ciclo for stampo ogni valore della lista
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#il ciclo for stampa gli elementi anche usando l'iterazione i, len indica il numero degli elementi range definisce quante volte for deve stampare
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#il ciclo while permette di stampare  i valori assegnando un indice ad ogni valore e  inccrementando il valore dell'indice ogni volta
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#è un modo di scrivere il loop for più velocemente
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
