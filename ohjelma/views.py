from django.shortcuts import render, redirect
from .models import Työntekijä, Kunta, Maakunta, Työpiste
from .forms import TyöntekijäForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

def index(request):
    työntekijät=Työntekijä.objects.all()

    context={
        'tyontekijat':työntekijät
    }
    return render(request, "index.html", context)

@login_required
def lisää_työntekijä(request):
    if request.method == "POST":
        form=TyöntekijäForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Työntekijä tallennettu!")
            return redirect("index")
        else:
            messages.error(request, "Työntekijän tallennus epäonnistui! Kokeile uudelleen")
    else:
        form=TyöntekijäForm()

    context={
        't':None,
        'form':form,

    }
    return render(request, "tyontekija.html", context)

            
@login_required
def muokkaa_työntekijää(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk)

    if request.method == "POST":
        form=TyöntekijäForm(request.POST, instance=työntekijä)
        if form.is_valid():
            form.save()
            messages.success(request, "Työntekijä päivitetty!")
            return redirect("index")
        else:
            messages.error(request, "Työntekijän tallennus epäonnistui! Kokeile uudelleen")    
    else:
        form=TyöntekijäForm(instance=työntekijä)

    context={
        't':työntekijä,
        'form':form
    }
    return render(request, "tyontekija.html", context)

@login_required
def poista_työntekijä(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk)
    työntekijä.delete()
    messages.success(request, "Työntekijä poistettu!")
    return redirect("index")

def lataa_kunnat(request):
    maakunta_id=request.GET.get('työmaakunta')
    kunnat=Kunta.objects.filter(maakunta_id=maakunta_id).order_by('nimi')
    context={
        'kunnat':kunnat
    }
    return render(request, 'kunta_lista.html', context)

def lataa_kaikki_kunnat(request):
    kunnat=Kunta.objects.all().order_by('nimi')
    context={
        'kunnat':kunnat
    }
    return render(request, 'k_kunta_lista.html', context)

def lataa_työpisteet(request):
    kunta_id=request.GET.get('työkunta')
    työpisteet=Työpiste.objects.filter(kunta_id=kunta_id).order_by('nimi')
    context={
        'tyopisteet':työpisteet
    }
    return render(request, 'tyopiste_lista.html', context)

def hae_tyontekijat(request):
    tyontekijat=Työntekijä.objects.all().values('sukunimi',
                                                'etunimi',
                                                'aloitus_pvm',
                                                'lopetus_pvm',
                                                'työsuhteen_tyyppi',
                                                'työtehtävä',
                                                'työkunta__nimi',
                                                'työpiste__nimi',
                                                'id')
    data=list(tyontekijat)
    #print(data)
    #print (JsonResponse(data,safe=False))
    return JsonResponse(data, safe=False)