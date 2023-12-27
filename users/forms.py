from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):#this will allows us to update username and the emails.
    email=forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email',]
        
class  ProfileUpdateForm(forms.ModelForm):#this will allows us to update profile
     class Meta:
         model = Profile
         fields=['image']