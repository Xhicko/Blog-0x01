# Generated by Django 4.1.7 on 2023-03-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='Posts/Default.jpg', upload_to='Posts/'),
        ),
    ]
