
from django.urls.conf import path
from .views import micasa
from . import views

urlpatterns = [
    path('',views.micasa, name ='home'),
    path('procesamiento/',views.procesamiento, name='proc'), 
]