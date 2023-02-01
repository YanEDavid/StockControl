from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField('Nome do Produto', max_length=50, null=False)
    descricao = models.CharField('Descrição', max_length=250)
    valor_bruto = models.DecimalField('Valor Bruto', null=False, max_digits=7, decimal_places=2)
    valor_liquido = models.DecimalField('Valor Líquido', null=False, max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(
    'Categoria',
    on_delete=models.PROTECT,
    null=False,
    blank=False
    )

    class Meta:
        ordering = ('nome_produto',)

    def __str__(self):
        return self.nome_produto
    
    def save(self, *args, **kwargs):
        super(Produto, self).save(*args, **kwargs)

class Categoria(models.Model):
    categoria = models.CharField('Categoria', null=False, max_length=128, unique=True)

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria