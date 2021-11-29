
from django.urls import path
from .views import principal

app_name = 'sintactico'

urlpatterns = [
    path("sintatico-estructural-patrones/", principal, name="patrones"),
    path("about/", principal, name="about"),
    path("grafos/", principal, name="grafos"),
    path("home/", principal, name="home"),
]