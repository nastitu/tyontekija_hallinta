from django.urls import path
from . import views

app_name="käyttäjät"

urlpatterns = [
    path('kirjaudu/', views.kirjaudu_sisään, name="sisaan"),
    path('ulos/', views.kirjaudu_ulos, name="ulos"),
    path('luo_tili/', views.luo_tili, name="luo_tili"),

]
