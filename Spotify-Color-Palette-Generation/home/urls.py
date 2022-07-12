import imp
from lib2to3.pytree import Base
from django.urls import path

from .views import home, simple_function

urlpatterns = [
    path('', home, name='home'),
    path("simple_function", simple_function)    
]