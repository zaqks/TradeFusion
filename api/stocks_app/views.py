from django.shortcuts import render

# Create your views here.



def stocks(request):
    return render(request, "stocks_app/stocks.html", {})