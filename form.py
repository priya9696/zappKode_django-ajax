from django import forms 
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    name= forms.CharField(max_length=100, required= True)
    username= forms.CharField(max_length=100, required= True)
    email= forms.CharField(max_length=100, required= True)
    contact= forms.IntegerField(required= True)
    password= forms.CharField(max_length=20, required= True, widget= forms.PasswordInput)
    confirm_password= forms.CharField(max_length=20, required= True, widget=forms.PasswordInput )


class UserLoginForm(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget= forms.PasswordInput))

    class Meta:
        model = User
        fields = ['username', 'email']
