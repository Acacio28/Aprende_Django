from django.db import models
import uuid

class Docente(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    nre = models.CharField(max_length=10, unique=True)
    naran_docente = models.CharField(max_length=100)
    hela_fatin = models.CharField(max_length=50, blank=True, default='')
    nu_telefone = models.CharField(max_length=15)
    sexu = models.CharField(max_length=4, choices=[("mane", "Mane"), ("feto", "Feto")])
    materia = models.CharField(max_length=100, blank=True, default='')
    data_kontratu = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.naran_docente
