# Generated by Django 4.2 on 2023-05-20 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0012_rename_content_comment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Brief_Content',
        ),
    ]
