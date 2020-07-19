from django.forms import Form, ModelForm
from .models import *
from django import forms


class RegistrationForm(forms.Form):
    # password = forms.CharField(required=True, widget=forms.PasswordInput)
    class Meta:
        model = cutomers
        fields = ('username', 'password', 'emailid')


class rform(forms.ModelForm):
    #book_genre1 =  forms.ChoiceField(required=True, choices=['Thriller','Romance','Fiction'])
    class Meta:
        model = book2
        fields = ('Book_name','Image_file','Book_genre','Book_price',)


class bookform (forms.ModelForm):
    class Meta:
        model = book2
        fields = ('Book_name','Image_file','Book_genre','Book_price',)


