from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def welcomePage(request):
    template_name = 'welcome-page.html'
    return render(request, template_name)

def homePage(request):
    template_name = 'home.html'
    return render(request, template_name)