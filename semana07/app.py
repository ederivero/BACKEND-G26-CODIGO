from flask import Flask
from dotenv import load_dotenv
from bd import conexion
from flask_migrate import Migrate
from os import environ
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion.init_app(app)
Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)
