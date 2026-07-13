from django.shortcuts import get_object_or_404, render, redirect
from estudante.models import Estudante
from akademiku.models import Turma


def Lista_estudante(request):
    q = request.GET.get('q', '')
    alunos = Estudante.objects.select_related('turma').all()
    if q:
        alunos = alunos.filter(naran_estudante__icontains=q)
    return render(request, "estudante/Lista_Estudante.html", {"alunos": alunos, "q": q})


def add_estudante(request):
    if request.method == "POST":
        turma_id = request.POST.get('turma') or None
        Estudante.objects.create(
            nre=request.POST['nre'],
            naran_estudante=request.POST['naran_estudante'],
            hela_fatin=request.POST['hela_fatin'],
            nu_telefone=request.POST['nu_telefone'],
            sexu=request.POST['sexu'],
            turma_id=turma_id,
        )
        return redirect('lista')
    turmas = Turma.objects.all()
    return render(request, "estudante/add_estudante.html", {"turmas": turmas})


def edit_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    if request.method == "POST":
        estudante.nre = request.POST['nre']
        estudante.naran_estudante = request.POST['naran_estudante']
        estudante.hela_fatin = request.POST['hela_fatin']
        estudante.nu_telefone = request.POST['nu_telefone']
        estudante.sexu = request.POST['sexu']
        estudante.turma_id = request.POST.get('turma') or None
        estudante.save()
        return redirect('lista')
    turmas = Turma.objects.all()
    return render(request, "estudante/edit_estudante.html", {"estudante": estudante, "turmas": turmas})


def delete_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    estudante.delete()
    return redirect('lista')
