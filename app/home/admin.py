from django.contrib import admin

from .models import ContactInformation


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(ContactInformation, ContactInformationAdmin)