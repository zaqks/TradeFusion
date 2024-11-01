from django.urls import path
from .views import stocks

urlpatterns  =[
    path("", stocks)
]