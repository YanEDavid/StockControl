from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField('Nome do Produto', max_length=50, null=False)
    descricao = models.CharField('Descrição', max_length=250)
    quantidade = models.IntegerField('Quantidade', null=False, default=0)
    valor_bruto = models.FloatField('Valor Bruto', null=False)
    valor_liquido = models.FloatField('Valor Líquido', null=False)

    def __str__(self):
        return self.nome_produto
    
    def save(self, *args, **kwargs):
        super(Produto, self).save(*args, **kwargs)
