# Generated by Django 5.0.7 on 2024-07-15 03:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='massages/video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'ogg', 'avi', 'wmv'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
