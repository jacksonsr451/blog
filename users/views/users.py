from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator
from ..models import Users

@has_role_decorator('admin')
def home_user(request):
    return render(request, 'users/home_user.html')

@has_role_decorator('admin')
def list_user(request):
    users = Users.objects.filter(occupation="user")
    return render(request, 'users/list_user.html', {'users': users})

@has_role_decorator('admin')
def change_user(request):
    user = Users.objects.get(pk=request.POST['id'])
    return render(request, 'users/change_user.html', {'user': user})

@has_role_decorator('update_user')
def update_user(request):
    user = Users.objects.get(pk=request.POST['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.username = request.POST['username']
    user.email = request.POST['email']
    if not user.check_password(request.POST['password']):
        user.set_password(request.POST['password'])
    user.save()
    return redirect('list_user')

@has_role_decorator('delete_user')
def delete_user(request):
    user = Users.objects.get(pk=request.POST['id'])
    user.delete()
    return redirect('list_user')

@has_role_decorator('invite_user')
def invite_user(request):
    # TODO: implement method by inviting user to the system
    return redirect('list_user')

@has_role_decorator('ban_user')
def ban_user(request):
    # TODO: create a new user with the same email as the banned user
    return redirect('list_user')

@has_role_decorator('add_user')
def add_user(request):
    return render(request, 'users/add_user.html')

@has_role_decorator('add_user')
def insert_user(request):
    first_name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = Users.objects.filter(email=email)
    if user.exists():
        # TODO: add error message
        return redirect('add_user')

    user = Users.objects.create_user(
        first_name=first_name, last_name=last_name, username=username, email=email, 
        password=password)
    # TODO: add success message
    return redirect('add_user')