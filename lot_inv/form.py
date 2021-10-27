from django import forms
from .models import LotInv, ProjectList


class LotInvForm(forms.ModelForm):
    class Meta:
        model = LotInv
        fields = '__all__'
        

