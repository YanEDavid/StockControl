from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProdutoList.as_view(), name='lista_produto')
]