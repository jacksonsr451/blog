from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class UsersAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Users
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('occupation',)}),
    )
