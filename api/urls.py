from unicodedata import name
from django import views
from django.urls import path
from api.views import listaAlumnos, detailAlumno, listaMatriculas, detailMatricula

urlpatterns = [
    path('api/alumnos',listaAlumnos.as_view()),

    path('api/alumno/<id>', detailAlumno.as_view()),

    path('api/matriculas/', listaMatriculas.as_view()),

    path('api/matricula/<id>', detailMatricula.as_view()),



]