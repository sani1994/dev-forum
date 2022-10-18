from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Title')
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    is_public = forms.BooleanField(widget=forms.HiddenInput())