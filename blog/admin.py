from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Categories, Posts


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


class PostAdmin(admin.ModelAdmin):
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


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Posts, PostAdmin)
