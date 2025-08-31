def calcular_igv():
    print('Calculando el igv')

# se pueden agregar parametros y se puede poner valores predeterminados a los parametros, si se proveen se asignan y si no se usa el valor predeterminado
def saludar(nombre, saludo = 'Buenos dias'):
    print(saludo, nombre)


saludar('Juancito', 'Buenas tardes')

saludar('Roberta')

# las funciones mayormente se usan para retornar un resultado y este pueda ser almacenado en una variable
# a partir de Python3.12 se puede TIPAR los parametros de la funcion, este tipado es DEBIL, osea , no obliga a pasar ese tipo de dato 
def sumar(numero1:int, numero2:int) ->int :
    resultado = numero1 + numero2

    return resultado

suma = sumar(10,40)
suma = sumar(numero1=10,numero2=40)

print(suma)


# podemos tener funciones que reciban parametros ilimitados
def sumatoria_infinita(*args) -> int:
    suma_total = 0
    for numero in args:
        suma_total += numero

    return suma_total

resultado = sumatoria_infinita(10,20,40,60,80,100)

print(resultado)

# kwargs > keyboard arguments
def creacion_persona(**kwargs):
    if 'mes' in kwargs:
        # podria validar si es que se esta proveyendo una llave incorrecta
        return 'Error parametro incorrecto'
    return kwargs

resultado = creacion_persona(nombre='Eduardo',
                             profesion='desarrollador',
                             mes='agosto')
print(resultado)

def creacion_persona_1(data:dict):
    if 'mes' in data :
        return 'Error parametro incorrecto'
    return data

resultado = creacion_persona_1({'nombre':'Eduardo',
                                'profesion':'desarrollador',
                                'mes':'agosto'})

print(resultado)

resultado = creacion_persona(**{'nombre':'Eduardo',
                                'profesion':'desarrollador',
                                'mes':'agosto'})

print(resultado)
