from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from docente.models import Docente


def Lista_docente(request):
    q = request.GET.get('q', '')
    docentes = Docente.objects.all()
    if q:
        docentes = docentes.filter(naran_docente__icontains=q)
    return render(request, "docente/Lista_Docente.html", {"docentes": docentes, "q": q})


def add_docente(request):
    if request.method == "POST":
        Docente.objects.create(
            nre=request.POST['nre'], naran_docente=request.POST['naran_docente'],
            hela_fatin=request.POST['hela_fatin'], nu_telefone=request.POST['nu_telefone'],
            sexu=request.POST['sexu'], materia=request.POST['materia'],
            data_kontratu=request.POST.get('data_kontratu') or None,
        )
        messages.success(request, "Docente aumenta ho sucesso!")
        return redirect('lista_docente')
    return render(request, "docente/add_docente.html")


def edit_docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    if request.method == "POST":
        for f in ['nre', 'naran_docente', 'hela_fatin', 'nu_telefone', 'sexu', 'materia']:
            setattr(docente, f, request.POST[f])
        docente.data_kontratu = request.POST.get('data_kontratu') or None
        docente.save()
        messages.success(request, "Docente hadia ho sucesso!")
        return redirect('lista_docente')
    return render(request, "docente/edit_docente.html", {"docente": docente})


def delete_docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    docente.delete()
    messages.success(request, "Docente apaga ho sucesso!")
    return redirect('lista_docente')
