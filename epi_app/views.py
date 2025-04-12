from django.shortcuts import render, redirect
from epi_app.models import *

def base(request):
    return render(request, 'base.html')

def inserir_colaborador(request):
    if request.method == 'GET':
        return render(request, 'epi_app/templates/colaborador.html')
    
    cpf = request.POST.get('cpf')
    nome = request.POST.get('nome')
    setor = request.POST.get('setor')
    cargo = request.POST.get('cargo')    
    telefone = request.POST.get('telefone')
    colaborador = ColaboradorModel.objects.create(cpf=cpf, nome=nome, setor=setor, cargo=cargo, telefone=telefone, colaborador=colaborador)
    return render(request, 'app_home/templates/colaborador.html', context={'colaborador': colaborador})

def listar_colaboradores(request):
    colaboradores = ColaboradorModel.objects.all()
    return render(request, 'epi_app/templates/listar.html', context={'colaboradores': colaboradores})


def deletar_pizza(request, cpf):
    colaborador = ColaboradorModel.objects.get(cpf=cpf)
    colaborador.delete()
    return redirect('listar') 


def atualizar_colaborador(request, cpf):
    if request.method == 'GET':
        colaborador = ColaboradorModel.objects.get(cpf=cpf)
        return render(request, 'epi_app/templates/atualizar_colaborador.html', context={'colaborador': colaborador})
    
    nome = request.POST.get('nome')
    setor = request.POST.get('setor')
    cargo = request.POST.get('cargo')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    ColaboradorModel.objects.filter(cpf=cpf).update(nome=nome, setor=setor, cargo=cargo, cpf=cpf, telefone=telefone, colaborador=colaborador)
    return redirect('listar')
