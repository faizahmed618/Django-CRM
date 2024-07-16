from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from . import models

User = get_user_model()

class create_form(forms.Form):
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)
    age = forms.IntegerField()
    
class create_form_model(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = ("firstName", "lastName", "age", "agent")
        
class Customusercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
