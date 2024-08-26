from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('tyontekija/', views.lisää_työntekijä, name="lisaa_t"),
    path('poista_t/<int:pk>', views.poista_työntekijä, name="poista_t"),
    path('tyontekija/<int:pk>', views.muokkaa_työntekijää, name="muokkaa_t"),
    path('kirjaudu/', views.kirjaudu_sisään, name="sisaan"),
    path('ulos/', views.kirjaudu_ulos, name="ulos"),
]
