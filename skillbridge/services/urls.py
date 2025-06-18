from django.urls import path
from .views import (
    submit_service, service_list, submission_success,
    book_service, dashboard, edit_service, delete_service, manage_bookings, cancel_booking
)
from django.views.generic import TemplateView

urlpatterns = [
    path('submit/', submit_service, name="submit_service"),
    path('submission-success/', submission_success, name='submission_success'),
    path('all/', service_list, name='service_list'),
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit/<int:service_id>/', edit_service, name='edit_service'),
    path('delete/<int:service_id>/', delete_service, name='delete_service'),
    path('manage_bookings/', manage_bookings, name='manage_bookings'),
    path('booking/<int:pk>/cancel', cancel_booking, name='cancel_booking'),

]