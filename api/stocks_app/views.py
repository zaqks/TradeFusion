from django.shortcuts import render
from .models import Stock
# Create your views here.



def stocks(request):
    stks = Stock.objects.all()

    return render(request, "stocks_app/stocks.html", {"stks":stks})



def imports(request):
    stks = Stock.objects.all()

    return render(request, "stocks_app/imports.html", {"stks":stks})



def exports(request):
    stks = Stock.objects.all()

    return render(request, "stocks_app/exports.html", {"stks":stks})


def export_add(request):
    return render(request, "stocks_app/export_add.html", {})


def stock(request, pk):
    itm = Stock.objects.get(id=pk)
    stks = Stock.objects.all()

    return render(request, "stocks_app/stock.html", {
        "itm":itm,
        "smlrs":stks})