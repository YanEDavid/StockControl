from django import forms
from apps.product.models import Produto
from .models import Estoque, EstoqueItens

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque 
        fields = ('nf',)

class EstoqueItensEntradaForm(forms.ModelForm):
    class Meta:
        model = EstoqueItens
        fields = '__all__'

class EstoqueItensSaidaForm(forms.ModelForm):
    class Meta:
        model = EstoqueItens
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EstoqueItensSaidaForm, self).__init__(*args, **kwargs)

        self.fields['product'].queryset = Produto.objects.filter(estoque__gt=0)