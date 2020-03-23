from django import forms
from django.core import validators



def vlad(value):
    if value[0].lower() != 'v':
        raise forms.ValidationError('your name is not Vlad')

class FormName(forms.Form):
    name = forms.CharField(validators=[vlad])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,    widget=forms.HiddenInput,   validators=[validators.MaxLengthValidator(0)])
