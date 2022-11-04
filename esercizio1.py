#assegno il valore 5 alla variabile x, assegno la scritta John alla variabile y, stampo prima il valore della x e stampo valore della variabile y
x = 5 
y = "John"
print(x)
print(y)

#assegno il valore 5 alla variabile x, modifico il valore della variabile x assegnadole la scritta Johnny, e infine stampo il valore di x
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#specifico il tipo della variabile x, string, assegnandole il valore 3, poi y, integer, assegnandole il valore 3, e infine z, float, assegnandole il valore 3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#assegno prima il valore 5 alla variabile x, poi la scritta John alla variabile y, e infine stampo il tipo di ognuna delle variabile, x e y.
x = 5
y = "John"
print(type(x))
print(type(y))

#La scritta john viene prima assegnata alla variabile x usando le doppie virgolette e dopo usando l'apostrofo
x = "John"
# is the same as
x = 'John'

#Assegno il valore 4 alla variabile a, e la scritta Sally alla variabile A. Questo indica che a e A sono due variabili diverse alle quali si possono assegnare valori diversi
a = 4
A = "Sally"
#A will not overwrite a

#Le variabili possono avere solo caratteri alfa numerici, e iniziare solo con lettere, maiuscole o minuscole, o trattino basso
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#assegna valori diversi a diverse varibili in una sola riga, rispettando l'ordine di scrittura.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assegno lo stesso valore a tre variabili diverse
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Quando dei valori si trovano in una lista è possibile estrarli e assegnarli a delle variabili. x ha come valore apple, y banana e z cherry. 
# Infine vengono stampati i vari valori attraverso la stampa delle diverse variabili
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Per stampare una variabile, usare la dicitura print()
x = "Python is awesome"
print(x)

#nel caso si volesse stampare diverse varibili in una stessa riga basta stampare digitando il nome dellle variabili separate da una virgola
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#nel caso si volesse stampare diverse varibili in una stessa riga si può anche digitare il nome delle variabili usando un +
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#usando un + tra variabili numeriche, i loro valori si sommano
x = 5
y = 10
print(x + y)

# assegno un valore ad una variabile x al di fuori della funzione, dunque questa si può usare in ogni momento, dentro e fuori dalle funzioni
# stampo poi il valore di x dentro la funzione
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


#creo una variabile x assegnandole il valore awesome, inoltre all'interno della funzione definisco nuovamente x.
#se stampo la x all'interno della funzione ottengo il valore assegnato all'interno della funzione
#se stampo la x fuoir dalla funzione stampo il valore iniziale
#le variabili dunque definite all'interno della funzioni sono locali e non modificano quelle esterne
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



#definisco la variabile x all'interno della funzione, assegnandole anche la parola chiave global. 
# la variabile pur essendo all'interno della variabile è resa esterna
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#definisco la variabile prima all'esterno della funzione poi la medesima all'interno di myfunc utilizzando la parola chiave global, dunque le modifiche sono anche esterne
#quando stampo la variabile il valore è quello modificato nella funzione
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
