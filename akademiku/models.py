from django.db import models
import uuid
from docente.models import Docente
from estudante.models import Estudante


class Turma(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    naran_turma = models.CharField(max_length=50, unique=True)
    ano_letivo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.naran_turma} ({self.ano_letivo})"


class Disciplina(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    naran_disciplina = models.CharField(max_length=100, unique=True)
    docente = models.ForeignKey(
        Docente, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="disciplinas"
    )

    def __str__(self):
        return self.naran_disciplina


class Avaliasaun(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    estudante = models.ForeignKey(
        Estudante, on_delete=models.CASCADE, related_name="avaliasaun"
    )
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, related_name="avaliasaun"
    )
    nota = models.DecimalField(max_digits=4, decimal_places=1)
    data = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("estudante", "disciplina", "data")
        verbose_name = "Avaliasaun"
        verbose_name_plural = "Avaliasaun"

    def __str__(self):
        return f"{self.estudante.naran_estudante} - {self.disciplina.naran_disciplina}: {self.nota}"
