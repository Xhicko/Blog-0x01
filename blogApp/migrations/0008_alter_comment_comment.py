# Generated by Django 4.2 on 2023-07-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Comment',
            field=models.TextField(max_length=270),
        ),
    ]
