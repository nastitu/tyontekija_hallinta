from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('tyontekija/', views.lisää_työntekijä, name="lisaa_t"),
    path('poista_t/<int:pk>', views.poista_työntekijä, name="poista_t"),
    path('tyontekija/<int:pk>', views.muokkaa_työntekijää, name="muokkaa_t"),
    path('lataa_kunnat', views.lataa_kunnat, name='lataa_kunnat'),
    path('lataa_tyopisteet', views.lataa_työpisteet, name='lataa_tyopisteet'),

]
