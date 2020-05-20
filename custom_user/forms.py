from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=60
    )
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    display_name = forms.CharField(
        max_length=60
    )
    username = forms.CharField(
        max_length=60
    )
    password = forms.CharField(widget=forms.PasswordInput)
