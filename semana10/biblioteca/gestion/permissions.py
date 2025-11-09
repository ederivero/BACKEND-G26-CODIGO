from rest_framework.permissions import BasePermission
# from rest_framework.
class EsAdmin(BasePermission):
    # Para modificar el mensaje si la respuesta es False entonces se puede hacer mediante el atributo message
    message='No tienes los privilegios suficientes para realizar esta accion'

    def has_permission(self, request, view):
        # en el request tenemos toda la data que envia el cliente (data, method, headers, user)
        if not request.user:
            return False
        # Si el usuario es anonimo (no esta autenticado) tenemos un atributo is_anonymous 
        # Si el metodo es get no hacer la validacion y retornar verdadero y si no validar que no este anonimo
        if request.method == 'GET':
            return True
        
        print(request.user.is_anonymous)
        # Aca obtenemos el valor del tipoUsuario
        tipoUsuario = request.user.tipoUsuario

        return tipoUsuario == '1'
    
class EsPersonal(BasePermission):
    message='No tienes los privilegios suficientes para realizar esta accion'

    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        
        tipoUsuario = request.user.tipoUsuario

        return tipoUsuario == '2'