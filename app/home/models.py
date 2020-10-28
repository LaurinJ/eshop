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
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()