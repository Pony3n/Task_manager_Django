from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about-us', about_us, name='about'),
    path('create', create_task, name='create')
]