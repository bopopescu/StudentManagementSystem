from django.shortcuts import render, redirect
from django.urls import NoReverseMatch
from .models import admin_data
from .login_form import LogInForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    login = LogInForm()
    data = {
        'login_form' : login,
        'login_type' : 'admin',
    }
    return render(request, 'login.html', data)

def admin_entry(request):
    if request.method == "POST":

        try:
            user_id = request.POST['user_id']
            password = request.POST['password']
            #print(user_id)
            
            user = auth.authenticate(user_id = user_id, password = password)

            if user is not None:
                auth.login(request, user)
                return redirect('admin_page')
            else:
                messages.info(request, "Invalid user")
                return redirect('admin_login')
        except NoReverseMatch:
            messages.info(request, "No Reverse Match allowed")

    else:
        return render(request, 'login.html')

