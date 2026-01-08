from django import forms
from .models import details
class details_data(forms.ModelForm):
    class Meta:
        model=details
        fields=['name','email']