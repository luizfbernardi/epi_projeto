from django.shortcuts import render, redirect
from django.contrib import messages
from epi_app.models import *
from datetime import date

def base(request):
    return render(request, 'base.html')

def inserir_colaborador(request):
    if request.method == 'GET':
        return render(request, 'pages/inserir_colaborador.html')
    
    cpf = request.POST.get('cpf')
    nome = request.POST.get('nome')
    numero_colaborador = request.POST.get('numero_colaborador')
    setor = request.POST.get('setor')
    cargo = request.POST.get('cargo')    
    telefone = request.POST.get('telefone')

    if not nome and cpf :
            messages.error(request, 'O campo nome e cpf são obrigatórios.')
            return redirect('inserir_colaborador')
    try:
            colaborador = ColaboradorModel.objects.create(cpf=cpf, nome=nome, setor=setor, numero_colaborador=numero_colaborador, cargo=cargo, telefone=telefone)
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
    numero_colaborador = request.POST.get('numero_colaborador')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    colaborador= ColaboradorModel.objects.filter(id=id).update(nome=nome, setor=setor, cargo=cargo, telefone=telefone)
    return redirect('listar_colaboradores')

def inserir_epi(request):
    if request.method == 'GET':
        return render(request, 'pages/inserir_epi.html')
    
    tipo = request.POST.get('tipo')
    numero_epi = request.POST.get('numero_epi')    

    if not tipo and n_serie :
            messages.error(request, 'O campo tipo e número série são obrigatórios.')
            return redirect('inserir_epi')
    try:
            epi = EpiModel.objects.create(tipo=tipo, numero_epi=numero_epi)
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
    numero_epi = request.POST.get('numero_epi')
    EpiModel.objects.filter(id=id).update(tipo=tipo)
    return redirect('listar_epis')

def emprestimos(request):  
    emprestimo = EmprestimoModel.objects.select_related('colaborador', 'epi').all()
    return render(request, 'pages/emprestimos.html', context={'emprestimos': emprestimo})

def inserir_emprestimo(request):
    if request.method == 'GET':
        colaboradores = ColaboradorModel.objects.all()
        epis = EpiModel.objects.all()

        return render(request, 'pages/inserir_emprestimo.html', {
            'colaboradores': colaboradores,
            'epis': epis,
            'today': date.today()
        })

    numero_emprestimo = request.POST.get('numero_emprestimo')
    numero_colaborador = request.POST.get('numero_colaborador')
    numero_epi = request.POST.get('numero_epi')
    data_prevista = request.POST.get('data_prevista')
    observacao = request.POST.get('observacao')
    status = request.POST.get('status')

    if not numero_emprestimo or not numero_colaborador or not numero_epi:
        messages.error(request, 'Os campos de identificação são obrigatórios.')
        return redirect('inserir_emprestimo')

    try:
        colaborador = ColaboradorModel.objects.get(id=numero_colaborador)
        epi = EpiModel.objects.get(id=numero_epi)
    except ColaboradorModel.DoesNotExist:
        messages.error(request, 'Colaborador não encontrado.')
        return redirect('inserir_emprestimo')
    except EpiModel.DoesNotExist:
        messages.error(request, 'EPI não encontrado.')
        return redirect('inserir_emprestimo')

    if data_prevista:
        data_prevista_obj = date.fromisoformat(data_prevista) 
        data_atual = date.today()

        if data_prevista_obj < data_atual:
            messages.error(request, 'A data prevista para devolução não pode ser anterior à data atual.')
            return redirect('inserir_emprestimo')

    try:
        EmprestimoModel.objects.create(
            numero_emprestimo=numero_emprestimo,
            colaborador=colaborador,
            epi=epi,
            data_prevista=data_prevista,
            observacao=observacao,
            status=status
        )
        messages.success(request, 'Cadastro realizado com sucesso!')
    except Exception as e:
        messages.error(request, f'Ocorreu um erro ao cadastrar: {str(e)}')

    return redirect('inserir_emprestimo')

def atualizar_emprestimo(request, id):
    if request.method == 'GET':
        emprestimo = EmprestimoModel.objects.get(id=id)
        return render(request, 'pages/atualizar_emprestimo.html', context={'emprestimo': emprestimo})
    
    data_devolucao = request.POST.get('data_devolucao')
    observacao = request.POST.get('observacao')
    data_prevista = request.POST.get('data_prevista')
    status = request.POST.get('status')

    if data_prevista:
        data_prevista_obj = date.fromisoformat(data_prevista) 
        data_atual = date.today()

    if data_prevista_obj < data_atual:
        messages.error(request, 'A data prevista para devolução não pode ser anterior à data atual.')

    EmprestimoModel.objects.filter(id=id).update(data_prevista=data_prevista, data_devolucao=data_devolucao, observacao=observacao, status=status)
    return redirect('inserir_emprestimo')
    
def controle(request):
    numero_identificacao = request.GET.get('numero_identificacao', '')
    
    if numero_identificacao:
        emprestimos = EmprestimoModel.objects.filter(
            numero_emprestimo__icontains=numero_identificacao) | EmprestimoModel.objects.filter(
            colaborador__numero_colaborador__icontains=numero_identificacao) | EmprestimoModel.objects.filter(
            epi__numero_epi__icontains=numero_identificacao)
    else:
        emprestimos = EmprestimoModel.objects.all()
    
    return render(request, 'pages/controle.html', {'emprestimos': emprestimos})
    
