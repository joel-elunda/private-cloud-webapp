from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User 
# from user.models import UserProfile


class Upload(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=50, null=True, blank=True)
    file = models.FileField(_("File"), upload_to='static/uploads/', max_length=100, null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True,  help_text='Unique value for product page URL, created from name.')
    meta_keywords = models.CharField('Meta Keywords', blank=True,   null=True, max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", blank=True,  null=True, max_length=255,   help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'uploads'
        verbose_name = _("Upload")
        verbose_name_plural = _("Uploads")
 

    def __str__(self):
        return '%s %s %s' % (self.file, self.name, self.updated_at)

    def get_absolute_url(self):
        return reverse("Upload_detail", kwargs={"pk": self.pk})


# Create your models here.
class ModelWithFileField(models.Model):
    pass