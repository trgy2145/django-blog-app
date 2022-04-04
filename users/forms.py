from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta():
        model = User
        # fields = '__all__'
        # , 'portfolio', 'profile_pic', 'first_name', 'last_name'
        fields = ('username', 'email', 'password1', 'password2')
        # exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )


class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image', 'bio']
