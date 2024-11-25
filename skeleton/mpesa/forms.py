from django import forms

class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(
        max_length=13,  # E.164 format (+2547XXXXXXXX)
        label="Phone Number",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +254712345678'}),
        help_text="Enter phone number in international format, e.g., +2547XXXXXXXX."
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Amount",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 500.00'}),
        min_value=1.0,
        help_text="Enter an amount to pay. Minimum: 1.00."
    )
