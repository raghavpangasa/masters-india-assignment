from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sub_categories")
    slug = models.SlugField(unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_categories")
    slug = models.SlugField(unique=True, db_index=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
