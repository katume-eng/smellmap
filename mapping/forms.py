from django import forms
from .models import Smell

class SmellForm(forms.ModelForm):
    class Meta:
        model = Smell
        fields = ['name', 'description', 'latitude', 'longitude', 'intensity', 'user']
