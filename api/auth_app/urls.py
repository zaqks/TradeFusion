from django.urls import path
from .views import sign_in, sign_up



app_name = "auth_app"

urlpatterns = [
    path("signin", sign_in, name="sign_in"),
    path("signup", sign_up, name="sign_up"),
]


