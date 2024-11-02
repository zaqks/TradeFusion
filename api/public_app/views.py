from django.shortcuts import render

def landing(request):
    return render(request, "public_app/landing.html", {})
