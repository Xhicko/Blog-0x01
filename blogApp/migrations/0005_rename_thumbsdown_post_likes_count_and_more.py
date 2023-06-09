# Generated by Django 4.2 on 2023-07-02 21:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0004_rename_currentthumbs_thumbs_current_thumbs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbsdown',
            new_name='likes_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbs',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbsup',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Thumbs',
        ),
    ]
