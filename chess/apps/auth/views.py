from django.contrib.auth import logout
from django.shortcuts import redirect, render

from ..board.views import home

def index(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        return redirect("auth:login")

def login(request):
    return render(request, "auth/login.html")

def logout_view(request):
    logout(request)
    return redirect("auth:login")
