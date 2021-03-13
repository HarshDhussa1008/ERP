from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('shop_login/', views.shop_login, name='shop_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='user_logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('tenant_dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
]