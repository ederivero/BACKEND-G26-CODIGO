from django.db import models
# BaseUserManager es la clase que sirve para ver como se gestiona el usuario de la tabla auth_user
# AbstractBaseUser permite la modificacion TOTAL del modelo del usuario
# PermissionsMixin permite la iteraccion con las otras tablas de permisos como la de auth_permissions y la de auth_group_permissions
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django_ulid.models import default, ULIDField

class ManejadorUsuario(BaseUserManager):
    # al heredar esa clase podemos usar un metodo llamado create_superuser
    def create_superuser(self, nombre, correo, password):
        # Este metodo es el que se ejecuta cuando se quiere crear un superusuario por consola
        # py manage.py createsuperuser
        if not correo:
            raise ValueError('El correo es obligatorio')

        correoNormalizado = self.normalize_email(correo)

        nuevoUsuario = self.model(correo=correoNormalizado, nombre=nombre)
        # hacemos el hash de la password
        nuevoUsuario.set_password(password)
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        # Guardamos el usuario en la bd
        nuevoUsuario.save()

TIPO_USUARIO = [
    ('1','ADMIN'),
    ('2','USUARIO'),
    ('3','PERSONAL')
]

class Usuario(AbstractBaseUser,PermissionsMixin):
    id = ULIDField(primary_key=True, default=default)
    nombre = models.TextField(null=False)
    apellido = models.TextField()
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    # NOT NULL
    tipoUsuario = models.TextField(db_column='tipo_usuario', choices=TIPO_USUARIO)

    # Ahora se agrega algunos otros elementos que son necesarios para el panel administrativo como 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Ahora agregamos el campo que se usara para cuando se quiera hacer login en el panel administrativo
    USERNAME_FIELD = 'correo'

    # Indicamos los atributos que se debe de solicitar en la terminal cuando se cree un superusuario, obviar el USERNAME_FIELD y el password porque esos de por si ya son requeridos
    REQUIRED_FIELDS = ['nombre']

    # ahora modificamos la configuracion de nuestro usuario por la terminal
    objects = ManejadorUsuario()

    class Meta:
        db_table='usuarios'

class Categoria(models.Model):
    id = ULIDField(primary_key=True, default=default)
    nombre = models.TextField(unique=True)

    class Meta:
        db_table = 'categorias'

class Libro(models.Model):
    id = ULIDField(primary_key=True, default=default)
    nombre = models.TextField(null=False)
    autor = models.TextField(null=False)
    edicion = models.TextField(null=False)
    descripcion = models.TextField()
    # on_delete | on_update > sirve para yo poder gestionar como se va a comportar mi registro con relacion al 'padre' 
    # CASCADE > si elimino una categoria se eliminan sus libros
    # PROTECT > no permite la eliminacion de la categoria si tiene libros
    # RESTRICT > es similar al PROTECT solo que emite un error de tipo RestrictedError cuando se quiere hacer la eliminacion
    # SET_NULL > permite la eliminacion de la categoria y a los libros los deja huerfanos es decir le cambia su valor a null
    # SET_DEFAULT > permite la eliminacion de la categoria y agarra el valor por defecto que configuramos y lo cambia
    # DO_NOTHING > permite la eliminacion de la categoria y aun mantiene el valor de los libros hacia la categoria que ya no existe
    categoriaId = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, db_column='categoria_id', related_name='libros')

    class Meta:
        db_table = 'libros'

class Prestamo(models.Model):
    id = ULIDField(primary_key=True, null=False, default=default)
    # related_name > es el atributo que se creara de manera virtual cuando quiera accdeder a mis prestamos desde mis libros, es decir, en la clase Libro se creara un atributo llamado 'prestamos' y asi yo podre ver todos los prestamos de un libro en especifico sin la necesidad de tener que hacer otra consulta
    libroId = models.ForeignKey(to=Libro, on_delete=models.PROTECT, db_column='libro_id', related_name='prestamos')
    usuarioId = models.ForeignKey(to=Usuario,on_delete=models.PROTECT, db_column='usuario_id', related_name='librosPrestadosUsuarios')
    fecha = models.DateField(null=False)
    estado = models.TextField()

    class Meta:
        db_table='prestamos'