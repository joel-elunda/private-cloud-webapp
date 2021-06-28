# Generated by Django 3.2.4 on 2021-06-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('slug', models.SlugField(help_text='Unique value for product page URL, created from name.', unique=True)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(upload_to='static/users_photos/')),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'UserModel',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
                'ordering': ['-created_at'],
            },
        ),
    ]