items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

# aqui se crea una lista con los precios de cada diccionario
prices = list(map(lambda item: item['price'], items))
print(prices)

# aqui al diccionario se le agrega una nueva clave y valor
def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

# aqui se crea una nueva lista con los diccionarios modificados
new_items = list(map(add_taxes, items))
print(new_items)

# aqui se crea una nueva lista con los diccionarios modificados
def add_taxes2(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
