from django.urls import path
from .views import registerPage
from users import views

urlpatterns = [
    path('usuario/cadastro/', registerPage, name="cadastro"),
    path('usuario/list/', views.ListaUsuario.as_view(), name="list_users"),
]