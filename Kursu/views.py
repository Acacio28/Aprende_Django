from django.shortcuts import render
from estudante.models import Estudante
from docente.models import Docente


def dashboard(request):
    return render(request, "dashboard.html", {
        "total_estudante": Estudante.objects.count(),
        "total_docente": Docente.objects.count(),
    })
