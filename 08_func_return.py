sum = 0
for x in range(1, 10):
  sum += x
print(sum)

#creo una funcion que me devuelva la suma de los numeros del 1 al 10
def sum_with_range(min, max):
  print(min,max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

#aqui estoy llamando a la funcion y le estoy pasando los parametros
result = sum_with_range(1, 10)
print(result)

#con esta funcion paso los resultados obtenidos antes y llamo a la funcion nuevamente
result_2 = sum_with_range(result, result + 10)
print(result_2)