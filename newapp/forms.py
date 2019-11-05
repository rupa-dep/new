from django import forms
from newapp.models import empregmodel
class empregform(forms.ModelForm):
      class Meta:
          model=empregmodel
          fields="__all__"

