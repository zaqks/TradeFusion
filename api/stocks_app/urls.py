from django.urls import path
from .views import stocks

app_name = "stocks_app"

urlpatterns  =[
    path("", stocks, name="stocks")
]