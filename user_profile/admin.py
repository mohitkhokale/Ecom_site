from django.contrib import admin

# Register your models here.
from user_profile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=[ 'id','address','email','mobile','dob','about']

admin.site.register(UserProfile,UserProfileAdmin)