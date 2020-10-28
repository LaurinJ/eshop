from django.shortcuts import render

from app.home.forms import ContactForm
from .models import ContactInformation, ContactMessage

def contact(request):
    info = ContactInformation.objects.get(pk=1)
    form = ContactForm(None or request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', {'info':info, 'form':form})