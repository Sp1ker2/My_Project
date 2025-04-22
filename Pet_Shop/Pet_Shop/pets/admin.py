from django.contrib import admin

from .models import Items, Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ["title", "description"]


class ItemsAdmin(admin.ModelAdmin):
    fields = ["title", "description", "price", "image", "category_id"]
    # inlines = [CategoryAdmin]


admin.site.register(Items, ItemsAdmin)
admin.site.register(Category, CategoryAdmin)
