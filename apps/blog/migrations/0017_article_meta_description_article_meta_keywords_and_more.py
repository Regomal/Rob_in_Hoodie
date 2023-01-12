# Generated by Django 4.1.5 on 2023-01-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_article_meta_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
    ]
