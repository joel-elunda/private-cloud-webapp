from django.contrib import admin
from user.models import UserModel

class UserAdmin(admin.ModelAdmin):
    ordering = ['-updated_at']
    search_fields = ['username']
    prepopulated_fields = {'slug': ('name',) } 
    prepopulated_fields = {'password': ('name',) } 

admin.site.register(UserModel, UserAdmin)