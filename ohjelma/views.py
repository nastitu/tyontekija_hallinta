from django.shortcuts import render, redirect
from .models import Työntekijä, Kunta, Maakunta, Työpiste
from .forms import TyöntekijäForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

#yleisnäkymä
def index(request):
    kunnat=Kunta.objects.all().order_by('nimi') #haetaan kaikki kunnat filteröintivalikkoa varten
    context={
        'kunnat':kunnat
    }
    return render(request, "index.html", context)

#uuden työntekijän lisäys
@login_required
def lisää_työntekijä(request):
    if request.method == "POST": # Kun tiedot on täytetty
        form=TyöntekijäForm(request.POST)
        if form.is_valid(): #tarkastetaan tiedot
            form.save() #tallennetaan järjestelmään
            messages.success(request, "Työntekijä tallennettu!")
            return redirect("index")
        else:
            messages.error(request, "Työntekijän tallennus epäonnistui! Kokeile uudelleen")
    else: #alussa annetaan tyhjä lomake
        form=TyöntekijäForm()

    context={
        't':None, #merkataan että työntekijä on uusi, tätä käytetään työntekijä.html:ssa päättämään ettei poista työntekijä-nappia näytetä
        'form':form,

    }
    return render(request, "tyontekija.html", context)

#Työntekijän tietojen muokkaus            
@login_required
def muokkaa_työntekijää(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk) #haetaan oikea työntekijä pääavaimen avulla
    if request.method == "POST":
        form=TyöntekijäForm(request.POST, instance=työntekijä) #kerrotaan että lomake kuuluu tietylle työntekijälle
        if form.is_valid():
            form.save()
            messages.success(request, "Työntekijä päivitetty!")
            return redirect("index")
        else:
            messages.error(request, "Työntekijän tallennus epäonnistui! Kokeile uudelleen")    
    else:
        form=TyöntekijäForm(instance=työntekijä) #annetaan alussa lomake, joka on valmiiksi täytetty työntekijän tiedoilla

    context={
        't':työntekijä, #merkataan että työntekijä on tunnettu, tätä käytetään työntekijä.html:ssa tekemään poista työntekijä-nappi
        'form':form
    }
    return render(request, "tyontekija.html", context)

#työntekijän poisto järjestelmästä
@login_required
def poista_työntekijä(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk) # haetaan työntekijä pääavaimen avulla
    if request.method == "POST": #Kun on painettu poistamisen varmistamisnappia
        työntekijä.delete() #poistetaan
        messages.success(request, "Työntekijä poistettu!") #info poistosta
        return redirect("index") #pääsivulle
    context={
        't':työntekijä
    }
    return render(request, "poista_tyontekija.html", context) 

#Kuntien haku valikkoa varten työntekijä sivulle
def lataa_kunnat(request):
    maakunta_id=request.GET.get('työmaakunta')
    kunnat=Kunta.objects.filter(maakunta_id=maakunta_id).order_by('nimi') #haetaan vain valitun maakunnan kunnat, järjestellään nimen mukaan
    context={
        'kunnat':kunnat
    }
    return render(request, 'kunta_lista.html', context)

#työpisteiden haku valikkoa varten työntekijä sivulle
def lataa_työpisteet(request):
    kunta_id=request.GET.get('työkunta')
    työpisteet=Työpiste.objects.filter(kunta_id=kunta_id).order_by('nimi') #haetaan vain valitun kunnan työpisteet, järjestellään nimen mukaan
    context={
        'tyopisteet':työpisteet
    }
    return render(request, 'tyopiste_lista.html', context)

#Työntekijöiden tietojen haku
def hae_tyontekijat(request):
    tyontekijat=Työntekijä.objects.all().values('sukunimi',
                                                'etunimi',
                                                'aloitus_pvm',
                                                'lopetus_pvm',
                                                'työsuhteen_tyyppi',
                                                'työtehtävä',
                                                'työmaakunta__nimi',
                                                'työkunta__nimi',
                                                'työpiste__nimi',
                                                'id')#haetaan työntekijöiden näytettävät tiedot(osoitetiedot jätetään hakematta)
    data=list(tyontekijat)
    return JsonResponse(data, safe=False)