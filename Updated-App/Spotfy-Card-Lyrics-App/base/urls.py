import imp
from lib2to3.pytree import Base
from django.urls import path

from .views import home, simple_function, debug, url

urlpatterns = [
    path('', home, name='home'),
    path('debug', debug, name='debug'),
    path("simple_function", simple_function),
    path('url', url, name='url')
]