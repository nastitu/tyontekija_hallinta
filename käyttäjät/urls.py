from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="käyttäjät"

urlpatterns = [
    path('kirjaudu/', views.kirjaudu_sisään, name="sisaan"),
    path('ulos/', views.kirjaudu_ulos, name="ulos"),
    path('luo_tili/', views.luo_tili, name="luo_tili"),
    path('salasana_vaihto/', views.salasana_vaihto, name="salasana_vaihto"),

]
