from django.db import models

# Create your models here.
class Residencia(models.Model):
    # Campo para guardar el número de la residencia (ej: "504", "Casa 12", etc.)
    # unique=True cumple con la regla de que cada residencia posee un número único.
    numero = models.CharField(max_length=50, unique=True, verbose_name="Número de Residencia")
    
    # Campo opcional para agregar detalles (ej: "Torre A", "Departamento")
    detalles = models.CharField(max_length=100, blank=True, null=True, verbose_name="Detalles o Torre")

    # Método para que en el panel de admin se muestre el número en lugar de "Residencia object (1)"
    def __str__(self):
        return f"Residencia {self.numero}"