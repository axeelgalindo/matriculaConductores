from rest_framework import serializers

from web.models import alumnos, matricula

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = alumnos
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = matricula
        fields = '__all__'