from django import forms
from .models import Contractus

class contractform(forms.ModelForm):
    class Meta:
        model=Contractus
        fields = ('name','email','subject','message')