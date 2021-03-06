from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from ckeditor_uploader.fields import RichTextUploadingField

user = get_user_model()

def category_image_url(instance, filename):
    '''upload_to for category image'''
    return 'category_{0}/{1}'.format(instance.id, filename)

def product_image_url(instance, filename):
    '''upload_to for category image'''
    return 'product_{0}/{1}'.format(instance.id, filename)

def images_url(instance, filename):
    '''upload_to for images'''
    return 'product_{0}/{1}'.format(instance.product.id, filename)

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to=category_image_url)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:category', args=[self.slug])

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to=product_image_url)
    price = models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField()
    detail = RichTextUploadingField(null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return ''

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to=images_url)

    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )

    comment = models.TextField()
    rating = models.IntegerField(default=5)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)