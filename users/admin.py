from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users.models.users import User


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields = ("id",)
    list_display_links = ["id", "username"]
    list_display = ("id", "username", "email", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {
            "fields": ("id",)
        }),
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
