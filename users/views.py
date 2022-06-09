from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator
from .models import Users

@has_role_decorator('admin')
def home_editor(request):
    return render(request, 'home_editor.html')

@has_role_decorator('add_editor')
def add_editor(request):
    return render(request, 'add_editor.html')

@has_role_decorator('add_editor')
def insert_editor(request):
    first_name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = Users.objects.filter(email=email)
    if user.exists():
        # TODO: add error message
        return redirect('add_editor')

    user = Users.objects.create_user(
        first_name=first_name, last_name=last_name, username=username, email=email, 
        password=password, occupation='editor')
    # TODO: add success message
    return redirect('add_editor')