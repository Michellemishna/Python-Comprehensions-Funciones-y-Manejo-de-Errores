#iter sirve para recorrer un objeto iterable
for i in range(1, 10):
  print(i)

#aqui hacemos una iteracion de un rang de 1 a 4
my_iter = iter(range(1, 4))
#aqui imprime range_iterator
print(my_iter)
#aqui imprimimos el primer elemento de la iteracion y usnado next() vamos a ir avanzando en la iteracion
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#aqui si intentamos usar next() de una iteracion que ya no tiene mas elementos nos dara un error
#print(next(my_iter))

