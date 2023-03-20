from django.contrib import admin
from product.models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_produto')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','nome_produto')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','categoria')