# Generated by Django 4.1.3 on 2022-12-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_tag_articles_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]