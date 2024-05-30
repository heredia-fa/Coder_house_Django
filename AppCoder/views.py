from django.shortcuts import render
from django.http import HttpResponse
# from AppCoder import models
from .models import *
from .forms import *



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

# Esto esta mal no se hace asi

# def curso_formulario(req):

#     if req.method =="POST":

#         curso = Curso( nombre=req.POST["Curso"], camada=req.POST["Camada"])

#         curso.save()

#         return render(req,"AppCoder/inicio.html")
    
#     return render(req, "AppCoder/curso_formulario.html")


def curso_formulario(req):

    if req.method == "POST":

        mi_formulario = Curso_formulario(req.POST)
        
        print(mi_formulario)

        if mi_formulario.is_valid:

            Informacion = mi_formulario.cleaned_data

            curso = Curso(nombre=Informacion["curso"] , camada=Informacion["camada"])

            curso.save()

            return render(req, "AppCoder/inicio.html", {"message" : "Curso creado"})
        
        
        else :
            return render(req, "AppCoder/inicio.html" , {"message" : "Datos erroneos"})

    else:

        mi_formulario = Curso_formulario()
        
        return render(req, "AppCoder/curso_formulario.html", {"mi_formulario":mi_formulario})
    

def busqueda_camada(req):
    
    return render(req, "AppCoder/busqueda_camada.html")

def resultado_bcamada(req):
    
    if req.GET["camada"]:

        camada = req.GET["camada"]

        #curso = Curso.objects.get(camada=camada)
        cursos = Curso.objects.filter(camada__icontains=camada)
        

        return render(req, "AppCoder/resultado_busqueda.html" , {"cursos" : cursos , "camada" :camada})
    
    else:

      return render(req, "AppCoder/inicio.html" , {"message" : "No enviaste el dato camada"})
