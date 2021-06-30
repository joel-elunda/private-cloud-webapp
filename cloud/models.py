from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from user.models import Profile


class Upload(models.Model):
    user = models.ForeignKey("user.Profile", verbose_name=_("User profile"), on_delete=models.CASCADE)
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
        return self.user.username

    def get_absolute_url(self):
        return reverse("Upload_detail", kwargs={"pk": self.pk})


# Create your models here.
class ModelWithFileField(models.Model):
    pass