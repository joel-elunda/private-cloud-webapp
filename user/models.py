from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=50, unique=True,  help_text='Unique value for product page URL, created from name.')
    bio = models.TextField(blank=True, null=True, )
    photo = models.ImageField(blank=True,  null=True, upload_to='static/users_photos/')
    newsletter = models.BooleanField(default=False) 
    meta_keywords = models.CharField('Meta Keywords', blank=True,   null=True, max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", blank=True,  null=True, max_length=255,   help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'profils'
        ordering = ['-created_at']
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username
 
    def __unicode__(self):
        return u"Profile de {0}".format(self.user.username)

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})