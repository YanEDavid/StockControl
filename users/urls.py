from django.urls import path, include
from .views import registerPage, ListaUsuario

urlpatterns = [
    path('usuario/cadastro/', registerPage, name="cadastro"),
    path('usuario/list/', ListaUsuario.as_view(), name="list_users"),
    path('usuario/', include("django.contrib.auth.urls"), name="login"),
]