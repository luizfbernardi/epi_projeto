from django.db import models

# Create your models here.

class ColaboradorModel(models.Model):
    cpf = models.CharField(max_length=14, null=False)
    nome = models.CharField(max_length=100, null=False)
    setor = models.CharField(max_length=45, null=False)
    cargo = models.CharField(max_length=45)    
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return f"Colaborador({self.cpf}, {self.nome}, {self.setor}, {self.cargo})"

class EpiModel(models.Model):
    #id_epi = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100, null=False)
    n_serie = models.CharField(null=False)
    status = models.CharField(max_length=30, null=False)
    estado = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"Epi({self.id_epi}, {self.tipo}, {self.n_serie})"

class EmprestimoModel(models.Model):
    #id_emprestimo = models.IntegerField(primary_key=True)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_retorno = models.DateField()
    observacao = models.TextField()
    colaborador = models.ForeignKey(ColaboradorModel, on_delete=models.CASCADE)
    epi = models.ForeignKey(EpiModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Emprestimo({self.id_emprestimo}, {self.colaborador}, {self.epi})"