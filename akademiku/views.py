from django.shortcuts import render, redirect, get_object_or_404
from akademiku.models import Turma, Disciplina, Avaliasaun
from estudante.models import Estudante
from docente.models import Docente


def lista_turma(request):
    turmas = Turma.objects.all()
    return render(request, "akademiku/lista_turma.html", {"turmas": turmas})


def add_turma(request):
    if request.method == "POST":
        Turma.objects.create(
            naran_turma=request.POST["naran_turma"],
            ano_letivo=request.POST["ano_letivo"],
        )
        return redirect("lista_turma")
    return render(request, "akademiku/add_turma.html")


def edit_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    if request.method == "POST":
        turma.naran_turma = request.POST["naran_turma"]
        turma.ano_letivo = request.POST["ano_letivo"]
        turma.save()
        return redirect("lista_turma")
    return render(request, "akademiku/edit_turma.html", {"turma": turma})


def delete_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    turma.delete()
    return redirect("lista_turma")


def lista_disciplina(request):
    disciplinas = Disciplina.objects.select_related("docente").all()
    return render(request, "akademiku/lista_disciplina.html", {"disciplinas": disciplinas})


def add_disciplina(request):
    docentes = Docente.objects.all()
    if request.method == "POST":
        docente_id = request.POST.get("docente")
        Disciplina.objects.create(
            naran_disciplina=request.POST["naran_disciplina"],
            docente_id=docente_id if docente_id else None,
        )
        return redirect("lista_disciplina")
    return render(request, "akademiku/add_disciplina.html", {"docentes": docentes})


def edit_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    docentes = Docente.objects.all()
    if request.method == "POST":
        docente_id = request.POST.get("docente")
        disciplina.naran_disciplina = request.POST["naran_disciplina"]
        disciplina.docente_id = docente_id if docente_id else None
        disciplina.save()
        return redirect("lista_disciplina")
    return render(request, "akademiku/edit_disciplina.html", {"disciplina": disciplina, "docentes": docentes})


def delete_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    disciplina.delete()
    return redirect("lista_disciplina")


def lista_avaliasaun(request):
    avaliasaun = Avaliasaun.objects.select_related("estudante", "disciplina").all()
    return render(request, "akademiku/lista_avaliasaun.html", {"avaliasaun": avaliasaun})


def add_avaliasaun(request):
    estudantes = Estudante.objects.all()
    disciplinas = Disciplina.objects.all()
    if request.method == "POST":
        Avaliasaun.objects.create(
            estudante_id=request.POST["estudante"],
            disciplina_id=request.POST["disciplina"],
            nota=request.POST["nota"],
        )
        return redirect("lista_avaliasaun")
    return render(request, "akademiku/add_avaliasaun.html", {
        "estudantes": estudantes,
        "disciplinas": disciplinas,
    })


def edit_avaliasaun(request, id):
    avaliasaun = get_object_or_404(Avaliasaun, id=id)
    estudantes = Estudante.objects.all()
    disciplinas = Disciplina.objects.all()
    if request.method == "POST":
        avaliasaun.estudante_id = request.POST["estudante"]
        avaliasaun.disciplina_id = request.POST["disciplina"]
        avaliasaun.nota = request.POST["nota"]
        avaliasaun.save()
        return redirect("lista_avaliasaun")
    return render(request, "akademiku/edit_avaliasaun.html", {
        "avaliasaun": avaliasaun,
        "estudantes": estudantes,
        "disciplinas": disciplinas,
    })


def delete_avaliasaun(request, id):
    avaliasaun = get_object_or_404(Avaliasaun, id=id)
    avaliasaun.delete()
    return redirect("lista_avaliasaun")
