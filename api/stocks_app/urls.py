from django.urls import path
from .views import stocks, imports, exports, stock, export_add

app_name = "stocks_app"

urlpatterns  =[
    path("", stocks, name="stocks"),
    path("<int:pk>", stock, name="stock"),
    #
    path("imports", imports, name="imports"),
    path("exports", exports, name="exports"),
    path("exports/add", export_add, name="export_add"),

]