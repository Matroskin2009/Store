from django.contrib import admin
from .models import User, Product, ProductImage, Category, SubCategory

admin.site.register(User)


class ProductImageInline(admin.TabularInline):  # Или admin.StackedInline для другого стиля
    model = ProductImage
    extra = 3  # Количество пустых форм для добавления изображений

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('title', 'material', 'category') #Пример отображения в списке продуктов
    list_filter = ('category',)  # Добавляем фильтр по категориям

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('imageName', 'product') # Пример отображения в списке изображений

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)


@admin.register(Category)  # Регистрируем Category с настройками
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Какие поля показывать в списке категорий
    # Другие настройки для админки Category