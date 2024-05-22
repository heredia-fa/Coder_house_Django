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

    return HttpResponse("Vista Inicio")

def cursos(req):

    return HttpResponse("Vista cursos")

def profesores(req):

    return HttpResponse("Vista profesores")

def estudiantes(req):

    return HttpResponse("Vista estudiantes")

def entregables(req):

    return HttpResponse("Vista entregables")
