from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombr Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    """ Personalizando un poco mi admin con la clase meta"""
    class Meta:
        verbose_name = 'Mi Departamento' 
        verbose_name_plural = 'Area de las Empresas' 
        ordering = ['-name']
        unique_together = ('name', 'shor_name') # Para que no se repita esta combinacion de elementos


    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name

