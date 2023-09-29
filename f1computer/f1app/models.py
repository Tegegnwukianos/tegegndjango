from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="categories")

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    image = models.ImageField(upload_to='product_photos/')

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    photos = models.ManyToManyField(Photo)  # Many-to-Many relationship with Photo model
    main_image = models.ImageField(upload_to="products", blank=True, null=True)  # Main product image

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_image:
            resize_image(self.main_image)

    def saveSlug(self, *args, **kwargs):
        if not self.slug:
            # Generate the slug from the title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
