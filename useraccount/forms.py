# AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext_lazy


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 
                                                           "class": "form-control rounded-left",
                                                           "placeholder": "Username",}))
    password = forms.CharField(
        label = gettext_lazy("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "class":"form-control rounded-left",
                                          "placeholder": "Password"}),
    )