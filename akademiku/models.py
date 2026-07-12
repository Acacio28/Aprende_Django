from django.db import models
import uuid

class Turma(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    naran_turma = models.CharField(max_length=50)
    ano_letitva = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.naran_turma} ({self.ano_letitva})"

class Disciplina(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    naran_disciplina = models.CharField(max_length=100)
    docente = models.ForeignKey('docente.Docente', on_delete=models.CASCADE)

    def __str__(self):
        return self.naran_disciplina

class Avaliasaun(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    estudante = models.ForeignKey('estudante.Estudante', on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f"{self.estudante} - {self.disciplina}: {self.nota}"
