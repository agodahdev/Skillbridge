from django import forms
from .models import SkillService

#This from will allow providers to submit services
class SkillServiceForm(forms.ModelForm):
    class Meta:
        model = SkillService
        fields = ['title', 'description', 'category', 'rate_per_hour']