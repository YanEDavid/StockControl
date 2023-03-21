from django.shortcuts import render
from apps.product.models import Produto
from django.views.generic import ListView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def lista_produto(request):
    template_name = 'lista_produto.html'
    produto = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        produto = produto.filter(produto__icontains = search)
    context = {'lista_produto': produto}
    return render(request, template_name, context)

class ListaProduto(ListView):
    model = Produto
    template_name = 'lista_produto.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListaProduto, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(produto__icontains = search))
        return queryset

@method_decorator(login_required, name='dispatch')
class ListaUsuario(ListView):
    model = User
    template_name = 'list_users.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListaUsuario, self).get_queryset()
        return queryset