from django.urls import path
from .views import index, welcome, about

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),
    path('about/', about, name='about'),
]