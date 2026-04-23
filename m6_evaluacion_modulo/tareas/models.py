from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length=60)
    numero = models.IntegerField()
    estado = models.CharField(max_length=20)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        permissions = [
            ("view_all_tarea", "Ver todas las tareas"), #(codigo_permiso, "Nombre visible")
        ]
        
