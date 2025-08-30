saludo = 'Bienvenidos al curso de Backend'
print(saludo)
print(type(saludo))

# En python se puede cambiar el contenido de una variable a diferentes tipos de datos, como por ejemplo, de un texto a un numero
saludo = 20
print(saludo)
print(type(saludo))

# Se puede usar comillas simples o dobles como mejor lo desee PERO
# Se DEBE usar comillas siemples cuando dentro del texto tengamos comillas dobles 
texto = "Buenos dias con todos! 'Aleluya!'"
texto = 'Buenos dias "Juan"! '

texto = "Buenos dias con todos! 'Aleluya!'"

# Si queremos tener un texto con saltos de lineas entonces usaremos la triple comilla simple o triple comilla doble
dialogo = '''Ahora, les contare un ejemplo de salto de linea
    Esta es una nueva linea
Y esta es otra linea
 Y una ultima mas'''

print(dialogo)

curso, mes, dia, habilitado, nota = "Backend", "Agosto", 30, True, 14.5

print(curso)

# Str | Int | Float | Boolean
print(type(curso))
print(type(dia))
print(type(habilitado))
print(type(nota))