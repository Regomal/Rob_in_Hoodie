# Generated by Django 4.1.5 on 2023-02-25 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_commentarticle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentarticle',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
