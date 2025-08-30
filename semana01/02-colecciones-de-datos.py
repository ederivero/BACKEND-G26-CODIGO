# Variables que pueden almacenar diferente informacion

# Lista (Arreglo)
# Modificables y ordenadas
numeros_telefonicos = ['104', '105', '974207075', '944566384', "123"]

# En la colecciones de datos se pueden agregar diferente tipos de datos dentro de sus elementos
numeros_telefonicos.append(False)
numeros_telefonicos.append(10.5)

print(numeros_telefonicos)
print(numeros_telefonicos[0])
# Tambien se puede obtener un sub conjunto de elementos de la lista
print(numeros_telefonicos[1:3])

# Todos los elementos desde la posicion 2
print(numeros_telefonicos[2:])

# Todos los elementos hasta la posicion <2
print(numeros_telefonicos[:2])

# Para obtener el ultimo elemento usamos valores negativos y asi se invierte la lista
print(numeros_telefonicos[-1])

print('--------------------')

# Formas de eliminar elementos de una lista

# Con el metodo pop retiramos el elemento de la lista y lo podemos almacenar en otra variable
valor_eliminado = numeros_telefonicos.pop(0)
print(valor_eliminado)
print(numeros_telefonicos)

# del > Sirve para eliminar variables (liberar espacio de memoria) y tambien se puede eliminar elementos de una lista
del numeros_telefonicos[1]
print(numeros_telefonicos)

# si se quiere limpiar completamente la lista
numeros_telefonicos.clear()
print(numeros_telefonicos)

print('-----------')
ejercicio_1 = [1, 'Eduardo', 'de Rivero', False, 32, 20.5, [4,8,12]]

# Como hago para obtener a 'de Rivero'
print(ejercicio_1[2])

# Como hago para obtener desde Eduardo hasta 32
print(ejercicio_1[1:5])

# Como hago para obtener la penultima posicion 20.5
print(ejercicio_1[-2])

# Como hago para obtener el valor 8
# al ser una lista dentro de la lista puedo ingresar a sus posiciones dentro de la sublista 
print(ejercicio_1[6][1])