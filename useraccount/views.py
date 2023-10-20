from django.shortcuts import render
from django.contrib.auth.views import LoginView as DjangoLoginView
# from django.contrib.auth.forms import 
# from wagtail.views import LoginView as WagtailLoginView


class DLoginView(DjangoLoginView):
    template_name = "login.html"
    # form_class = 
    pass


# class WLoginView(WagtailLoginView):
#     template_name = "login.html"
#     ...

# Create your views here.
