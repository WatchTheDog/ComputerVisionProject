# forms.py
from django import forms
from .models import *


class SearchImageForm(forms.ModelForm):
    class Meta:
        model = SearchImage
        fields = ['imageToSearch']
