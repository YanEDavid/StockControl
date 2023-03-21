from django.urls import path
from apps.product import views
from .views import ListaUsuario

urlpatterns = [
    path('list/', ListaUsuario.as_view(), name="list_users")
]