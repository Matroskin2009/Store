from django.contrib import admin
from .models import Product, ProductImage, Category, SubCategory, Product3DModel


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('title', 'material', 'category', 'has_3d_model')  # заменяем model_3d на has_3d_model
    list_filter = ('category',)

    def has_3d_model(self, obj):
        return bool(obj.model_3d)
    has_3d_model.boolean = True
    has_3d_model.short_description = 'Есть 3D модель'

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'product')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product3DModel)
class Product3DModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'description')