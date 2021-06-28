from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True, )
    # password = models.
    slug = models.SlugField(max_length=50, unique=True,  help_text='Unique value for product page URL, created from name.')
    password = models.CharField(max_length=255, blank=True, null=True,)
    bio = models.TextField(blank=True, null=True, )
    photo = models.ImageField(blank=True,  null=True, upload_to='static/users_photos/')
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField('Meta Keywords', blank=True,   null=True, max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", blank=True,  null=True, max_length=255,   help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = _("UserModel")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("UserModel_detail", kwargs={"pk": self.pk})