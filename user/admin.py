from django.contrib import admin
from user.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass
    ordering = ['-updated_at']
    search_fields = ['username']
    # prepopulated_fields = {'slug': ('username',) } 
    # prepopulated_fields = {'user.password': ('username',) } 

admin.site.register(UserProfile, UserProfileAdmin)