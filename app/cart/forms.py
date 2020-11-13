from django import forms

class PositivIntegerField(forms.IntegerField):

    def validate(self, value):
        super().validate(value)
        if value < 1:
            raise forms.ValidationError('Počet nemuže být zaporný')

class CartForm(forms.Form):
    quantity = PositivIntegerField(initial=1, widget=forms.NumberInput(attrs={'class':'input'}))
    product_id = forms.CharField(max_length=10, widget=forms.HiddenInput())