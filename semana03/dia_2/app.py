# convencion de como se debe de llamar el archivo principal de un proyecto de python
from flask import Flask, request
from psycopg import connect

# aplicacion de flask
app = Flask(__name__)

# Aca agregamos las credenciales siguiendo el formato postgresql://USERNAME:PASSWORD@HOST:PUERTO/NOMBRE_BD
credenciales = 'postgresql://postgres:root@localhost:5432/flask_db'
conexion = connect(conninfo=credenciales)

@app.route('/estado')
def estado():
    # es el encargo de conectarse con la bd
    cursor = conexion.cursor()

    # ejecuta el script en la bd
    cursor.execute('SELECT now();')

    # fetchall > retorna todos los registros en una lista
    # fetchmany(cantidad) > retorna la cantidad de registros como maximo indicada
    # fetchone > retorna el primero registro de la query
    resultado = cursor.fetchone()
    fecha = resultado[0]

    # Es necesario cerrar la conexion para evitar hacer un overflow de conexion en la bd y generar un trafico innecesario de conexion
    cursor.close()
    
    stringFecha = fecha.strftime('%Y-%m-%d %H:%M:%S')
    return {
     'hora': stringFecha
    }

@app.route('/producto', methods = ['POST'])
def crearProducto():
    data = request.get_json()

    cursor = conexion.cursor()
    # en el script se suele colocar %s cuando queremos hacer la conversion de nuestras variables a string, 
    # En los string comunes de python podemos utilizar %f para flotantes y adicionalmente el %i para la conversion a enteros. Estos tambien evitan posibles ataques de SQL-INYECTION
    cursor.execute('INSERT INTO productos (nombre, precio, observacion, fecha_caducidad) VALUES (%s, %s, %s, %s ) RETURNING *',(
        data.get('nombre'), 
        data.get('precio'), 
        data.get('observacion'), 
        data.get('fechaCaducidad')))
    
    # Los cambios se guardaran de manera PERMANENTE en la bd
    conexion.commit()
    
    nuevoProducto = cursor.fetchone()

    print(nuevoProducto)
    return {
        'message': 'Producto creado exitosamente',
        'producto': '' # { 'nombre' : '', 'precio':'', ...}
    }

@app.route('/productos', methods = ['GET'])
def devolverProducto():
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    
    resultado = []
    for producto in productos:
        informacion = {
            'id': producto[0],
            'nombre': producto[1],
            'precio': producto[2],
            'observaciones': producto[3],
            'fechaCaducidad': producto[4].strftime('%Y-%m-%d %H:%M:%S'),
            'fechaCreacion': producto[5].strftime('%Y-%m-%d %H:%M:%S')
        }

        resultado.append(informacion)


    return{
        'Message' : 'Productos recuperados',
        'content' : resultado
    }


if __name__ == '__main__':
    # asi nos aseguramos de que la instancia de Flask este en el archivo principal del proyecto
    app.run(port=5000, debug=True)