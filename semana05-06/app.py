from flask import Flask
from bd import conexion
from os import environ
from dotenv import load_dotenv
from categoria import categorias_blueprint
from flask_migrate import Migrate
load_dotenv()

app = Flask(__name__)
# Se almacenan variables que sirve para el funcionamiento de la aplicacion, no son las mismas  que las variables de entorno
# print(app.config)

# agregamos la variable que necesita SQLALChemy para funcionar
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# Inicializamos nuestra conexion a la bd
conexion.init_app(app)

# Luego de inicializar mi conexion con la bd creamos el flujo de migracion
Migrate(app, conexion)


# Aca registraremos los mini-apps en nuestra aplicacion principal
app.register_blueprint(categorias_blueprint)

if (__name__ == '__main__'):
    app.run(debug=True)
