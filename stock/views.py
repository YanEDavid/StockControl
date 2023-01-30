from django.shortcuts import render
from product import Produto
from django.views.generic import ListView
from django.db.models import Q

def lista_produto(request):
    template_name = 'lista_produto.html'
    objects = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains = search)
    context = {'object_list': objects}
    return render(request, template_name, context)

class ListaProduto(ListView):
    model = Produto
    template_name = 'lista_produto.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListaProduto, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q
                                        (produto__icontains = search) | 
                                        Q(ncm__icontains = search)
                                        )
        return queryset
