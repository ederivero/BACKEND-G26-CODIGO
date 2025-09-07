from faker import Faker
from datetime import date
# Creamos una instancia de nuestra clase
# instancia: copia de toda la configuracion de la clase que va a ser almacenada en la variable
creador = Faker()

print(creador.name())

nombre = creador.first_name()
apellidos = creador.last_name()
correo = creador.email(True)
correo_institucional = creador.email(True,'codigo.edu.pe')
activo = creador.boolean()
fecha_contratacion = creador.date_between(start_date=date(2022,1,15),end_date=date(2025,8,1))

