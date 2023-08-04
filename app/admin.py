from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog

class CustomUserAdmin(UserAdmin):
    # Add any customizations you need to display user fields in the admin interface
    list_display = ['id','username', 'email', 'first_name', 'last_name', 'is_staff']

class BlogAdmin(admin.ModelAdmin):
    exclude = ('image',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BlogAdmin)