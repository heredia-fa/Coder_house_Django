from django.shortcuts import render
from django.http import HttpResponse
from AppCoder import models


# Create your views here.

# def curso(req):
#     curso = Curso(nombre= "Desarrolo Web" , camada="19969")
#     curso.save()
#     doc_text= f"Curso: {curso.nombre} Camada: {curso.camada}  fue agreagado"

#     return HttpResponse(doc_text)

def inicio(req):

    return render(req,"AppCoder/inicio.html")

def cursos(req):

    return render(req,"AppCoder/cursos.html")

def profesores(req):

    return render(req,"AppCoder/profesores.html")

def estudiantes(req):

    return render(req,"AppCoder/estudiantes.html")

def entregables(req):

    return render(req,"AppCoder/entregables.html")
