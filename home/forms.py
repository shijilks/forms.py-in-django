
from django import forms

class FormName(forms.Form):
    # Define your form fields here
    name = forms.CharField()
    Email = forms.EmailField()
    description=forms.CharField(widget=forms.Textarea)
