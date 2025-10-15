from django import forms
from .models import SkillService, BookingRequest



class SkillServiceForm(forms.ModelForm):
    """Form for creating or editing a service."""
    class Meta:
        model = SkillService
        fields = ['title', 'description', 'category', 'rate_per_hour']



class BookingRequestForm(forms.ModelForm):
    """Form for booking a service with a date."""
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