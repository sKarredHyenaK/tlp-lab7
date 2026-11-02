from django.db import models
from django.contrib.auth.models import User

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
    

class Residencia(models.Model):
    numero = models.CharField(max_length=50, unique=True, verbose_name="Número de Residencia")
    detalles = models.CharField(max_length=100, blank=True, null=True, verbose_name="Detalles o Torre")

    def __str__(self):
        return f"Residencia {self.numero}"

class Correspondencia(models.Model):
    # Opciones fijas para el estado de la encomienda según el laboratorio
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Entregada', 'Entregada'),
    ]

    tipo = models.CharField(max_length=100, verbose_name="Tipo de encomienda (Ej: Carta, Paquete)")
    descripcion = models.TextField(verbose_name="Descripción detallada")
    fecha_recepcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de Recepción")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente', verbose_name="Estado")
    
    # Relación ForeignKey: Cada correspondencia pertenece obligatoriamente a una Residencia
    residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE, verbose_name="Residencia Destino")
    
    # Relación ForeignKey con el usuario de Django (el conserje que recibe)
    conserje_receptor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Conserje Receptor")

    def __str__(self):
        return f"{self.tipo} - Residencia {self.residencia.numero} ({self.estado})"