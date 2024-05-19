from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models.users import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    pass