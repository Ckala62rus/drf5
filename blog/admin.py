from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Categories, Posts, PostImage


# Register your models here.
class PostInline(admin.StackedInline):
    model = Posts
    fields = [
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at'
    ]
    list_display = [
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at'
    ]
    readonly_fields = ['created_at', 'updated_at']
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]


class PostImagesInline(admin.TabularInline):
    model = PostImage
    fields = [
        "user",
        "post",
        "image",
        'created_at',
        'updated_at',
        "thumbnail_preview",
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
        'user',
        'thumbnail_preview',
    ]
    extra = 0

    def thumbnail_preview(self, obj):
        html = '<img src="{img}"  width="50" height="50" />'
        if obj.image:
            return format_html(html, img=obj.image.url)
        return format_html('<strong>There is no image for this entry.<strong>')

    thumbnail_preview.short_description = 'Миниатюра'
    thumbnail_preview.allow_tags = True


@admin.action(description="publish post")
def make_published_post(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="unpublish post")
def make_unpublished_post(modeladmin, request, queryset):
    queryset.update(is_active=False)


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    actions = [make_published_post, make_unpublished_post]
    fields = [
        'name',
        'description',
        'category',
        'is_active',
        'created_at',
        'updated_at'
    ]
    readonly_fields = ['created_at', 'updated_at']
    list_display = [
        'id',
        'name',
        'category_link',
        'is_active',
        'created_at',
        'updated_at'
    ]
    list_display_links = ['name']
    list_filter = ['is_active', 'category']
    inlines = [PostImagesInline]

    def category_link(self, obj):
        link = reverse(
            "admin:blog_categories_change",
            args=[obj.category_id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.category.name)

    category_link.short_description = 'Категория'

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        super().save_model(request, obj, form, change)
        print("model is updated")

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        obj.delete()


class PostImageAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "post",
        "image",
        "thumbnail_preview",
    )

    list_display = [
        'id',
        'image',
        'picture',
        'post_name',
        'post_category',
        'thumbnail',
    ]

    readonly_fields = ('thumbnail_preview',)

    def picture(self, obj):
        return "some text"

    def post_name(self, obj):
        return obj.post.name + " " + f"({obj.post.id})"

    def post_category(self, obj):
        return obj.post.category.name

    def thumbnail(self, obj):
        html = '<img src="{img}"  width="100" height="100" />'
        if obj.image:
            return format_html(html, img=obj.image.url)
        return format_html('<strong>There is no image for this entry.<strong>')

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail.short_description = 'Миниатюра'
    thumbnail_preview.short_description = 'Миниатюра'
    thumbnail_preview.allow_tags = True
    picture.short_description = 'Изображение'
    post_name.short_description = 'Пост'
    post_category.short_description = 'Категория поста'


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Posts, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
