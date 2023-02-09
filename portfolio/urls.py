from django.urls import path
from .views import index, welcome, about, services

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
]