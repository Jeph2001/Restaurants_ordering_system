from django.shortcuts import render, redirect
from .models import Menu, Tables, Orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def menu_view(request):
    menu = Menu.objects.all()
    return render(request, 'menus.html', {'menu': menu})


def tables_view(request):
    tables = Tables.objects.all()
    return render(request, 'tables.html', {'tables': tables})


def orders_view(request):
    orders = Orders.objects.all()
    return render(request, 'orders.html', {'orders': orders})


# this is the user authentication part

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/orders/')
        else:
            messages.info(request, 'Wrong Password or username')
            return redirect('/')
    
    return render(request, 'login_page.html')


def logout_view(request):
    logout(request)
    return redirect('/')


        

