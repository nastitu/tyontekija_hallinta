from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def lisää_työntekijä(request):
    pass

def poista_työntekijä(request, pk):
    pass

def muokkaa_työntekijän_tietoja(request, pk):
    pass