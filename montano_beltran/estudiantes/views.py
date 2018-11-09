from django.shortcuts import render, redirect
from modelo.models import Estudiante
from modelo.forms import FormularioEstudiante
# Create your views here.
def principal (request):
    listaEstudiantes = Estudiante.objects.all()
    context = {
        'lista': listaEstudiantes
    }
    return render(request, 'estudiante/principal_estudiante.html', context)

def crear (request):
    formulario = FormularioEstudiante(request.POST)

    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data        #arreglo de todos los datos q tiene el formulario
            estudiante = Estudiante()
            estudiante.matricula = datos.get('matricula')
            estudiante.cedula = datos.get('cedula')
            estudiante.nombres = datos.get('nombres')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.ciclo = datos.get('ciclo')
            estudiante.paralelo=datos.get('paralelo')

            estudiante.save()
            return redirect(principal)
    context = {
        'fa': formulario,

    }
    return render(request, 'estudiante/crear_estudiante.html', context)

def modificar(request):
    numEst = request.GET['matricula']
    estudiante = Estudiante.objects.get(matricula = numEst)
    formulario = FormularioEstudiante(request.POST, instance=estudiante)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante.matricula = datos.get('matricula')
            estudiante.cedula = datos.get('cedula')
            estudiante.nombres = datos.get('nombres')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.ciclo = datos.get('ciclo')
            estudiante.paralelo = datos.get('paralelo')
            estudiante.save()
            return redirect(principal)
    else:
        formulario = FormularioEstudiante(instance=estudiante)

    context = {
        'f': formulario,
    }
    return render(request, 'estudiante/crear_estudiante.html', context)

def eliminar(request):
    numEst = request.GET['matricula']
    estudiante = Estudiante.objects.get(matricula=numEst)
    estudiante.estado = False
    estudiante.save()
    return redirect(principal)