from django.db import models
from applications.departamento.models import Departamento
#from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad' 
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    

# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""

    JOB_CHOICE = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    # Contador
    # Administrador
    # Economista
    # Otros

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField(
        'Nombres Completos', 
        max_length=120,
    )
    job = models.CharField('Trabajos', max_length=1, choices=JOB_CHOICE)

    # ForeingKey ---> Relacion de uno a uno"
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


    #ImageField ---> Lo veremos luego
    avatar_emp = models.ImageField(upload_to='media_empleados', blank=True, null=True)

    #  ---> Relacion de mucho a mucho
    habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name', 'last_name']
        unique_together = ['first_name', 'departamento']

    #hoja_vida = RichTextField()


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name