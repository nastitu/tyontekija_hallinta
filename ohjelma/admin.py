from django.contrib import admin

from .models import Työntekijä, Kunta, Työpiste, Maakunta
# Register your models here.
class TyöntekijäAdmin(admin.ModelAdmin):
    list_display=("etunimi", "sukunimi", "työsuhteen_tyyppi")
class KuntaAdmin(admin.ModelAdmin):
    list_display=("nimi", "maakunta")
class MaakuntaAdmin(admin.ModelAdmin):
    list_display=("nimi", )
class TyöpisteAdmin(admin.ModelAdmin):
     list_display=("nimi", "kunta")

admin.site.register(Työntekijä, TyöntekijäAdmin)
admin.site.register(Kunta, KuntaAdmin)
admin.site.register(Maakunta, MaakuntaAdmin)
admin.site.register(Työpiste, TyöpisteAdmin)