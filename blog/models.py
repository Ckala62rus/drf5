from django.db import models
from django.utils.safestring import mark_safe

from users.models.users import User


# Create your models here.


class Categories(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название",
        help_text="Title for your post"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Some description...",
        blank=True,
        null=True,
    )

    class Meta:
        # by default name app + class name.
        # example: app goods + class categories = goods_categories
        db_table = "categories"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ('id',)

    def __str__(self):
        return self.name + ': ' + str(self.pk)


class Posts(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название Статьи",
        help_text="Title",
    )
    description = models.TextField(
        verbose_name="Текст статьи",
        help_text="Lorem ipsum dollar sit amet",
        blank=False,
        null=True,
    )
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Опубликовано?",
        help_text="Опубликовать пост",
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )

    class Meta:
        # by default name app + class name.
        # example: app goods + class categories = goods_categories
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('id',)

    def __str__(self):
        return self.name + ': ' + f"({str(self.pk)})"


def upload_to(instance, filename):
    """ /images/posts/{post_id}/images/some-file.jpg """
    return '/'.join([
        'images',
        "posts",
        str(instance.post.id),
        "images",
        filename
    ])


class PostImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=upload_to
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )

    class Meta:
        db_table = "post_images"
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ('id',)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    def __str__(self):
        # return str(self.post.name) + ': ' + str(self.pk)
        return 'id : ' + str(self.pk)
