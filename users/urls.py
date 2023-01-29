from django.urls import path
from .views import registerPage

urlpatterns = [
    path('cadastro/', registerPage, name="cadastro"),
]