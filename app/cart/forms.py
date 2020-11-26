from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _

from .models import ShippingAddress



class AddressForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input ', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input ', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input ', 'placeholder': 'Email'}))
    telephone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input ', 'placeholder': 'Telephone'}))
    password1 = forms.CharField(
        # label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input ', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        # label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'input ', 'placeholder': 'Password again'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = ShippingAddress
        exclude = ['customer', 'order']