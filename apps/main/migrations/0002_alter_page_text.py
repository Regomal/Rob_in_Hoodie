# Generated by Django 4.1.5 on 2023-02-21 15:58

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Содержание'),
        ),
    ]
