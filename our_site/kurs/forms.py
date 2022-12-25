from django.forms import fields
from .models import Kurs
from django import forms


class KursForm(forms.ModelForm):
    class Meta:
        model = Kurs
        fields = '__all__'

