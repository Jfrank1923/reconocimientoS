from django.shortcuts import render
from home.models import tessiu

# Create your views here.
import numpy as np 

def generaGrafo(request):
    Lista = tessiu.objects.get_queryset()
    calcula(Lista)
    diccionario={}
    calcula(Lista)
    return render(request, "home/home.html",diccionario)

def calcula(L):
    n=np.array([1,2,3])
    return n

