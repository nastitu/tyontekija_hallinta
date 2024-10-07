from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, DateInput
from django.forms.utils import ErrorList
from .models import Työntekijä,Kunta,Työpiste,Maakunta
from django.core.exceptions import ValidationError

class TyöntekijäForm(ModelForm):
    class Meta:
        model = Työntekijä
        fields ="__all__"
        widgets ={
            'aloitus_pvm': DateInput(attrs={"type": "date"}),
            'lopetus_pvm': DateInput(attrs={"type": "date"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['työkunta'].queryset = Kunta.objects.none() #nollataan kunta
        if 'työmaakunta' in self.data:
            try:
                maakunta_id = int(self.data.get('työmaakunta'))
                self.fields['työkunta'].queryset = Kunta.objects.filter(maakunta_id=maakunta_id).order_by('nimi') 
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk: #kun työntekijä tiedossa
            try:
                self.fields['työkunta'].queryset = self.instance.työmaakunta.kunta_set.order_by('nimi')
            except (AttributeError): #tämä koska ei tykkää null arvoista työmaakunnassa ja työkunnassa
                pass 
        self.fields['työpiste'].queryset = Työpiste.objects.none() #nollataan työpiste
        if 'työkunta' in self.data:
            try:
                kunta_id = int(self.data.get('työkunta'))
                self.fields['työpiste'].queryset = Työpiste.objects.filter(kunta_id=kunta_id).order_by('nimi')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk: #kun työntekijä tiedossa
            try:
                self.fields['työpiste'].queryset = self.instance.työkunta.työpiste_set.order_by('nimi')
            except (AttributeError):   #tämä koska ei tykkää null arvoista työkunnassa ja työpisteessä
                pass 
    

    def clean(self): #Tarkastetaan että lopetus on aloituksen jälkeen
        puhdistettu_data =super().clean()
        aloitus=puhdistettu_data.get("aloitus_pvm")
        lopetus=puhdistettu_data.get("lopetus_pvm")

        if lopetus is not None: #jos lopetus tyhjä niin se on joskus tulevaisuudessa
            if lopetus < aloitus:
                raise ValidationError("Lopetuksen täytyy olla aloituksen jälkeen")




