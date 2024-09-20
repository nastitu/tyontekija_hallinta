from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('tyontekija/', views.lisää_työntekijä, name="lisaa_t"),
    path('poista_t/<int:pk>', views.poista_työntekijä, name="poista_t"),
    path('tyontekija/<int:pk>', views.muokkaa_työntekijää, name="muokkaa_t"),
    path('lataa_kunnat', views.lataa_kunnat, name='lataa_kunnat'),
    path('lataa_tyopisteet', views.lataa_työpisteet, name='lataa_tyopisteet'),
    path('lataa_kaikki_kunnat', views.lataa_kaikki_kunnat, name='lataa_kaikki_kunnat'),
    path('hae_t', views.hae_tyontekijat, name="hae_t"),
]
