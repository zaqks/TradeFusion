from django.shortcuts import render




def sign_in(request):
    return render("auth_app/signin.html")

def sign_up(request):
    return render("auth_app/signup.html")


