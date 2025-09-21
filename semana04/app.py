from flask import Flask, request
from psycopg import connect
from dotenv import load_dotenv
from os import environ
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from psycopg.rows import dict_row

# lee el archivo .env dentro del proyecto y asigna las variables declaradas en ese archivo como variables de entorno
load_dotenv()


# Validador
class CanchasSchema(Schema):
    # la clase Schema es la encargada de hacer las validaciones de todas las propiedades que definamos en esta clase
    # https://marshmallow.readthedocs.io/en/latest/marshmallow.fields.html
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    disponible = fields.Bool(required=False)


class ReservaSchema(Schema):
    # en el serializador el atributo se llamara horaInicio pero para guardarlo en la bd u obtenerlo usaremos la llave hora_inicio
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    horaInicio = fields.Str(attribute='hora_inicio', required=True)
    horaFin = fields.Str(attribute='hora_fin', required=True)
    adelanto = fields.Float()
    total = fields.Float(required=True)
    canchaId = fields.Int(required=True, attribute='cancha_id')


app = Flask(__name__)
# dict_row > retornara la informacion de la base de datos en un diccionario con los nombre de las columnas
conn = connect(environ.get('DATABASE_URL'), row_factory=dict_row)


def creacionTablas():
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS canchas (
        id SERIAL PRIMARY KEY,
        nombre TEXT,
        disponible BOOLEAN DEFAULT TRUE)
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id SERIAL PRIMARY KEY,
        nombre TEXT NOT NULL,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL,
        adelanto FLOAT,
        total FLOAT NOT NULL,
        cancha_id INT NOT NULL,
        FOREIGN KEY (cancha_id) REFERENCES canchas(id))
    ''')

    conn.commit()
    cursor.close()


creacionTablas()


@app.route('/canchas', methods=['POST', 'GET'])
def gestionCanchas() -> tuple[dict, int]:
    if request.method == 'POST':
        data = request.get_json()
        try:
            validador = CanchasSchema()
            dataValidada = validador.load(data)

            cursor = conn.cursor()
            cursor.execute('INSERT INTO canchas (nombre, disponible) VALUES (%s, %s) RETURNING *',
                           (dataValidada.get('nombre'), dataValidada.get('disponible', True)))

            conn.commit()  # Guardar los cambios de manera permanente
            canchaCreada = cursor.fetchone()

            cursor.description  # retorna la informacion de la data
            # en la posicion 0 de cada descripcion tendremos el nombre de la columna
            # en la posicion 1 tendremos el tipo de dato representado por su oid
            # columnas = [column[0] for column in cursor.description]

            # ES LO MISMO QUE ESTO
            columnas = []
            for column in cursor.description:
                columnas.append(column[0])

            cursor.close()

            resultado = validador.dump(canchaCreada)

            return {
                'message': 'Cancha creada exitosamente',
                'content': resultado
            }, 201  # Created

        except ValidationError as marshmalllowError:
            return {
                'message': 'Error al validar la data',
                'content': marshmalllowError.args
            }, 400  # Bad Request (mala solicitud)

    else:
        # METODO GET
        # obtener todas las canchas (fetchall)
        # devolveras, usando el CanchasSchema (dump(canchas, many=True))
        cursor = conn.cursor()
        serializador = CanchasSchema()
        cursor.execute('SELECT * FROM canchas')
        canchas = cursor.fetchall()

        # many=True es cuando tenemos varios registros y el serializador tiene que iterar estos registros para convertir o validar la data
        resultado = serializador.dump(canchas, many=True)

        return {
            'content': resultado
        }, 200  # Ok


@app.route('/reserva', methods=['POST'])
def crearReserva():
    # Crear un ReservaSchema con las validaciones correspondientes
    # al recibir la canchaId validar que esta cancha exista, si no existe, retornar un mensaje de error que la cancha es invalida
    # Si todo esta bien, crear la reserva
    # {
    #    "nombre": "Eduardo",
    #    "horaInicio": "10:00",
    #    "horaFin": "12:00",
    #    "adelanto": 0.0,
    #    "total": 90.00,
    #    "canchaId": 1,
    # }
    try:
        data = request.get_json()
        serializador = ReservaSchema()
        dataValidada = serializador.load(data)
        print(dataValidada.get('cancha_id'))
        cursor = conn.cursor()

        # Buscamos que la cancha exista
        cursor.execute('SELECT id FROM canchas WHERE id = %s',
                       (dataValidada.get('cancha_id'),))
        cancha = cursor.fetchone()

        # Si al buscar la cancha nos retorna None entonces no existe por ende retornamos un mensaje de error
        if cancha is None:
            return {
                'message': 'La cancha a reservar no existe'
            }, 400

        # Si la cancha existe, procederemos con la creacion de la reserva
        cursor.execute(
            'INSERT INTO reservas (nombre, hora_inicio, hora_fin, adelanto, total, cancha_id) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *', (
                dataValidada.get('nombre'),
                dataValidada.get('hora_inicio'),
                dataValidada.get('hora_fin'),
                dataValidada.get('adelanto'),
                dataValidada.get('total'),
                dataValidada.get('cancha_id')
            ))

        # Guardamos los cambios de manera permanente en la bd
        conn.commit()

        # Obtenemos la reserva creada gracias al `RETURNING *`
        reservaCreada = cursor.fetchone()
        cursor.close()

        resultado = serializador.dump(reservaCreada)

        return {
            'message': 'Reserva creada exitosamente',
            'content': resultado
        }, 201
    except ValidationError as marshmallowError:
        return {
            'message': 'Error al crear la reserva',
            'content': marshmallowError.args
        }, 400


if __name__ == "__main__":
    app.run(debug=True)
