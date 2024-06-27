from django import forms

class create_form(forms.Form):
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)
    age = forms.IntegerField()
