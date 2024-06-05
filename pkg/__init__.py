#si trabajas con la version de python 3.3 o inferior el archivo __init__.py es necesario para que funcione el paquete

#en versiones posteriores a la 3.3 el archivo __init__.py se puede omitir, pero tambien se puede usar para inicializar variables o importaciones a otros archivos

print( 'Se inicio paquete')

URL = 'platzi.com'

#cada vez que se llame a este paquete se inicializara e importara lo que este dentro de este archivo

import pkg.mod_1, pkg.mod_2