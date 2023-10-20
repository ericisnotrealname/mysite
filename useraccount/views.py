from django.shortcuts import render
from django.contrib.auth.views import LoginView as DjangoLoginView


class DLoginView(DjangoLoginView):
    template_name = "login.html"
    next_page = "/"


# Create your views here.
