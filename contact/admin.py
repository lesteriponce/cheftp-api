from django.contrib import admin
from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'phone_number', 'status', 'created_at']
    list_filter   = ['status']
    search_fields = ['full_name', 'email']
    ordering      = ['-created_at']
