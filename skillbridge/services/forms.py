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
        widgets = {'requested_date': forms.DateInput(
                attrs={
                    'type': 'date',}), 
        }
    

    def clean_requested_date(self):
         """
        Validate that the booking date is not in the past.
        Prevents users from booking services for dates that already happened.
        """
         requested_date = self.cleaned_data.get('requested_date')

        # Check if date is in the past
         if requested_date and requested_date < date.today():
          raise ValidationError("You cannot book a service for a date in the past.Please select today or a future date.")

          return requested_date