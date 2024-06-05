import functools
#functools es una libreria que tiene varias funciones para trabajar con listas
numbers = [1, 2, 3, 4]

#reduce es una funcion que recibe dos parametros, uno es una funcion y el otro es una lista y lo que hace es iterar la lista y retornar un solo valor

def accum(counter, item):
  print('counter =>', counter)
  print('item =>', item)
  return counter + item


result = functools.reduce(accum, numbers)
print(result)



