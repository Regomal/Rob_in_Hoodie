# Generated by Django 4.1.5 on 2023-02-25 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_article_publish_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Пользователь')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_checked', models.BooleanField(default=False, verbose_name='Проверен?')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='Статья')),
            ],
        ),
    ]
