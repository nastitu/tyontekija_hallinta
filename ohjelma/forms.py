from django.forms import ModelForm, DateInput
from .models import Työntekijä

class TyöntekijäForm(ModelForm):
    class Meta:
        model = Työntekijä
        fields ="__all__"
        widgets ={
            'aloitus_pvm': DateInput(attrs={"type": "date"}),
            'lopetus_pvm': DateInput(attrs={"type": "date"}),
        }


# class MaakuntaForm(forms.Form):
#     maakunta = forms.ModelChoiceField(queryset=Maakunta.objects.all(), empty_label="Valitse maakunta")

# class KuntaForm(forms.Form):
#     kunta = forms.ModelChoiceField(queryset=Kunta.objects.none(), empty_label="Valitse kunta")

# class KuntaForm(ModelForm):
#     class Meta:
#         model = Kunta
#         fields ="__all__"