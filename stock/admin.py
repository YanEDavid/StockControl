from django.contrib import admin
from stock.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_produto')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','nome_produto')