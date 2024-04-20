# user_management/forms.py

from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'mobile']
