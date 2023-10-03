from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# those are the routes for the created views
urlpatterns = [
    path('menu/', views.menu_view),
    path('tables/', views.tables_view),
    path('orders/', views.orders_view),
    path('', views.login_view),
    path('logout/', views.logout_view),
    path('change/', auth_views.PasswordChangeView.as_view(template_name="login.html")),
]
