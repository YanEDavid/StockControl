from django.db import models
from django.contrib.auth.models import User
from .managers import EstoqueEntradaManager, EstoqueSaidaManager
from product.models import Produto

MOVIMENTO = (
    ('E', 'Entrada'),
    ('S', 'Saida'),
)

class Estoque(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    nf = models.PositiveIntegerField('Nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)
    frete = models.PositiveIntegerField(null=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-criado',)

    def __str__(self):
        if self.nf:
            return f'{self.pk} - {self.nf}'
        return f'{self.pk}'

    def nf_format(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '--'
    
class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        verbose_name = 'Estoque Entrada'
        verbose_name_plural = 'Estoque Entrada'
        proxy = True

class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()

    class Meta:
        verbose_name = 'Estoque Saida'
        verbose_name_plural = 'Estoque Saida'
        proxy = True

class ItensEstoque(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank = True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.produto}'
