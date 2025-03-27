from django import forms
from .models import CuentaContable

class CuentaForm(forms.ModelForm):
    class Meta:
        model = CuentaContable
        fields = '__all__'  # Or specify the fields you want to include
