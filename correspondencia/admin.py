from django.contrib import admin
from django.contrib import admin
from .models import Residencia, Correspondencia

# Register your models here. 

# Registramos el modelo Residencia en el panel de administración
admin.site.register(Residencia)

admin.register(Correspondencia)
class CorrespondenciaAdmin(admin.ModelAdmin):
    # Campos que se verán como columnas en la tabla del panel de administración
    list_display = ('tipo', 'residencia', 'estado', 'fecha_recepcion', 'conserje_receptor')
    
    # Filtros laterales para buscar por estado o fecha
    list_filter = ('estado', 'fecha_recepcion')
    
    # Buscador en la parte superior
    search_fields = ('tipo', 'descripcion', 'residencia__numero')

    # REGLA CLAVE DEL LAB: Capturar automáticamente al usuario autenticado (conserje)
    def save_model(self, request, obj, form, change):
        if not change:  # Si el registro es nuevo (se está creando)
            obj.conserje_receptor = request.user  # Asigna al usuario que ha iniciado sesión
        super().save_model(request, obj, form, change)