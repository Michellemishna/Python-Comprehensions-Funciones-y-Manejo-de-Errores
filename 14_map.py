#map es una funcion que transfoma cada elemento de una lista, en este caso, la lista de numeros
numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

#map es una funcion que recibe dos parametros, uno es una funcion y el otro es una lista

numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

#ejercicio:
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)

#lo que hace es unir las dos listas en una sola lista con la funcion lambda sumando los valores de las dos listas uno por uno

#es decir, [1, 2, 3, 4] + [5, 6, 7] = [6, 8, 10] no suma el ultimo valor de numbers_1 porque no tiene con que sumar
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

#ejercicio:
def multiply_numbers(numbers):
  # Escribe tu solución 👇
  return list(map(lambda i: i * 2 , numbers))

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)