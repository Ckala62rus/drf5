from django.contrib import admin
from blog.models import Categories, Posts


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_display_links = ['name']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        print("model is updated")


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Posts, PostAdmin)
