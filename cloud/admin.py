from django.contrib import admin
from cloud.models import Upload

# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    ordering = ['-updated_at']


admin.site.register(Upload, UploadAdmin)