from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

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
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to=product_image_url)
    price = models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to=images_url)

    def __str__(self):
        return self.title