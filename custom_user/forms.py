from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    displayname = forms.CharField(max_length=60)
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)
    fieldname = forms.URLField(max_length=200)
    age = forms.IntegerField()
