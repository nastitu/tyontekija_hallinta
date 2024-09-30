from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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

@login_required
def salasana_vaihto(request):
    if request.method == "POST":
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Salasanan vaihto onnistui")
            return redirect("index")
        else:
            messages.error(request, "kokeile uudelleen")
    else:
        form=PasswordChangeForm(request.POST)

    context={
        "form":form
    }

    return render(request, "vaihda_salasana.html", context)