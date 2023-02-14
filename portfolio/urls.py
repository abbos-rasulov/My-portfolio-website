from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('resume/', resume, name='resume'),
    path('works/', works, name='works'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),

]
