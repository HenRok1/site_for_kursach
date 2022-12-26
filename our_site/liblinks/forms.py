from django.forms import fields
from .models import Liblinks
from django import forms


class LiblinksForm(forms.ModelForm):
    class Meta:
        model = Liblinks
        fields = '__all__'

