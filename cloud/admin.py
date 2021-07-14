from django.contrib import admin
from cloud.models import Upload

# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    ordering = ['-updated_at']
    search_fields = ['slug']
    prepopulated_fields = {'slug': ('name',) } 


admin.site.register(Upload, UploadAdmin)