from django.forms import ModelForm
from .models import Työntekijä

class TyöntekijäForm(ModelForm):
    class Meta:
        model = Työntekijä
        fields = "__all__"
        

    