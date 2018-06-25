from django.http import HttpResponse

from django.shortcuts import render



# Create your views here.

#def index(request):
 #   return HttpResponse("Hola")
    
def index(request):
    titulo = "Proyecto"
    
    context = {
        "titulo": titulo,
        
    }
    return render(request,"index.html", context)