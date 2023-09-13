from django.contrib import admin
from .models import Menu, Tables, Orders

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']


class TablesAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'table_status']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'name_of_menu_ordered', 'customer_preferences', 'customer_name', 'waiter', 'table_of_order']



admin.site.register(Menu, MenuAdmin)
admin.site.register(Tables, TablesAdmin)
admin.site.register(Orders, OrdersAdmin)

