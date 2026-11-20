from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "organization", "ticket", "created_at")
    search_fields = ("full_name", "email", "phone", "organization")
    list_filter = ("ticket", "role", "experience", "industry")
    readonly_fields = ("created_at",)
