from django import forms
from . import models

class create_form(forms.Form):
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)
    age = forms.IntegerField()
    
class create_form_model(forms.ModelForm):
    class Meta:
        model = models.Lead
        fields = ("firstName", "lastName", "age", "agent")
