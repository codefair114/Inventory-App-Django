from django import forms
from .models import *

def get_custom_form(m, f):

    class _CustomForm(forms.ModelForm):
        class Meta:
            model = m
            fields = f

    return _CustomForm