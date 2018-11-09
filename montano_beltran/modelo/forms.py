from django import forms

from modelo.models import Estudiante


class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model =Estudiante
        fields =["matricula", "cedula","nombres", "apellidos","ciclo","paralelo"]


