from django.contrib import admin
from blog.models import Categories, Posts


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Posts, PostAdmin)
