from faker import Faker
from datetime import date
# Creamos una instancia de nuestra clase
# instancia: copia de toda la configuracion de la clase que va a ser almacenada en la variable
creador = Faker()

texto = 'INSERT INTO profesores (nombre, apellidos, correo, correo_institucional, activo, fecha_contratacion) VALUES '

for numero in range(100):
    nombre = creador.first_name()
    apellidos = creador.last_name()
    correo = creador.email(True)
    correo_institucional = creador.email(True,'codigo.edu.pe')
    activo = creador.boolean()
    fecha_contratacion = creador.date_between(start_date=date(2022,1,15),end_date=date(2025,8,1))

    data = "('{}','{}','{}','{}',{},'{}'),".format(nombre,
                                                  apellidos,
                                                  correo,
                                                  correo_institucional,
                                                  activo,
                                                  fecha_contratacion)

    # Al ser string no se hara sumatoria sino se realizara una concatenacion
    texto += data
    # En el ultimo registro en vez de colocar una coma se coloque un `;`

resultado = texto.rsplit(',',1)[0] + ';'

print(resultado)

# agregando al comando `> NOMBRE_ARCHIVO.EXT` en vez de mostrarlo en la terminal las impresiones de pantalla lo guardara en ese archivo definido en la terminal


# Para leer este archivo en la terminal
# MAC | Powershell | GitBash : cat
# CMD (windows): type