from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, ("Error al iniciar sesión, intente nuevamente..."))
            return redirect('login')
    else:
        return render(request,'loginApp/login.html')

def logout_user(request):
    logout(request)
    messages.warning(request, ("Sesión cerrada correctamente"))
    return redirect('/')