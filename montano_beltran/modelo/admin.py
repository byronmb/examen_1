from django.contrib import admin
from .models import Estudiante
# Register your models here.
class AdminEstudiante(admin.ModelAdmin):
    list_display = ["matricula", "cedula", "nombres", "apellidos", "ciclo", "paralelo"]
    list_editable = ["cedula", "nombres"]
    list_filter = ["matricula"]
    search_fields = ["matricula"]
    class Meta:
        model = Estudiante
admin.site.register(Estudiante, AdminEstudiante)

