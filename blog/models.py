from django.db import models

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
        return self.name + ': ' + str(self.pk)
