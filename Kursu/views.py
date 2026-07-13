from django.shortcuts import render
from django.db.models import Avg, Max, Min, Count
from django.apps import apps


def dashboard(request):
    context = {}
    for model_name, app in [('Estudante', 'estudante'), ('Docente', 'docente')]:
        try:
            context[f'total_{model_name.lower()}'] = apps.get_model(app, model_name).objects.count()
        except LookupError:
            context[f'total_{model_name.lower()}'] = 0
    for m in ['Turma', 'Disciplina', 'Avaliasaun']:
        try:
            context[f'total_{m.lower()}'] = apps.get_model('akademiku', m).objects.count()
        except LookupError:
            context[f'total_{m.lower()}'] = 0
    try:
        Avaliasaun = apps.get_model('akademiku', 'Avaliasaun')
        stats = Avaliasaun.objects.aggregate(Avg('nota'), Max('nota'), Min('nota'))
        context['media_geral'] = stats['nota__avg'] or 0
        context['nota_max'] = stats['nota__max'] or 0
        context['nota_min'] = stats['nota__min'] or 0
    except LookupError:
        context.update(media_geral=0, nota_max=0, nota_min=0)
    try:
        Turma = apps.get_model('akademiku', 'Turma')
        Estudante = apps.get_model('estudante', 'Estudante')
        context['turma_counts'] = Turma.objects.annotate(total=Count('estudante'))
    except LookupError:
        context['turma_counts'] = []
    return render(request, 'dashboard.html', context)


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    return render(request, 'errors/500.html', status=500)
