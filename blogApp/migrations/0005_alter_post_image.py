# Generated by Django 4.1.7 on 2023-03-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_post_image_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='media/Posts/Default.jpg', upload_to='media/Posts/'),
        ),
    ]
