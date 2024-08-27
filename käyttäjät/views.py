from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def kirjaudu_sisään(request):
    if request.method == "POST":
        nimi=request.POST["username"]
        salasana=request.POST["password"]
        käyttäjä=authenticate(request, username=nimi, password=salasana)
        if käyttäjä is not None:
            login(request, käyttäjä)
            messages.success(request, "Olet nyt kirjautunut sisään!")
            return redirect("index")
        else:
            messages.error(request, "Kokeile uudestaan")
            return render(request, "kirjaudu.html", {})

    return render(request, "kirjaudu.html", {})

def kirjaudu_ulos(request):
    logout(request)
    messages.success(request, "Kirjauduttu ulos")
    return redirect("index")

def luo_tili(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            messages.error(request, "Kokeile uudelleen")
            
        
    else:
        form= UserCreationForm()
    
    context={
        "form":form
    }

    return render(request, "luo_tili.html", context)