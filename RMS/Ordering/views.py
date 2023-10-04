from django.shortcuts import render, redirect
from .models import Menu, Tables, Orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def menu_view(request):
    menu = Menu.objects.all()
    return render(request, 'menus.html', {'menu': menu})

@login_required
def tables_view(request):
    tables = Tables.objects.all()
    return render(request, 'tables.html', {'tables': tables})

@login_required
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


def send_email(request):
    send_mail(
        "Greeting", 
        "Hello, we wanted to greet you just for fun. hahahaha",
        "josephmaniragaba9@gmail.com",
        ["josephmaniragaba09@gmail.com", "josephmaniragaba9@gmail.com"],
        fail_silently=False,
    )
    return render(request, 'menus.html')





        

