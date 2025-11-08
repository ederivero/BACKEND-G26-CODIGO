from django.db import models


class Receta(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    descripcion = models.TextField()
    dificultad = models.IntegerField()

    class Meta:
        db_table = 'recetas'


class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(null=False)
    cantidad = models.TextField(null=False)
    recetaId = models.ForeignKey(
        to=Receta, on_delete=models.CASCADE, db_column='receta_id')

    class Meta:
        db_table = 'ingredientes'


class Preparacion(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    descripcion = models.TextField(null=False)
    orden = models.IntegerField()
    recetaId = models.ForeignKey(
        to=Receta, on_delete=models.CASCADE, db_column='receta_id')

    class Meta:
        db_table = 'preparaciones'
