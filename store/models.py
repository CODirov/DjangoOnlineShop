from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime, timezone
from django.conf import settings


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=255)
    is_stuff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class Category(models.Model):
    class Meta():
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    name = models.CharField(max_length=255, verbose_name="Nomi")
    icon = models.ImageField(upload_to="images/", null=True, verbose_name="Rasmi")
    slug = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    class Meta():
        verbose_name = "Kichik kategoriya"
        verbose_name_plural = "Kichik kategoriyalar"

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    slug = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta():
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    title = models.CharField(max_length=255)
    price = models.FloatField()
    slug = models.CharField(max_length=255, null=True)
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="images/", null=True)
    sub_category = models.ForeignKey(Subcategory, on_delete=CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.price}"

    def get_rating_precent(self):
        return 100 * (self.rating/5)

    def is_new_product(self):
        time_delta = datetime.now(timezone.utc) - self.created_at
        return time_delta.seconds < settings.NEW_PRODUCT_SECONDS