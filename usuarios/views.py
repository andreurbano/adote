from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def cadastro(request):
#    return HttpResponse('Olá estou no cadastro!')
    return render(request, 'cadastro.html')