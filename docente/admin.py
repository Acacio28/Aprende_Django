from django.contrib import admin
from docente.models import Docente


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nre', 'naran_docente', 'hela_fatin', 'nu_telefone', 'sexu', 'materia', 'data_kontratu')
    search_fields = ('nre', 'naran_docente', 'materia')
    list_filter = ('sexu', 'materia')