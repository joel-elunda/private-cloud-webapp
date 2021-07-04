from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, )
    # slug = models.SlugField(max_length=50, unique=True,  help_text='Unique value for product page URL, created from name.')
    bio = models.TextField(blank=True, null=True, )
    photo = models.ImageField(blank=True,  null=True, upload_to='static/users_photos/')
    newsletter = models.BooleanField(default=False) 
    meta_keywords = models.CharField('Meta Keywords', blank=True,   null=True, max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", blank=True,  null=True, max_length=255,   help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username
 
    def __unicode__(self):
        return u"Profile de {0}".format(self.user.username)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfiles")
 

    def get_absolute_url(self):
        return reverse("UserProfile_detail", kwargs={"pk": self.pk})
