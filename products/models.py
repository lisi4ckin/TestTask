from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)  # type: Category
    name = models.CharField(max_length=40)
    price = models.IntegerField(null=False)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name
