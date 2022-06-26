from django import forms


class CodeForm(forms.Form):
    dotaz = forms.CharField(label="", widget=forms.Textarea)
