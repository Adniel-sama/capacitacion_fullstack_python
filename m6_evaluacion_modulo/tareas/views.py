from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
# Create your views here.

#Importar Modelo auth: User, authenticate, login, logout, decoradores (@login_required, @permission_required)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

#Obtener a los 2 usuarios
elena = User.objects.get(username='elena')
juana = User.objects.get(username='juana')
homero = User.objects.get(username='homero')
bart = User.objects.get(username='bart')
lisa = User.objects.get(username='lisa')

#Lista de tareas
TAREAS = [
    # Tareas de Homero
    Tarea(nombre="ir al trabajo", estado="pendiente", descripcion="Salir para la planta nuclear a las 8:00", usuario=homero),
    Tarea(nombre="comprar donas", estado="en progreso", descripcion="Pasar por Lard Lad Donuts después del trabajo", usuario=homero),
    Tarea(nombre="ver televisión", estado="completada", descripcion="Ver su programa favorito en el sofá", usuario=homero),

    # Tareas de Bart
    Tarea(nombre="hacer travesura", estado="pendiente", descripcion="Planear una broma para Skinner", usuario=bart),
    Tarea(nombre="andar en patineta", estado="completada", descripcion="Dar una vuelta por Springfield", usuario=bart),
    Tarea(nombre="hacer la tarea", estado="en progreso", descripcion="Intentar terminar la tarea de matemáticas", usuario=bart),

    # Tareas de Lisa
    Tarea(nombre="estudiar saxofón", estado="completada", descripcion="Practicar una nueva melodía de jazz", usuario=lisa),
    Tarea(nombre="leer libro", estado="en progreso", descripcion="Leer sobre filosofía y ética", usuario=lisa),
    Tarea(nombre="proteger el medio ambiente", estado="pendiente", descripcion="Organizar campaña ecológica en la escuela", usuario=lisa)
]

@login_required
def home(request):
    mis_tareas = [tarea for tarea in TAREAS if tarea.usuario == request.user]
    return render(request, 'home.html', {"tareas": mis_tareas})

def login_view(request):
    #Revisar qué tipo de método tenemos en la petición
    if request.method == 'POST': #Significa que estamos recibiendo la información del formulario
        username = request.POST['username']
        password = request.POST['password']
        #autenticar al usuario
        usuario = authenticate(request, username=username, password=password) #usuario = None X
        if usuario is not None:
            #inicio sesión
            login(request, usuario) #Guardo en sesión la información del usuario
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request) #Función que está hecho de Modelo auth que elimina la sesión actual
    return redirect('login')

@login_required
# @permission_required('mainapp.add_tarea', raise_exception=True)
def crear(request):
    formulario = TareaForm()
    if request.method == 'POST':
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            estado = formulario.cleaned_data['estado']
            descripcion = formulario.cleaned_data['descripcion']
            
            
            nueva_tarea = Tarea(
                nombre = nombre,
                estado = estado,
                descripcion = descripcion,
                usuario = request.user
            )
            
            TAREAS.append(nueva_tarea)
            return redirect('home')
            
    return render(request, 'nuevo.html', {'formulario': formulario})
 
@login_required
# @permission_required('mainapp.change_tarea', raise_exception=True)  
def editar(request,nombre):
    try:
        tarea = [m for m in TAREAS if m.nombre==nombre][0]
        if request.method == 'POST':
            formulario = TareaForm(request.POST)
            if formulario.is_valid():
                tarea.nombre = formulario.cleaned_data['nombre']
                tarea.estado = formulario.cleaned_data['estado']
                tarea.descripcion = formulario.cleaned_data['descripcion']
                return redirect('home')
        else: 
            formulario = TareaForm(initial={"nombre": tarea.nombre, "estado": tarea.estado, "descripcion": tarea.descripcion})
        
    except IndexError:
        tarea = None
        print("La tarea no existe")      
    contexto = {"nombre": nombre, 'formulario': formulario}
    return render(request, 'editar.html', contexto)

@login_required
# @permission_required('mainapp.view_tarea', raise_exception=True) 
def detalle(request,nombre):
    try:
        tarea = [m for m in TAREAS if m.nombre==nombre][0]
        
    except IndexError:
        tarea = None
        print("La tarea no existe")      
    return render(request, 'tarea.html', {"tarea": tarea})

@login_required
# @permission_required('mainapp.delete_tarea', raise_exception=True) 
def borrar(request, nombre):
    global TAREAS
    
    TAREAS = [tarea for tarea in TAREAS if not (tarea.nombre == nombre and tarea.usuario == request.user)]
    return redirect('home')

"""

@login_required
@permission_required('mainapp.view_all_tarea', raise_exception=True) 
def todas(request):
    return render(request, 'todas.html', {'tareas': TAREAS})

"""