from django.shortcuts import render
from .models import Stock
# Create your views here.



def stocks(request):
    stks = Stock.objects.all()
    
    return render(request, "stocks_app/stocks.html", {"stks":stks})