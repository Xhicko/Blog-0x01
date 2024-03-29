# Generated by Django 4.2 on 2023-07-27 03:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0010_remove_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmark',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='bookmark_count',
            field=models.IntegerField(default=0),
        ),
    ]
