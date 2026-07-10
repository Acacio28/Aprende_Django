from django.shortcuts import get_object_or_404, render, redirect
from docente.models import Docente


def Lista_docente(request):
    docentes = Docente.objects.all()
    return render(request, "docente/Lista_Docente.html", {"docentes": docentes})


def add_docente(request):
    if request.method == "POST":
        Docente.objects.create(
            nre=request.POST['nre'],
            naran_docente=request.POST['naran_docente'],
            hela_fatin=request.POST['hela_fatin'],
            nu_telefone=request.POST['nu_telefone'],
            sexu=request.POST['sexu'],
            materia=request.POST['materia'],
            data_kontratu=request.POST.get('data_kontratu') or None,
        )
        return redirect('lista_docente')
    return render(request, "docente/add_docente.html")


def edit_docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    if request.method == "POST":
        docente.nre = request.POST['nre']
        docente.naran_docente = request.POST['naran_docente']
        docente.hela_fatin = request.POST['hela_fatin']
        docente.nu_telefone = request.POST['nu_telefone']
        docente.sexu = request.POST['sexu']
        docente.materia = request.POST['materia']
        docente.data_kontratu = request.POST.get('data_kontratu') or None
        docente.save()
        return redirect('lista_docente')
    return render(request, "docente/edit_docente.html", {"docente": docente})


def delete_docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    docente.delete()
    return redirect('lista_docente')
