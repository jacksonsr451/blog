from django.shortcuts import render, redirect
from rolepermissions.decorators import has_role_decorator


@has_role_decorator('admin')
def admin_area(request):
    return render(request, 'admin_area.html')
