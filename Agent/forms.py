from APP1 import models
from django import forms

class create_form_agent(forms.ModelForm):
    class Meta:
        model = models.Agent
        fields = ("user", "firstName", "lastName")