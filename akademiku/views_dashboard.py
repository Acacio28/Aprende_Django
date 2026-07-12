from django.shortcuts import render
from akademiku.models import Turma, Disciplina, Avaliasaun


def dashboard_akademiku(request):
    return render(request, "akademiku/dashboard.html", {
        "total_turma": Turma.objects.count(),
        "total_disciplina": Disciplina.objects.count(),
        "total_avaliasaun": Avaliasaun.objects.count(),
    })
