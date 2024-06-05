#Higher Order Functions es una funcion que recibe otra funcion como parametro HOF "funcion puede recibir otra funcion como parametro"

#la funcion increment es una funcion que recibe un parametro y retorna un parametro
def increment(x):
  return x + 1
#usando lammbda
increment_v2 = lambda x: x + 1


#la funcion high_ord_func es una funcion que recibe dos parametros, uno es un parametro que recibe una funcion y el otro es un parametro que recibe un parametro
def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

#usando lammbda
high_ord_func_v2 = lambda x, func: x + func(x)
result2 = high_ord_func_v2(2, increment_v2)
print(result2)

#en esta funcion lamdba no se le asigna un nombre, se le asigna un nombre al parametro que recibe la funcion
result3 = high_ord_func_v2(2, lambda x: x + 2)
print(result3)



