# Generated by Django 4.1.3 on 2023-01-10 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_meta_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='article',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='blogcategory',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='blogcategory',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='blogcategory',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='meta_title',
        ),
    ]
