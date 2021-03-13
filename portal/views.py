from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import Tenant

# Create your views here.
def index(request):
    return render(request, 'portal/index.html')

def shop_login(request):
    return render(request, 'portal/shop_login.html')

def admin_login(request):
    return render(request, 'portal/admin_login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def admin_dashboard(request):
    data=Tenant.objects.all()
    for shop in data:
        print(shop.phone_number)
    return render(request, 'portal/admin_dashboard.html', {'shops': data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def tenant_dashboard(request):
    return render(request, 'portal/tenant.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(request.POST)
        #print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("success\n",user.username)
            if user.username.endswith('rishabh'):
                return redirect('admin_dashboard')
            else:
                return redirect('tenant_dashboard')
        else:
            # Return an 'invalid login' error message.
            print("failed\n",user)
            return redirect('index')
    else:
        return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')
