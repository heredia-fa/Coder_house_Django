from django.urls import path

from AppCoder import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name = "Cursos"),
    path('profesores/', views.profesores, name = "Profesores"),
    path('estudiantes/', views.estudiantes, name = "Estudiantes"),
    path('entregables/', views.entregables, name = "Entregables"),
    path('curso_formulario/', views.curso_formulario , name = "Curso_Formulario"),
    path('busqueda_camada/', views.busqueda_camada, name = "Busqueda_Camada"),
    path('resultado_camada/', views.resultado_bcamada, name = "resultado_Bcamada"),


]
