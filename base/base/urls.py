from django.urls import path
from .views import homePage, welcomePage

urlpatterns = [
    path('home/', homePage, name="home"),
    path('welcome', welcomePage, name='welcome page')
]