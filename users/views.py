from django.shortcuts import render
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = CreateUserForm()
    context = {'form': form}

    return render(request, 'cadastro.html', context)
