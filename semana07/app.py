from flask import Flask, request, render_template
from dotenv import load_dotenv
from bd import conexion
from flask_migrate import Migrate
from os import environ
from modules.usuarios import usuarioBlueprint
from requests import post
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion.init_app(app)
Migrate(app, conexion)


@app.route('/validar-usuario')
def validarUsuario():
    token = request.args.get('token')
    if not token:
        return render_template('not_found.html')

    # en nuestra API podemos consultar otras API's
    respuesta = post(
        'http://127.0.0.1:5000/usuario/habilitar-usuario', json={"token": token})
    if respuesta.status_code == 200:
        return render_template('validacion_exitosa.html')
    else:
        return render_template('not_found.html')


app.register_blueprint(usuarioBlueprint)

if __name__ == '__main__':
    app.run(debug=True)
