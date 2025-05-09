from django.db import models

# Create your models here.

class ColaboradorModel(models.Model):
    cpf = models.CharField(max_length=14, null=False)
    nome = models.CharField(max_length=100, null=False)
    numero_colaborador = models.IntegerField(null=False)
    setor = models.CharField(max_length=45, null=False)
    cargo = models.CharField(max_length=45)    
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return f"Colaborador({self.cpf}, {self.nome}, {self.numero_colaborador}, {self.setor}, {self.cargo})"

class EpiModel(models.Model):
    tipo = models.CharField(max_length=100, null=False)
    numero_epi = models.IntegerField(null=False)

    def __str__(self):
        return f"Epi({self.tipo}, {self.numero_epi})"

class EmprestimoModel(models.Model):

    numero_emprestimo = models.IntegerField(null=False)

    colaborador = models.ForeignKey(ColaboradorModel, on_delete=models.CASCADE)
    epi = models.ForeignKey(EpiModel, on_delete=models.CASCADE)

    data_emprestimo = models.DateField(auto_now_add=True)
    data_prevista = models.DateField(blank=True)
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(null=False)

    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"Emprestimo({self.numero_emprestimo}, {self.observacao}, {self.status}, {self.colaborador}, {self.data_devolucao}, {self.data_prevista}, {self.epi}, {self.data_emprestimo})"