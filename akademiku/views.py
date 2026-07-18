from django.shortcuts import get_object_or_404, render, redirect
from akademiku.models import Turma, Disciplina, Avaliasaun
from django.db.models import Q

def Lista_turma(request):
    q = request.GET.get('q', '')
    turmas = Turma.objects.all()
    if q:
        turmas = turmas.filter(Q(naran_turma__icontains=q) | Q(ano_letitva__icontains=q))
    return render(request, "akademiku/Lista_turma.html", {"turmas": turmas, "q": q})

def add_turma(request):
    if request.method == "POST":
        Turma.objects.create(naran_turma=request.POST['naran_turma'], ano_letitva=request.POST['ano_letitva'])
        return redirect('lista_turma')
    return render(request, "akademiku/add_turma.html")

def edit_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    if request.method == "POST":
        turma.naran_turma, turma.ano_letitva = request.POST['naran_turma'], request.POST['ano_letitva']
        turma.save(); return redirect('lista_turma')
    return render(request, "akademiku/edit_turma.html", {"turma": turma})

def delete_turma(request, id):
    get_object_or_404(Turma, id=id).delete(); return redirect('lista_turma')

def Lista_disciplina(request):
    q = request.GET.get('q', '')
    disciplinas = Disciplina.objects.select_related('docente').all()
    if q:
        disciplinas = disciplinas.filter(Q(naran_disciplina__icontains=q) | Q(docente__naran_docente__icontains=q))
    return render(request, "akademiku/Lista_disciplina.html", {"disciplinas": disciplinas, "q": q})

def add_disciplina(request):
    if request.method == "POST":
        Disciplina.objects.create(naran_disciplina=request.POST['naran_disciplina'], docente_id=request.POST['docente'])
        return redirect('lista_disciplina')
    from docente.models import Docente
    return render(request, "akademiku/add_disciplina.html", {"docentes": Docente.objects.all()})

def edit_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    if request.method == "POST":
        disciplina.naran_disciplina, disciplina.docente_id = request.POST['naran_disciplina'], request.POST['docente']
        disciplina.save(); return redirect('lista_disciplina')
    from docente.models import Docente
    return render(request, "akademiku/edit_disciplina.html", {"disciplina": disciplina, "docentes": Docente.objects.all()})

def delete_disciplina(request, id):
    get_object_or_404(Disciplina, id=id).delete(); return redirect('lista_disciplina')

def Lista_avaliasaun(request):
    q = request.GET.get('q', '')
    avaliasauns = Avaliasaun.objects.select_related('estudante', 'disciplina').all()
    if q:
        avaliasauns = avaliasauns.filter(Q(estudante__naran_estudante__icontains=q) | Q(disciplina__naran_disciplina__icontains=q))
    return render(request, "akademiku/Lista_avaliasaun.html", {"avaliasauns": avaliasauns, "q": q})

def add_avaliasaun(request):
    if request.method == "POST":
        Avaliasaun.objects.create(estudante_id=request.POST['estudante'], disciplina_id=request.POST['disciplina'], nota=request.POST['nota'])
        return redirect('lista_avaliasaun')
    from estudante.models import Estudante
    return render(request, "akademiku/add_avaliasaun.html", {"estudantes": Estudante.objects.all(), "disciplinas": Disciplina.objects.all()})

def edit_avaliasaun(request, id):
    avaliasaun = get_object_or_404(Avaliasaun, id=id)
    if request.method == "POST":
        avaliasaun.estudante_id, avaliasaun.disciplina_id, avaliasaun.nota = request.POST['estudante'], request.POST['disciplina'], request.POST['nota']
        avaliasaun.save(); return redirect('lista_avaliasaun')
    from estudante.models import Estudante
    return render(request, "akademiku/edit_avaliasaun.html", {"avaliasaun": avaliasaun, "estudantes": Estudante.objects.all(), "disciplinas": Disciplina.objects.all()})

def delete_avaliasaun(request, id):
    get_object_or_404(Avaliasaun, id=id).delete(); return redirect('lista_avaliasaun')
