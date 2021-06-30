from django.contrib import admin
from user.models import Profil

class ProfilAdmin(admin.ModelAdmin):
    ordering = ['-updated_at']
    search_fields = ['username']
    # prepopulated_fields = {'slug': ('username',) } 
    # prepopulated_fields = {'user.password': ('username',) } 

admin.site.register(Profil, ProfilAdmin)