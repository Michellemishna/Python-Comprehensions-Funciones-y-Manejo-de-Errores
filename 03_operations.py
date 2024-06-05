set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union de conjuntos
set_c = set_a.union(set_b)
print(set_c)

#otra forma de unir conjuntos es:
print(set_a | set_b)

# Interseccion de conjuntos
set_c = set_a.intersection(set_b)
print(set_c)

#otra forma de interseccion de conjuntos es:
print(set_a & set_b)

# Diferencia de conjuntos
set_c = set_a.difference(set_b)
print(set_c)

#otra forma de diferencia de conjuntos es:
print(set_a - set_b)

# Diferencia simetrica de conjuntos
set_c = set_a.symmetric_difference(set_b)
print(set_c)

#otra forma de diferencia simetrica de conjuntos es:
print(set_a ^ set_b)

#ejercicio:
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

# Escribe tu solución 👇

new_set = set(countries | northAm | centralAm | southAm)
print(new_set)
