# Generated by Django 4.2 on 2023-07-03 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_rename_thumbsdown_post_likes_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
