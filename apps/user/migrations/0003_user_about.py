# Generated by Django 4.1.5 on 2023-01-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='О себе'),
        ),
    ]
