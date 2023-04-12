

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import contato


# Create your views here.
def index(request):
        return render(request, 'graosdaterra/index.html')

def contatos(request):
        novo_contato = contato()
        novo_contato.nome = request.POST.get('nome')
        novo_contato.telefone = request.POST.get('telefone')
        novo_contato.save()

        contatos= {
                'contatos': contato.objects.all()
        }
        return render(request,  "graosdaterra/contatos.html", contatos)

def historia(request):
        return render(request, 'graosdaterra/historia.html')

def deletecontatos(request, id):
        contato.delete()
