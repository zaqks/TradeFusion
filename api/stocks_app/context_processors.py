from django.conf import settings

def currency(request):
    return {"currency": settings.CURRENCY}