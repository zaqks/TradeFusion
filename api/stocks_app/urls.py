from django.urls import path
from .views import stocks, imports, exports, stock

app_name = "stocks_app"

urlpatterns  =[
    path("", stocks, name="stocks"),
    path("<int:pk>", stock, name="stock"),
    #
    path("imports", imports, name="imports"),
    path("exports", exports, name="exports")
]