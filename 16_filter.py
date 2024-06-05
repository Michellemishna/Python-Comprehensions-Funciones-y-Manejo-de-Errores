#filter es una funcion que recibe dos parametros, uno es una funcion y el otro es una lista, la cual se va a iterar y se va a filtrar
numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)

