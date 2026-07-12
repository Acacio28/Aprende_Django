from django.shortcuts import render
from django.db.models import Count
from django.apps import apps

def dashboard(request):
    context = {}
    try:
        Estudante = apps.get_model('estudante', 'Estudante')
        context['total_estudante'] = Estudante.objects.count()
    except LookupError:
        context['total_estudante'] = 0
    try:
        Docente = apps.get_model('docente', 'Docente')
        context['total_docente'] = Docente.objects.count()
    except LookupError:
        context['total_docente'] = 0
    for m in ['Turma', 'Disciplina', 'Avaliasaun']:
        try:
            context[f'total_{m.lower()}'] = apps.get_model('akademiku', m).objects.count()
        except LookupError:
            context[f'total_{m.lower()}'] = 0
    return render(request, 'dashboard.html', context)
