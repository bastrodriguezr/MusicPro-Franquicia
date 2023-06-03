from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Sesión iniciada correctamente!"))
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

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("Registro realizado correctamente!"))
            return redirect('/')
    else:
        form = CustomCreationForm()
    return render(request,'loginApp/register.html',{
        'form':form,
    })