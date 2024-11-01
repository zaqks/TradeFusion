from django.urls import path
from .views import stocks, imports, exports

app_name = "stocks_app"

urlpatterns  =[
    path("", stocks, name="stocks"),
    path("imports", imports, name="imports"),
    path("exports", exports, name="exports")
]