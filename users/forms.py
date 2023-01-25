from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'id':"nome"})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'id':"sobrenome"})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'id':"user"})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'email@email.com', 'class': 'form-control', 'id':"password"})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'id':"confirm-password"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'id':"email"})

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']