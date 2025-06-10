from django import forms
from .models import SkillService

#This from will allow providers to submit services
class SkillService(forms.ModelForm):
    class Meta:
        model = SkillService
        fields = ['title', 'descriptions', 'category', 'rate_per_hour']