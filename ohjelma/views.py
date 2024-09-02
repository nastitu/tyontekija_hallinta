from django.shortcuts import render, redirect
from .models import Työntekijä
from .forms import TyöntekijäForm, KuntaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        kuntaform=KuntaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Työntekijä tallennettu!")
            return redirect("index")
    form=TyöntekijäForm()
    kuntaform=KuntaForm()
    context={
        't':None,
        'form':form,
        'kuntaform': kuntaform
    }
    return render(request, "tyontekija.html", context)

@login_required
def poista_työntekijä(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk)
    työntekijä.delete()
    messages.success(request, "Työntekijä poistettu!")
    return redirect("index")
            
@login_required
def muokkaa_työntekijää(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk)

    if request.method == "POST":
        form=TyöntekijäForm(request.POST, instance=työntekijä)
        if form.is_valid():
            form.save()
            messages.success(request, "Työntekijä päivitetty!")
            return redirect("index")
            
    
    form=TyöntekijäForm(instance=työntekijä)

    context={
        't':työntekijä,
        'form':form
    }
    return render(request, "tyontekija.html", context)

