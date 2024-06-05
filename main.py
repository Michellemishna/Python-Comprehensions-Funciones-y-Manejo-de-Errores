#aqui los paquetes que importamos son los que estan en la carpeta pkg
#from pkg.mod_1 import func_1, func_2
#from pkg.mod_2 import func_3, func_4


# aqui se llama a las funciones que estan en los modulos que importamos
'''
print(func_1())
print(func_2())
print(func_3())
print(func_4())
'''
import pkg
print(pkg.URL)
#esta es una forma de importar un modulo que esta en una carpeta que no sea la carpeta raiz del proyecto y una buena practica
print(pkg.mod_1.func_1())

#ejercicio 
#archivo my_fuctions.py 
def get_totals(orders):
   return [order['total'] for order in orders]

def calc_total(totals):
   return sum(totals)

#archivo main
import my_functions
def get_total(orders):
  # Tu código aquí 👇
  totals = my_functions.get_totals(orders)
  acum = my_functions.calc_total(totals)
  return acum

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)
