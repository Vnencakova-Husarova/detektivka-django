from django import forms


class CodeForm(forms.Form):
    dotaz = forms.CharField(widget=forms.Textarea)
