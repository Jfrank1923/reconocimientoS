#from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):
   
   resultado = mifuncion(request)

   
   template_name='about/about.html'
   #dict= {"nombreusuario":resultado, 'edad': 23}
   return render(request, template_name,)

def mifuncion(args):
    return 'FRANK'


  
    """
    textHtml = 
    <h1>Hola Mundo <h1>

    <ul>

        <li>Donde 
        <li>La fiesta 

    </ul>


    

    return HttpResponse(textHtml)"""