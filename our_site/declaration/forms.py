from django.forms import fields
from .models import Declaration
from django import forms


class DeclarationForm(forms.ModelForm):
    class Meta:
        model = Declaration
        fields = '__all__'

