from django import forms


class Curso_formulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()