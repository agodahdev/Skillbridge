from django import forms
from .models import SkillService, BookingRequest


# This form will allow providers to submit services
class SkillServiceForm(forms.ModelForm):
    class Meta:
        model = SkillService
        fields = ['title', 'description', 'category', 'rate_per_hour']


# This form will allow clients to book a service
class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['messages', 'requested_date']
        widgets = {
            'requested_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'messages': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short message for the provider'
            })

        }