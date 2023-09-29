from django.contrib import admin

# Register your models here.

from web.models import *
#user: matriculas
#psw: matriculas

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','nombre','password']

class AlumAdmin(admin.ModelAdmin):
    list_display = ['id','rut','nombre','apaterno','amaterno','direccion','email','fono']

class MatriculasAdmin(admin.ModelAdmin):
    list_display = ['id','tipcurcodigo','alumrut','sucursalId','matfecha']

class SucursalAdmin(admin.ModelAdmin):
    list_display = ['id','ciudadId','nombre']

class CiudadAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

class TipoCursoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','valor']




admin.site.register(Usuario,UserAdmin)
admin.site.register(alumnos,AlumAdmin)
admin.site.register(matricula,MatriculasAdmin)
admin.site.register(sucursal,SucursalAdmin)
admin.site.register(ciudad,CiudadAdmin)
admin.site.register(tipocurso,TipoCursoAdmin)





#class EmployeeAdmin(admin.ModelAdmin):
 #   list_display= ['nombre','email','fono']

#admin.site.register(Employee,EmployeeAdmin)