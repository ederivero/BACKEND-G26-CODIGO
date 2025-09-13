from flask import Flask

# __name__ > variable de python que sirve para indicar si el archivo que estamos utilizando es el archivo principal de nuestro proyecto, si lo es el valor sera __main__ sino sera el nombre del archivo
# Flask utiliza el __name__ para crear una sola instancia del servidor en todo el proyecto y evitar tener mas de uno por proyecto
servidor = Flask(__name__)

# DECORADORES: la forma en la cual podemos agregar funcionamiento a un metodo sin la necesidad de modificar la clase como tal
@servidor.route('/')
def bienvenida():
    return 'Bienvenido a mi API de Flask'

# frontend 8080
# postgres 5432
# Tiene que ir al final porque es el encargador de levantar la aplicacion y luego de esto se queda en espera de nuevas solicitudes
# debug > si esta habilitado cada vez que hagamos un cambio se reiniciara la aplicacion de manera automatica
servidor.run(port=5000,debug=True)