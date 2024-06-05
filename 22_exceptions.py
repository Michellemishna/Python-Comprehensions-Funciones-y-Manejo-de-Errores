#correcto manejo de errores
try:
  print(0/0)
except ZeroDivisionError as error:
  print(error)

print('Hola')

try:
  assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as error:
  print(error)

try:
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error:
  print(error)

try:
  print(0/0)
  age = 10
  if age < 18:
     raise Exception('No se permiten menores de edad')
  assert 1 != 1, 'Uno no es igual a uno'
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola 2')

#ejercicio 
def my_divide(a, b):
   # Escribe tu solución 👇
   try:
      result = a / b
   except ZeroDivisionError as error:
      result = 'No se puede dividir por 0'
   return result

response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0
