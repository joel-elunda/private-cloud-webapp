# Generated by Django 3.2.4 on 2021-06-30 13:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cloud', '0001_initial'),
        ('user', '0002_remove_profil_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='Profile',
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created_at'], 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
    ]
