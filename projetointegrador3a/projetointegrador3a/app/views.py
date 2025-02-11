"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.forms import ChamadosForm, AreaTecnicaForm, TecnicoForm, EquipamentosForm
from app.models import Chamado, AreaTecnica, Equipamento, Tecnico

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def users(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/users.html',
        {
            'title':'Usuarios',
            'message':'Listagem de Usuarios',
            'year':datetime.now().year,
        }
    )

def addusers(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/addusers.html',
        {
            'title':'Adicionar Usuario',
            'message':'Criacao de Usuario',
            'year':datetime.now().year
        }
    )

def addchamados(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    form = ChamadosForm()
    if request.method == 'POST':
       form = ChamadosForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('addchamados')

    return render(
        request,
        'app/addchamados.html',
        {
            'title':'Criar um Chamado',
            'message':'Novo Chamado',
            'year':datetime.now().year,
            'form': form
        }
    )

def chamados(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    chamados = Chamado.objects.all();
    return render(
        request,
        'app/chamados.html',
        {
            'year':datetime.now().year,
            'chamados': chamados
        }
    )

def tecnicos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    tecnicos = Tecnico.objects.all();
    return render(
        request,
        'app/tecnicos.html',
        {
            'year':datetime.now().year,
            'tecnicos': tecnicos
        }
    )

def areastecnicas(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    areastecnicas = AreaTecnica.objects.all();
    return render(
        request,
        'app/areastecnicas.html',
        {
            'year':datetime.now().year,
            'areastecnicas': areastecnicas
        }
    )

def equipamentos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    equipamentos = Equipamento.objects.all();
    return render(
        request,
        'app/equipamentos.html',
        {
            'year':datetime.now().year,
            'equipamentos': equipamentos
        }
    )

def addareatecnica(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    form = AreaTecnicaForm()
    if request.method == 'POST':
       form = AreaTecnicaForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('addareatecnica')

    return render(
        request,
        'app/addareatecnica.html',
        {
            'title':'Crição de area tecnica',
            'year':datetime.now().year,
            'form': form
        }
    ) 

def addtecnicos(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    form = TecnicoForm()
    if request.method == 'POST':
       form = TecnicoForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('addtecnicos')

    return render(
        request,
        'app/addtecnicos.html',
        {
            'title':'Criar um novo Tecnico',
            'message':'Novo Tecnico',
            'year':datetime.now().year,
            'form': form
        }
    )

def addequipamentos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    form = EquipamentosForm()

    if request.method == 'POST':
       form = EquipamentosForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('addequipamentos')      
    
    return render(
        request,
        'app/addequipamentos.html',
        {
            'title':"Adicionar Equipamento",
            'message':'Criação de um novo equipamento',
            'year':datetime.now().year,
            'form': form
            }
        )