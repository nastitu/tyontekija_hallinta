from django.contrib import admin

from .models import Työntekijä

# Register your models here.
class TyöntekijäAdmin(admin.ModelAdmin):
    list_display=("etunimi", "sukunimi", "työsuhteen_tyyppi")

admin.site.register(Työntekijä, TyöntekijäAdmin)