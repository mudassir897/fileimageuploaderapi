from django.contrib import admin
from api.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileModeAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'email', 'dob', 'state', 'gender', 'pimage', 'rdocs',
    ]
