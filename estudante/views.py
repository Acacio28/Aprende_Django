from django.shortcuts import get_object_or_404, render,redirect
from estudante.models import Estudante


def Lista_estudante(request):
    alunos =Estudante.objects.all()
    return render(request,"estudante/Lista_Estudante.html",{"alunos":alunos})


def add_estudante(request):
    if request.method == "POST":
        nre =request.POST['nre']
        naran_estudante=request.POST['naran_estudante']
        hela_fatin=request.POST['hela_fatin']
        nu_telefone=request.POST['nu_telefone']
        sexu=request.POST['sexu']
        Estudante.objects.create(nre=nre,naran_estudante=naran_estudante,hela_fatin=hela_fatin,nu_telefone=nu_telefone,sexu=sexu)
        return redirect('lista')
    return render(request,"estudante/add_estudante.html")


def edit_estudante(request,id):
    estudante = get_object_or_404(Estudante,id=id)
    if request.method == "POST":
        estudante.nre =request.POST['nre']
        estudante.naran_estudante=request.POST['naran_estudante']
        estudante.hela_fatin=request.POST['hela_fatin']
        estudante.nu_telefone=request.POST['nu_telefone']
        estudante.sexu=request.POST['sexu']
        estudante.save()
        # return render(request,"lista")
        return redirect('lista')
    return render(request,"estudante/edit_estudante.html",{"estudante":estudante})

def delete_estudante(request,id):
    estudante = get_object_or_404(Estudante,id=id)
    estudante.delete()
    return redirect('lista')
