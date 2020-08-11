from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, "reg_auth/index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'reg_auth/register.html', context)