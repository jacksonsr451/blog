from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Users
        
class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
