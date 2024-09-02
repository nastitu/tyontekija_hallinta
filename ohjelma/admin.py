from django.contrib import admin

from .models import Työntekijä, Kunta, Työpiste

# Register your models here.
class TyöntekijäAdmin(admin.ModelAdmin):
    list_display=("etunimi", "sukunimi", "työsuhteen_tyyppi")
class KuntaAdmin(admin.ModelAdmin):
    list_display=("nimi", "maakunta")
class TyöpisteAdmin(admin.ModelAdmin):
    list_display=("nimi", "kunta")

admin.site.register(Työntekijä, TyöntekijäAdmin)
admin.site.register(Kunta, KuntaAdmin)
admin.site.register(Työpiste, TyöpisteAdmin)