from django.forms import ModelForm, DateInput
from .models import Työntekijä

class TyöntekijäForm(ModelForm):
    class Meta:
        model = Työntekijä
        fields = "__all__"
        widgets ={
            'aloitus_pvm': DateInput(attrs={"type": "date"}),
            'lopetus_pvm': DateInput(attrs={"type": "date"}),
        }

    