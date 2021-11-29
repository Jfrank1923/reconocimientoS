from django.shortcuts import render
from django.http import HttpResponse
from .models import tessiu
# Create your views here.



def micasa(request):
    Lista = tessiu.objects.get_queryset()

    L1, L2 = ProcesaLista(Lista)
    template_name='home/home.html'

    mislistas = [Lista,L1,L2]

    diccionario = {'l':Lista, "otra":"INFORMACION", "Lista1":L1, "Lista2":L2,"mislistas":mislistas}

    return render(request, template_name, diccionario)
    
    #return HttpResponse('<h1>Hola Mundo</p>')

def ProcesaLista(L):
    listaColorMayor20=[]
    listaColorMenor20=[]
    for i in L:
        if i.color > 20:
            listaColorMayor20.append(i)
            
        else:
            listaColorMenor20.append(i) 

    return listaColorMayor20, listaColorMenor20   

def procesamiento(request):
    umbral=0
    if request.method == 'GET':
        umbral=int(request.GET.get('umbral'))

   
    print('me mandaste el: ', umbral*2)
    Lista = tessiu.objects.get_queryset()
    L1,L2=ProcesaLista(Lista)
    diccionario={'l1':L1, 'l2':L2}  
    return render(request, "home/home.html",diccionario)  

   