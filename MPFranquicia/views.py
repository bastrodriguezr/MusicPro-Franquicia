from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template

#Request: para realizar peticiones.
#HttpResponse: para devolver una respuesta.
#render: para renderizar una plantilla.
#redirect: para redireccionar a una URL específica.
#reverse: para obtener la URL de un view.
# get_object_or_404: para obtener un objeto de una clase o devolver un 404.

# esto es una vista
def musicProHome(request):#pasamos un objeto de tipo request como primer parámetro
    #return HttpResponse("Hola mundo")#devolvemos un objeto de tipo HttpResponse
    return render(request, "home.html")#renderizamos la plantilla home.html
    # plantillaExterna = open("C:\Users\alicia muñoz\Desktop\Quinto Semestre\Integracion de Plataformas\MusicPro-Franquicia\MPFranquicia\templates\home.html")
    # template = Template(plantillaExterna.read())
    # plantillaExterna.close()
    # contexto = Context()
    # documento = template.render(contexto)
    # return HttpResponse(documento)

def musicProMenu(request):
    return render(request, "menu.html")
