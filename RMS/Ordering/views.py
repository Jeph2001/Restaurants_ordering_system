from django.shortcuts import render
from .models import Menu, Tables, Orders

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

