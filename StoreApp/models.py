
from django.contrib.auth.hashers import make_password, check_password

from django.db import models

from django.db import models
from django import forms

class User(models.Model):
    username = models.CharField(max_length=15, blank=False, unique=True)
    password = models.CharField(max_length=158, blank=False)
    count = models.IntegerField(default=0, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    remember_me = forms.BooleanField(required=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

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
    id = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=600, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    warranty = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    countryOfOrigin = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    width = models.DecimalField(max_digits=7, decimal_places=2)
    length = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=7, decimal_places=2)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=50)
    maxLoad = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=600, blank=True, null=True)
    mainImg = models.ImageField(upload_to='products/images/', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['subcategory']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return f"{self.title} - {self.material}"

class ProductImage(models.Model):
    imageName = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.title}"


