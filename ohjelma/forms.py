from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, DateInput
from django.forms.utils import ErrorList
from .models import Työntekijä,Kunta,Työpiste,Maakunta

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
        elif self.instance.pk:
            self.fields['työkunta'].queryset = self.instance.maakunta.kunta_set.order_by('nimi')
        
        self.fields['työpiste'].queryset = Työpiste.objects.none() #nollataan työpiste
        if 'työkunta' in self.data:
            try:
                kunta_id = int(self.data.get('työkunta'))
                self.fields['työpiste'].queryset = Työpiste.objects.filter(kunta_id=kunta_id).order_by('nimi')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['työpiste'].queryset = self.instance.kunta.työpiste_set.order_by('nimi')

# class MaakuntaForm(forms.Form):
#     maakunta = forms.ModelChoiceField(queryset=Maakunta.objects.all(), empty_label="Valitse maakunta")

# class KuntaForm(forms.Form):
#     kunta = forms.ModelChoiceField(queryset=Kunta.objects.none(), empty_label="Valitse kunta")

# class KuntaForm(ModelForm):
#     class Meta:
#         model = Kunta
#         fields ="__all__"