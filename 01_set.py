#conjuntos
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

#no puede haber elementos duplicados
set_numbers = {1, 2, 2, 443, 23} 
print(set_numbers)
set_types = {1, 'hola', False, 12.12}
print(set_types)

#podemos crear un conjunto a partir de un string sin elementos duplicados
set_from_string = set('hoola')
print(set_from_string)

#podemos crear un conjunto a partir de una tupla sin elementos duplicados
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# de esta manera se puede convertir una lista a un conjunto sin elementos duplicados
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

# de esta manera se puede convertir un conjunto a una lista sin elementos duplicados
unique_numbers = list(set_numbers)
print(unique_numbers)

