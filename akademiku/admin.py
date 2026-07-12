from django.contrib import admin
from akademiku.models import Turma, Disciplina, Avaliasaun

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin): list_display = ('naran_turma', 'ano_letitva')
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin): list_display = ('naran_disciplina', 'docente')
@admin.register(Avaliasaun)
class AvaliasaunAdmin(admin.ModelAdmin): list_display = ('estudante', 'disciplina', 'nota')
