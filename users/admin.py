from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django import forms

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('user_name','departament', 'first_name', 'last_name', 'middle_name')
    list_filter = ('departament', 'user_name', 'first_name', 'last_name', 'middle_name')
    ordering = ('user_name',)
    list_display = ('user_name', 'first_name', 'last_name', 'middle_name', 'departament', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('user_name', 'first_name', )}),
        ('Permissions', {'fields': ('is_active', 'departament', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal', {'fields': ('last_name', 'middle_name')}),)
    formfield_overrides = {
        NewUser.departament: {'widget': forms.Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'first_name', 'last_name', 'middle_name', 'departament', 'is_staff', 'is_active')}
         ),
    )
admin.site.register(NewUser, UserAdminConfig)