from django.db import models
from django.contrib.auth.models import User


class SkillService(models.Model):
    """
    A service that providers can offer.
    Needs admin approval before showing publicly.
    """
    CATEGORY_CHOICES = [
        ('Tutoring', 'Tutoring'),
        ('Tech Help', 'Tech Help'),
        ('Sewing', 'Sewing'),
        ('Gardening', 'Gardening'),
        ('Other', 'Other'),

    ]

    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    rate_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.provider.username}"


class BookingRequest(models.Model):
    """
    A request from a client to book a service.
    Starts as 'pending' until provider accepts/rejects.
    """
    service = models.ForeignKey('SkillService', on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.TextField()
    requested_date = models.DateField()
    status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} -> {self.service.title}"
