from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']