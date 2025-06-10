from django.urls import path
from .views import submit_service
from django.views.generic import TemplateView

urlpatterns = [
    path('submit/', submit_service, name="submit_service"),
    path('submission-success/', TemplateVie.as_view(,
        template_name='services/submission_success.html'
    ), name='submission_success'),

]