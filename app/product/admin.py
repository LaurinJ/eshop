from django.contrib import admin
from django.utils.html import format_html

from app.product.models import Category, Product, Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_html']
    list_filter = ['category']
    readonly_fields = ['image_html']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug':('title',)}

    def image_html(self, obj):
        return format_html('<img src={} height="50">', obj.image.url)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)