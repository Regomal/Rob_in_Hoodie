from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from apps.main.mixins import MetaTagMixin
from config.settings import MEDIA_ROOT
from apps.user.models import User


class BlogCategory(MetaTagMixin):
    name = models.CharField(verbose_name='Имя категории', max_length=255)
    # image = models.ImageField(verbose_name='Изображение', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блога'
        verbose_name_plural = 'Категории блога'

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'/>")

    image_tag_thumbnail.short_description = 'Изображение'


    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'/>")

    image_tag.short_description = 'Изображение'


class Article(MetaTagMixin):
    category = models.ForeignKey(verbose_name='Категория', to=BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью', null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    tags = models.ManyToManyField(to='Tag', verbose_name='Теги', blank=True)
    user = models.ForeignKey(verbose_name='Автор', to=User, on_delete=models.CASCADE, null=True, blank=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Tag(MetaTagMixin):
    name = models.CharField(verbose_name='Теги', max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class CommentArticle(models.Model):
    username = models.CharField(verbose_name="Пользователь", max_length=255)
    email = models.EmailField(verbose_name="E-mail", max_length=255)
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_checked = models.BooleanField(verbose_name="Проверен?", default=False)
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE)

    def user_image(self):
        if User.objects.get(email=self.email):
            image = User.objects.get(email=self.email).image_thumbnail
            return image

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


    def __str__(self):
        return self.username    #######

