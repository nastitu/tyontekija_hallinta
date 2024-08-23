from django.shortcuts import render, redirect
from .models import Työntekijä
from .forms import TyöntekijäForm
from django.contrib import messages

# Create your views here.

def index(request):
    työntekijät=Työntekijä.objects.all()

    context={
        'tyontekijat':työntekijät
    }
    return render(request, "index.html", context)

def lisää_työntekijä(request):
    if request.method == "POST":
        form=TyöntekijäForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Työntekijä tallennettu!")
            return redirect("/")
    form=TyöntekijäForm()
    context={
        'form':form
    }
    return render(request, "tyontekija.html", context)

def poista_työntekijä(request, pk):
    työntekijä=Työntekijä.objects.get(pk=pk)
    context={
        't':työntekijä
    }
    return render(request, "poista_t.html", context)

def muokkaa_työntekijää(request, pk):


    # if request.method == "POST":
    #     form=TyöntekijäForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Työntekijä tallennettu!")
    #         return redirect("/")
            
    työntekijä=Työntekijä.objects.get(pk=pk)
    form=TyöntekijäForm(instance=työntekijä)

    context={
        't':työntekijä,
        'form':form
    }
    return render(request, "tyontekija.html", context)