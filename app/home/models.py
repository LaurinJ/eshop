from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class ContactInformation(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contact_info = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=False, max_length=20)
    email = models.EmailField(blank=False, max_length=50)
    subject = models.CharField(blank=False, max_length=50)
    message = models.TextField(blank=False)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name