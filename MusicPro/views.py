from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def carrito(request):
    return render(request, 'carrito.html')


def saludo(request):
    url = 'http://musicpro.bemtorres.win/api/v1/test/saldo'
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        
    except request.exceptions.RequestException as e:
        print(f'Error: {e}')

    return HttpResponse(data['message'])