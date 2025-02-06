from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'type':"text",  'class': "form-control", 'id':"name",  'name':"name",  'value':"", 'placeholder':"Username"}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'type':"email", 'class':"form-control", 'id':"password", 'name':"email", 'value':"", 'placeholder':"Email"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'type':"password", 'class':"form-control", 'id':"password", 'name':"password1", 'value':"",'placeholder':"Password"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'type':"password", 'class':"form-control", 'id':"password", 'name':"password2", 'value':"", 'placeholder':"Confirm Password"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'type':"checkbox", 'id':"f-option", 'name':"selector"}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email already exists')
        return email


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'type':"text",  'class': "form-control", 'id':"name",  'name':"name",  'value':"", 'placeholder':"Username"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'type': "password", 'class': "form-control", 'id': "password", 'name': "password1", 'value': "",
               'placeholder': "Password"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'type':"checkbox", 'id':"f-option", 'name':"selector"}))

