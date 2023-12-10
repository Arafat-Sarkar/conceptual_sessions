from django import forms

class djangoForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()