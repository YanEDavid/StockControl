from django.contrib import admin
from .models import Estoque, EstoqueEntrada, EstoqueSaida, ItensEstoque

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'movimento', 'criado', 'atualizado')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','movimento', 'criado', 'atualizado')

@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    pass

@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    pass

@admin.register(ItensEstoque)
class ItensEstoqueAdmin(admin.ModelAdmin):
    pass

