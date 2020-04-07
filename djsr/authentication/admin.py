from django.contrib import admin

from authentication import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    exclude = ['password']
    list_display = ('email', 'is_admin', 'is_staff', 'is_active', )
    search_fields = ["first_name", "last_name"]
