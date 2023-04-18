# Generated by Django 4.1.7 on 2023-03-24 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('First_Name', models.CharField(default='User_LastName', max_length=15)),
                ('Last_Name', models.CharField(default='User_LastName', max_length=15)),
                ('Email', models.EmailField(default='learningdjango@gmail.com', max_length=30)),
                ('slug', models.SlugField(default='default', max_length=250, unique_for_date='Publish')),
                ('Publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('Brief_Content', models.TextField(max_length=69, null=True)),
                ('Content', models.TextField()),
                ('Status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blogApp.category')),
            ],
            options={
                'ordering': ('-Publish',),
            },
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=25)),
                ('Content', models.TextField()),
                ('Publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('Status', models.BooleanField(default=True)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='blogApp.post')),
            ],
            options={
                'ordering': ('-Publish',),
            },
        ),
    ]
