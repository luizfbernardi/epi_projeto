from django.shortcuts import render, redirect
from django.contrib import messages
from epi_app.models import *

def base(request):
    return render(request, 'base.html')

def inserir_colaborador(request):
    if request.method == 'GET':
        return render(request, 'pages/inserir_colaborador.html')
    
    cpf = request.POST.get('cpf')
    nome = request.POST.get('nome')
    setor = request.POST.get('setor')
    cargo = request.POST.get('cargo')    
    telefone = request.POST.get('telefone')

    if not nome and cpf :
            messages.error(request, 'O campo nome e cpf são obrigatórios.')
            return redirect('inserir_colaborador')
    try:
            colaborador = ColaboradorModel.objects.create(cpf=cpf, nome=nome, setor=setor, cargo=cargo, telefone=telefone)
            messages.success(request, 'Cadastro realizado com sucesso!')
    except Exception as e:
            messages.error(request, f'Ocorreu um erro ao cadastrar: {str(e)}')
    
    return redirect('inserir_colaborador') 


def listar_colaboradores(request):
    colaboradores = ColaboradorModel.objects.all()
    return render(request, 'pages/listar_colaboradores.html', context={'colaboradores': colaboradores})


def excluir_colaborador(request, id):
    colaborador = ColaboradorModel.objects.get(id=id)
    colaborador.delete()
    return redirect('listar_colaboradores') 


def atualizar_colaborador(request, id):
    if request.method == 'GET':
        colaborador = ColaboradorModel.objects.get(id=id)
        return render(request, 'pages/atualizar_colaborador.html', context={'colaborador': colaborador})
    
    nome = request.POST.get('nome')
    setor = request.POST.get('setor')
    cargo = request.POST.get('cargo')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    ColaboradorModel.objects.filter(cpf=cpf).update(nome=nome, setor=setor, cargo=cargo, cpf=cpf, telefone=telefone)
    return redirect('listar_colaboradores')

def inserir_epi(request):
    if request.method == 'GET':
        return render(request, 'pages/inserir_epi.html')
    
    tipo = request.POST.get('tipo')
    n_serie = request.POST.get('n_serie')
    status = request.POST.get('status')
    estado = request.POST.get('estado')    

    if not tipo and n_serie :
            messages.error(request, 'O campo tipo e número série são obrigatórios.')
            return redirect('inserir_epi')
    try:
            epi = EpiModel.objects.create(tipo=tipo, n_serie=n_serie, status=status, estado=estado)
            messages.success(request, 'Cadastro realizado com sucesso!')
    except Exception as e:
            messages.error(request, f'Ocorreu um erro ao cadastrar: {str(e)}')
    
    return redirect('inserir_epi') 
    

def listar_epis(request):
    epis = EpiModel.objects.all()
    return render(request, 'pages/listar_epis.html', context={'epis': epis})

def excluir_epi(request, id):
    epi = EpiModel.objects.get(id=id)
    epi.delete()
    return redirect('listar_epis')

def atualizar_epi(request, id):
    if request.method == 'GET':
        epi = EpiModel.objects.get(id=id)
        return render(request, 'pages/atualizar_epi.html', context={'epi': epi})
    
    tipo = request.POST.get('tipo')
    n_serie = request.POST.get('n_serie')
    status = request.POST.get('status')
    estado = request.POST.get('estado')
    EpiModel.objects.filter(id=id).update(tipo=tipo, n_serie=n_serie, status=status, estado=estado)
    return redirect('listar_epis')

def inserir_emprestimo(request):
    if request.method == 'GET':
        return render(request, 'pages/inserir_emprestimo.html')
    
    cpf = request.POST.get('cpf')
    n_serie = request.POST.get('n_serie')

    
    emprestimo = ColaboradorModel.objects.create(cpf=cpf, n_serie=n_serie, )
    return render(request, 'pages/inserir_emprestimo.html', context={'emprestimo': emprestimo})
