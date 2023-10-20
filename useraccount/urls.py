from django.urls import include, path
from .views import DLoginView



urlpatterns = [
    path("", DLoginView.as_view(), name="login")
]