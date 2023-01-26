from django.db import models
from django.contrib.auth.models import User

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(models.Model):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('funcionario',)
