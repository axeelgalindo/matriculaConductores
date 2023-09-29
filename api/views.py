from django.shortcuts import render

from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound

from web.models import alumnos, matricula

from .serializers import AlumnoSerializer, MatriculaSerializer

from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# Create your views here.

class listaAlumnos(APIView):
    def get(self,request):
        alu = alumnos.objects.all()
        serializer = AlumnoSerializer(alu, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AlumnoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class detailAlumno(APIView):
    def get_object(self,id):
        try:
            return alumnos.objects.get(id=id)
        except alumnos.DoesNotExist:
            raise Http404
            #return HttpResponseNotFound

    def get(self, request, id):
        alu = self.get_object(id)
        serializer = AlumnoSerializer(alu)
        return Response(serializer.data)
    
    def put(self, request,id):
        alu = self.get_object(id)
        serializer = AlumnoSerializer(alu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id):
        alu = self.get_object(id)
        alu.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#MatriculaSerializer,matricula

class listaMatriculas(APIView):
    def get(self,request):
        mat = matricula.objects.all()
        serializer = MatriculaSerializer(mat, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MatriculaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class detailMatricula(APIView):
    def get_object(self,id):
        try:
            return matricula.objects.get(id=id)
        except matricula.DoesNotExist:
            raise Http404
            #return HttpResponseNotFound

    def get(self, request, id):
        mat = self.get_object(id=id)
        serializer = MatriculaSerializer(mat)
        return Response(serializer.data)
    
    def put(self, request,id):
        mat = self.get_object(id=id)
        serializer = MatriculaSerializer(mat, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id):
        mat = self.get_object(id=id)
        mat.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


