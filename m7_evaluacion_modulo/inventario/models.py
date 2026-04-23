from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    dimensiones = models.CharField(max_length=120, blank=True)
    peso_kg = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    info_adicional = models.TextField(blank=True)

    def __str__(self):
        parts = []
        if self.dimensiones:
            parts.append(self.dimensiones)
        if self.peso_kg:
            parts.append(f"{self.peso_kg} kg")
        return " / ".join(parts) if parts else "Detalle"


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, related_name='productos')
    detalle = models.OneToOneField(DetalleProducto, on_delete=models.CASCADE, null=True, blank=True, related_name='producto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
