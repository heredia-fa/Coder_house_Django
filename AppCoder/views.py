from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(req):
    curso = Curso(nombre= "Desarrolo Web" , camada="19969")
    curso.save()
    doc_text= f"Curso: {curso.nombre} Camada: {curso.camada}  fue agreagado"

    return HttpResponse(doc_text)

