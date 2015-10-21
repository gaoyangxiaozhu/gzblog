from django import forms

class CommonForms(forms.Form):
    author = forms.CharField(max_length=100)
    email = forms.EmailField()
    url = forms.URLField(required=False)
    comment = forms.Textarea(required=False)

