from django.urls import path
from . import views

# those are the routes for the created views
urlpatterns = [
    path('menu/', views.menu_view),
    path('tables/', views.tables_view),
    path('orders/', views.orders_view),
]
