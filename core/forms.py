from django import forms
from .models import Areas

class AreasForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Select Area")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial selected area, for example, the area with pk=1
        self.fields['area'].initial = Areas.objects.get(pk=1)  # Adjust pk as needed