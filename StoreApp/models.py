
from django.contrib.auth.models import User


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/images/', blank=True, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):  # Выносим как отдельную модель
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Product(models.Model):
    #id = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=600, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    warranty = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    country_of_origin = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    width = models.DecimalField(max_digits=7, decimal_places=2)
    length = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=7, decimal_places=2)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=50)
    max_load = models.PositiveIntegerField()
    description = models.CharField(max_length=600, blank=True, null=True)
    main_img = models.ImageField(upload_to='products/images/', blank=True)
    model_3d = models.FileField(upload_to='models3d/', blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['subcategory']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return f"{self.title} - {self.material}"

class ProductImage(models.Model):
    image_name = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.title}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.product.title}"

class Product3DModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='models_3d')
    model_file = models.FileField(upload_to='StoreProject/StoreApp/models3d/')  # Загрузка файла 3D-модели
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"3D Model for {self.product.title}"