from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import generic
from .forms import LoginForm


class DLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "index.html"
    # template_name = "login.html"
    next_page = "/"

# Create your views here.
