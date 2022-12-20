from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['name','file']

class SearchForm(forms.Form):
    query = forms.CharField()