from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Direccion

# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige al inicio de productos usando namespace
            return redirect("productos:inicio")
        else:
            return render(request, "sesion.html", {"error": "Usuario o contraseña incorrectos"})
    return render(request, "sesion.html")

# REGISTRO
def registro_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return render(request, "registro.html", {"error": "Las contraseñas no coinciden"})

        if User.objects.filter(username=username).exists():
            return render(request, "registro.html", {"error": "El nombre de usuario ya existe"})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        # Redirige al inicio de productos usando namespace
        return redirect("productos:inicio")

    return render(request, "registro.html")


# PERFIL
def perfil_view(request):
    if not request.user.is_authenticated:
        # Redirige al login de usuarios usando namespace
        return redirect("usuario:login")

    direcciones = Direccion.objects.filter(usuario=request.user)
    return render(request, "perfil.html", {
        "usuario": request.user,
        "direcciones": direcciones,
    })

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect("productos:inicio")  # Redirige al inicio después de cerrar sesión


# AGREGAR DIRECCIÓN
def agregar_direccion(request):
    if not request.user.is_authenticated:
        return redirect("usuarios:login")

    if request.method == "POST":
        Direccion.objects.create(
            usuario=request.user,
            direccion=request.POST["direccion"],
            ciudad=request.POST["ciudad"],
            referencia=request.POST.get("referencia", ""),
            principal=False
        )
        # Redirige al perfil de usuarios usando namespace
        return redirect("usuarios:perfil")

    return render(request, "direccion_form.html")

def eliminar_direccion(request, direccion_id):
    if not request.user.is_authenticated:
        return redirect("usuarios:login")

    direccion = get_object_or_404(Direccion, id=direccion_id, usuario=request.user)
    direccion.delete()
    return redirect("usuarios:perfil")
