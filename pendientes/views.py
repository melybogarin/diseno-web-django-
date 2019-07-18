from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Tarea

from random import randint


# Create your views here.

def index(request):
    listita = Tarea.objects.all()

    persona = {
    "nombre":"Melissa",
    "edad":28,
    "hobbies": ["caminar","salir a pasear con mi familia"],
    "lista_tareas": listita,
    }
    return render(request, "inicio.html",persona)

def tarea (request):
    return HttpResponse("hola soy la vista de tarea")

def music (request):
    return HttpResponse(" hola estas buscando alguna cosa")
