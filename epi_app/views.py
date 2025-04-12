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
    colaborador = ColaboradorModel.objects.create(cpf=cpf, nome=nome, setor=setor, cargo=cargo, telefone=telefone)
    return render(request, 'pages/inserir_colaborador.html', context={'colaborador': colaborador})

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
    
    epi = EpiModel.objects.create(tipo=tipo, n_serie=n_serie, status=status, estado=estado)
    return render(request, 'pages/inserir_epi.html', context={'epi': epi})

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
    nome = request.POST.get('nome')
    
    emprestimo = ColaboradorModel.objects.create(cpf=cpf, nome=nome, setor=setor, cargo=cargo, telefone=telefone)
    return render(request, 'pages/inserir_colaborador.html', context={'colaborador': colaborador})

    class EmprestimoModel(models.Model):
    id_emprestimo = models.IntegerField(primary_key=True)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_retorno = models.DateField()
    observacao = models.TextField()
    colaborador = models.ForeignKey(ColaboradorModel, on_delete=models.CASCADE)
    epi = models.ForeignKey(EpiModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Emprestimo({self.id_emprestimo}, {self.colaborador}, {self.epi})"
