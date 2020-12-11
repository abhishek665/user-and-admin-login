from django import forms
from . models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RegForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


class EditForm(UserChangeForm):
    class Meta:
        model = Registration
        fields = ('Firstname', 'Lastname')