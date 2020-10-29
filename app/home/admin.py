from django.contrib import admin

from .models import ContactInformation, ContactMessage


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status']
    list_filter = ['status']

admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)