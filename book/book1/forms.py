from django.forms import Form, ModelForm
from .models import *
from django import forms


class RegistrationForm(forms.Form):
    # password = forms.CharField(required=True, widget=forms.PasswordInput)
    class Meta:
        model = cutomers
        fields = ('username', 'password', 'emailid')
