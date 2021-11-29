from django.urls import path
from .views import about

app_name = 'about'

urlpatterns = [
    path("acerca-de-mi-empresa", about, name="about")
]