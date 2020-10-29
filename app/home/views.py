from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView


from app.home.forms import ContactForm
from .models import ContactInformation, ContactMessage


def contact(request):
    info = ContactInformation.objects.get(pk=1)
    form = ContactForm(None or request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', {'info':info, 'form':form})

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home:contact')
    success_message = 'The event  has been updated successfully'
    error_message = 'The event  could not be updated'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = ContactInformation.objects.get(pk=1)
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, self.error_message)
        # super().form_invalid(form)
        return self.render_to_response(self.get_context_data(form=form))