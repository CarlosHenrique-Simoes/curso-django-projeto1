from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Carlos Simões'
    })


def contato(request):
    return render(request, 'recipes/contato.html')
