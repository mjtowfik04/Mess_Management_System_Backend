from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # Admin list page
    list_display = ('email', 'first_name', 'Phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    ordering = ('email',)
    search_fields = ('email',)

    # User change page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name','last_name','address', 'Phone')}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # User add page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'address',
                'Phone',
                'is_staff',
                'is_active',
            ),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')
