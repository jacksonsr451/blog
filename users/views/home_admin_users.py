from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator
from ..models import Users

@has_role_decorator('admin')
def home_admin_users(request):
    return render(request, 'home_admin_users.html')

@has_role_decorator('admin')
def list_guests(request):
    users = Users.objects.filter(occupation="guest")
    return render(request, 'home_admin_guests.html', {'users': users})

@has_role_decorator('admin')
def show_guest(request):
    user = Users.objects.get(pk=request.POST['id'])
    return render(request, 'home_admin_change.html', {'user': user})

@has_role_decorator('admin')
def list_banneds(request):
    users = Users.objects.filter(occupation="banned")
    return render(request, 'home_admin_banneds.html', {'users': users})

@has_role_decorator('admin')
def get_banned(request):
    user = Users.objects.get(pk=request.POST['id'])
    return render(request, 'home_admin_change.html', {'user': user})

@has_role_decorator('admin')
def admin_delete_user(request):
    user = Users.objects.get(pk=request.POST['id'])
    user.delete()
    return redirect('home_admin_users')

@has_role_decorator('admin')
def admin_update_user(request):
    user = Users.objects.get(pk=request.POST['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.occupation = request.POST['occupation']
    user.save()
    return redirect('home_admin_users')