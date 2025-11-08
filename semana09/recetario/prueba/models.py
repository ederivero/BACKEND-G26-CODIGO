from django.db import models


# https://docs.djangoproject.com/en/5.2/topics/db/models/
class Nota(models.Model):
    # https://docs.djangoproject.com/en/5.2/ref/models/fields/
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)

    # Si queremos modificar informacion de la tabla usaremos la clase Meta
    class Meta:
        # https://docs.djangoproject.com/en/5.2/ref/models/options/
        db_table = 'notas'
        # Cambiar la forma en al cual se va a mostrar la info en el panel administrativo
        verbose_name = 'notita'
        verbose_name_plural = 'notitas'
