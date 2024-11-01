from django.urls import path
from .views import sign_in, sign_up




urlpatterns = [
    path("signin", sign_in),
    path("signup", sign_up),


]


