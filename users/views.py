from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib import messages



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
        else:
            messages.error(request, 'Ocorreu um erro!')            

        form = CreateUserForm()    
    
    context = {'form': form}
    return render(request, 'cadastro.html', context)
