from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import SkillService, BookingRequest

class ServiceTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.provider = User.objects.create_user(username='provider', password='pass1234')
        self.client_user = User.objects.create_user(username='client', password='pass1234')

    def test_submit_service_requires_login(self):
        response = self.client.get(reverse('submit_service'))
        self.assertRedirects(response, '/accounts/login/?next=/services/submit/')

    def test_service_submission(self):
        self.client.login(username='provider', password='pass1234')
        response = self.client.post(reverse('submit_service'), {
            'title': 'Test Service',
            'description': 'Some description',
            'category': 'Tutoring',
            'rate_per_hour': 50.00,
        })
        self.assertEqual(SkillService.objects.count(), 1)
        self.assertRedirects(response, reverse('submission_success'))

    def test_dashboard_authenticated(self):
        self.client.login(username='provider', password='pass1234')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Dashboard')

    def test_booking_request(self):
        service = SkillService.objects.create(
            provider=self.provider,
            title='Math Help',
            description='Basic math tutoring',
            category='Tutoring',
            rate_per_hour=20.00,
            is_approved=True,
        )
        self.client.login(username='client', password='pass1234')
        response = self.client.post(reverse('book_service', args=[service.id]), {
            'requested_date': '2025-07-01',
            'messages': 'Need help with fractions.'
        })
        self.assertEqual(BookingRequest.objects.count(), 1)
        self.assertRedirects(response, reverse('dashboard'))