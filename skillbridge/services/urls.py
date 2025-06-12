from django.urls import path
from .views import submit_service, service_list, submission_success, book_service
from django.views.generic import TemplateView

urlpatterns = [
    path('submit/', submit_service, name="submit_service"),
    path('submission-success/', submission_success, name='submission_success'),
    path('all/', service_list, name='service_list'),
    path('book/<int:service_id>', book_service, name='book_service'),

]