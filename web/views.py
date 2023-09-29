from django.shortcuts import redirect, render
from web.models import *

#user
#from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

#forms
from . import forms
from .forms import AlumnoForm, CiudadForm, CustomUserCreationForm, MatriculaForm, TipoCursoForm, SucursalForm
# Create your views here.

#filters
from .filters import AlumnosFilter, MatriculasFilter, CiudadFilter, SucursalFilter, tCursoFilter, UserFilter

#pagination
#from django.core.paginator import Paginator  --- paginator
#from django.http import Http404   --- paginator

def BaseIndex(request):
    usNombre = Usuario()

    data = {
        "us" : usNombre
    }

    return render(request, 'base.html', data)

def Index(request):
    alum = alumnos.objects.all()[:3]
    tip = tipocurso.objects.all()[:3]
    suc = sucursal.objects.all()[:3]

    data ={
        'alumno' : alum,
        'tp' : tip,
        'sucursales' : suc
    }


    return render(request,'index.html',data)

def Iniciar(request):
    data={'estado':'0'} #Sin Usuario
    return render(request,'./registration/login.html')

def Login(request):
    us=Usuario()
    user=Usuario()
    if request.method=='POST':
        us.usuario=request.POST['txtuser']
        us.password=request.POST['txtpassword']
        print("PASE EL POST --->" + us.usuario + us.password)
        try:
            user=Usuario.objects.get(usuario=us.usuario,password=us.password)
            data={'usuario':user.usuario,"nombre":user.nombre,'estado' : '1'} #Usuario encontrado
            print("PASE EL TRY --->" + us.usuario + us.password)
            return render(request,'../index.html',data)
        except:
            #data={'estado':'2','usuario':us.usuario,"password":us.password} #No Encontrado
            #print("PASO EL except")
            #return render(request,'./registration/login.html',data)   
            print('EXCEPT----')
    else:
        data={'estado':'0'} #Sin Usuario
        return render(request,'./registration/login.html')

## users ##

def IndexUser(request):
    u = Usuario.objects.all()
#s
    u_filter = UserFilter(request.GET, queryset = u)
#s    #page = request.GET.get('page',1)
#s    #try:
    #    paginator = Paginator( u, 5)
    #    u = paginator.page(page)
    #except:
    #    raise Http404#
    data = {
        'usuario' : u_filter
    #    'entity' : u,   // entity porque asi viene en el paginator.html // entity = user
    #    'paginator' : paginator
    }
    return render(request,'./usuarios/index.html',data)
#s
#sdef Usuario(request,id):
#s    u = Usuario.objects.get(id=id)
#s    data = {
#s        'usu' : u
#s    }
#s    return render(request,'./usuarios/usuario.html',data)

## users ##


#def Login(request): 
#
#    return render(request,'./registration/login.html')

def Registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)

            return redirect(to='index')
        data['form'] = formulario
    return render(request, './registration/registro.html',data)


def CerrarSesion(request):
    logout(request)
    return redirect('login')

## LOGIN / USERS ##


#---------------------------------------------------------


##  ALUMNOS ALUMNOS ##

def IndexAlumnos(request):

    #alum = alumnos.objects.filter(nombre__contains='L')

    alumno = alumnos.objects.all()

    alumno_filter = AlumnosFilter(request.GET, queryset=alumno)

    

    data = {
        'alumnos' : alumno_filter,

        #'al' : alum
    }
    return render(request,'./alumnos/index.html',data)

def Alumno(request,id):
    
    alumno = alumnos.objects.get(id=id)

    data = {
        'alum' : alumno, 
        'titulo' : 'alumno'
    }

    return render(request, './alumnos/alumno.html', data)

def AddAlumno(request):
    form = AlumnoForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(to='IndexAlumnos')
    data = {
        'form' : form
    }

    return render(request, './alumnos/agregar-alumno.html', data)

def DeleteAlumno(request,id):

    alum = alumnos.objects.get(id=id)
    alum.delete()
    return redirect('IndexAlumnos')

def EditAlumno(request,id):

    alumno = alumnos.objects.get(id=id)

    form = AlumnoForm(instance=alumno)

    data = {
        'alumno' : alumno,
        'form' : form
    }

    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance = alumno)
        if form.is_valid():
            form.save()
        return redirect(to='IndexAlumnos')

    return render(request,'alumnos/modificar-alumno.html',data)

##  ALUMNOS ALUMNOS ##


#---------------------------------------------------------


## MATRICULAS MATRICULAS MATRICULAS MATRICULAS ##

from django.db.models import Sum

def IndexMatriculas(request):
    
    suc = sucursal.objects.all()

    matriculas = matricula.objects.all()

    matricula_filter = MatriculasFilter(request.GET, queryset=matriculas)

    suma = 0

    for x in matricula_filter.qs:
        suma = x.tipcurcodigo.valor + suma

    #total = matricula_filter.tipcurcodigo.objects.all().aggregate(Sum('valor')) 

    data = {
        'matriculas' : matricula_filter,
        'ciudad' : suc,
        'total' : suma


    }

    return render(request,'./matriculas/index.html', data)

def Matricula(request,id):
    
    m = matricula.objects.get(id=id)

    data = {
        'm' : m, 
    }

    return render(request, './matriculas/matricula.html', data)


def DeleteMatricula(request,id):
    
    m = matricula.objects.get(id=id)
    m.delete()

    return redirect('IndexMatriculas')

       #form = AlumnoForm(request.POST, instance = alumno)
        #if form.is_valid():
        #    form.save()
        #return redirect(to='IndexAlumnos')

def AddMatricula(request):
    matri = matricula()
    if request.method == 'POST':
        matri.matfecha = request.POST["fecha"]
        #tipo curso codigo
        matri.tipcurcodigo = tipocurso.objects.get(id=request.POST["ticurso"])
        #rut alumno
        matri.alumrut = alumnos.objects.get(id=request.POST["alu"])
        #sucursal id
        matri.sucursalId = sucursal.objects.get(id=request.POST["sucursal"])
        matri.save()
        return redirect(to='IndexMatriculas')
    else:
        tipcurso = tipocurso.objects.all()
        alum = alumnos.objects.all()
        sucur = sucursal.objects.all()

        data = {
                'sucursales' : sucur,
                'alumn' : alum,
                'tipC' : tipcurso,

            }
        return render(request, './matriculas/agregar-matricula.html', data)


def EditMatricula(request,id):
    matri = matricula.objects.get(id=id)
    tipcurso = tipocurso.objects.all()
    alum = alumnos.objects.all()
    sucur = sucursal.objects.all()
    data ={
        'matriculas' : matri,
        'sucursales' : sucur,
        'alumn' : alum,
        'tipC' : tipcurso
    }
    if request.method == 'POST':
        matri.matfecha = request.POST["fecha"]
        matri.tipcurcodigo = tipocurso.objects.get(id=request.POST["ticurso"])
        matri.alumrut = alumnos.objects.get(id=request.POST["alu"])
        matri.sucursalId = sucursal.objects.get(id=request.POST["sucursal"])
        matri.save()
        return redirect(to='IndexMatriculas')
    else:
        return render(request,'./matriculas/modificar-matricula.html',data)



## MATRICULAS MATRICULAS MATRICULAS MATRICULAS ##

#---------------------------------------------------------

## CIUDADES CIUDADES CIUDADES CIUDADES CIUDADES CIUDADES ##

def IndexCiudades(request):
    c = ciudad.objects.all()

    c_filter = CiudadFilter(request.GET, queryset=c)

    data = {
        'ciudad' : c_filter
    }
    return render(request,'./ciudades/index.html',data)

def Ciudad(request,id):
    ciu = ciudad.objects.get(id=id)

    data = {
        'ciudad' : ciu
    }
    return render(request,'./ciudades/ciudad.html',data)

def AddCiudad(request):
    form = CiudadForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(to='IndexCiudades')
    data = {
        'form' : form
    }
    return render(request, './ciudades/agregar-ciudad.html', data)

def EditCiudad(request,id):
    city = ciudad.objects.get(id=id)
    form = CiudadForm(instance=city)

    data = {
        'ciu' : city,
        'form' : form
    }
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance = city)
        if form.is_valid():
            form.save()
        return redirect(to='IndexCiudades')

    return render(request,'ciudades/modificar-ciudad.html',data)

def DeleteCiudad(request,id):

    ciu = ciudad.objects.get(id=id)
    ciu.delete()

    return redirect('IndexCiudades')

    
## CIUDADES CIUDADES CIUDADES CIUDADES CIUDADES CIUDADES ##


#---------------------------------------------



#---------------------------------------------
## Sucursales ##

def IndexSucursal(request):

    suc = sucursal.objects.all()

    suc_filter = SucursalFilter(request.GET, queryset=suc)

    data = {
        'sucursal' : suc_filter
    }

    return render(request,'./sucursales/index.html',data)

def Sucursal(request,id):
    
    sucu = sucursal.objects.get(id=id)
    data = {
        'sucursal' :sucu
    }

    return render(request,'./sucursales/sucursal.html',data)

def AddSucursal(request):
    comuna = sucursal()
    if request.method == 'POST':
        comuna.nombre = request.POST["txtcomuna"]
        ciudadd = ciudad.objects.get(id=request.POST["ciudad"])
        comuna.ciudadId = ciudadd
        comuna.save()
        return IndexSucursal(request)
    else:
        ciudades = ciudad.objects.all()
        data = {
            'ciudades' : ciudades
        }

    return render(request,'./sucursales/agregar-sucursal.html',data)

def EditSucursal(request,id):
    sucu = sucursal.objects.get(id=id)
    ciu = ciudad.objects.all()
    data ={
        'sucursales' : sucu,
        'ciu' : ciu,
    }
    if request.method == 'POST':
        sucu.nombre = request.POST["nombre"]
        sucu.ciudadId = ciudad.objects.get(id=request.POST["ciudadid"])
        sucu.save()
        return redirect(to='IndexSucursales')
    else:
    
        return render(request,'sucursales/modificar-sucursal.html',data)

    

def DeleteSucursal(request,id):
    
    suc = sucursal.objects.get(id=id)
    suc.delete()

    return redirect(to='IndexSucursales')


## Sucursales ##



#---------------------------------------------



## Tipo curso ##

def IndexTipoCurso(request):
    
    tip = tipocurso.objects.all()

    tip_filter = tCursoFilter(request.GET, queryset = tip)

    data = {
        'tipo' : tip_filter
    }

    return render(request,'./tipoCurso/index.html',data)

def TipoCurso(request,id):

    tp = tipocurso.objects.get(id=id)
    data = {
        'tipo' :tp
    }

    return render(request,'./tipoCurso/tipoCurso.html',data)

def AddTipoCurso(request):

    form = TipoCursoForm(data=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(to='IndexTipoCurso')
    data = {
        'form' : form
    }

    return render(request,'./tipoCurso/agregar-tipoCurso.html',data)

def EditTipoCurso(request,id):
    
    tip = tipocurso.objects.get(id=id)
    form = TipoCursoForm(instance=tip)

    data = {
        'tipo' : tip,
        'form' : form
    }
    if request.method == 'POST':
        form = TipoCursoForm(request.POST, instance = tip)
        if form.is_valid():
            form.save()
        return redirect(to='IndexTipoCurso')

    return render(request,'tipoCurso/modificar-tipoCurso.html',data)


def DeleteTipoCurso(request,id):
    
    tip = tipocurso.objects.get(id=id)
    tip.delete()

    return redirect(to='IndexTipoCurso')



