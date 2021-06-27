from django import forms
from user.models import UserModel

class UserLogin(forms.Form):
    class Meta:
        model = UserModel
        fields = ['email', 'password']

class UserRegister(forms.Form):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password']