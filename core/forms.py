from django import forms
from .models import Areas

class AreasForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Select Area")