from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import redirect




def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
            return redirect('/usuario/list')
        else:
            messages.error(request, form.errors)            
        form = CreateUserForm()    
    
    context = {'form': form}
    return render(request, 'cadastro.html', context)


class ListaUsuario(ListView):
    model = User
    template_name = 'list_users.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListaUsuario, self).get_queryset()
        return queryset
