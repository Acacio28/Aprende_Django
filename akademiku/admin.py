from django.contrib import admin
from akademiku.models import Turma, Disciplina, Avaliasaun


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('naran_turma', 'ano_letivo')
    search_fields = ('naran_turma',)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('naran_disciplina', 'docente')
    search_fields = ('naran_disciplina',)
    list_filter = ('docente',)


@admin.register(Avaliasaun)
class AvaliasaunAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'disciplina', 'nota', 'data')
    list_filter = ('disciplina', 'data')
