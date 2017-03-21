from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'birth', 'email', 'ipv4')
    list_filter = ('birth',)
