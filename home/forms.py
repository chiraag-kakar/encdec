from django import forms
from .models import AllData

# class PswdForm(forms.Form):
#     finder = forms.CharField(widget=forms.TextInput(attrs={
#         'type': 'password',
#         'id': 'password',
#         'class': 'validate'
#     }))

class EncryptForm(forms.Form):
    decText = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'materialize-textarea',
        'id': 'textarea2',
        'rows': '5',
        'data-length': '5000',
    }))
    finder = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'id': 'password',
        'class': 'validate'
    }))

class DecryptForm(forms.Form):
    encText = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'materialize-textarea',
        'id': 'textarea2',
        'rows': '5',
        'data-length': '5000',
    }))
    finder = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'id': 'password',
        'class': 'validate'
    }))