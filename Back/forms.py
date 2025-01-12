from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('name', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['name']


class AccUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['avatar']