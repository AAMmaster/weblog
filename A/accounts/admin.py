from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from . models import User
from django.utils.html import mark_safe


class UserAdmin(BaseUserAdmin):
    def image_tag(self):
        return mark_safe(f'<img src="{self.avatar.url}" width="50" height="50" style="border-radius:12px" />' if self.avatar else "")
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['first_name', "email", image_tag, "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("Main", {"fields": ['first_name', 'last_name', 'username', 'phone_number', 'avatar', "email", "password"]}),
        ("Permissions", {"fields": ['is_active', "is_admin", 'last_login']}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
            (None, {"fields":('first_name', 'last_name', 'username', 'phone_number', 'avatar', "email", "password1", 'password2')
            }),
        )

    search_fields = ["email", 'username']
    ordering = ["last_name"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
