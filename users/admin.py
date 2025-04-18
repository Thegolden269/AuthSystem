# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser', 'date_joined']
