from django.db import models
from django.contrib.auth.models import User

class SkillService(models.Model):
    CATEGORY_CHOICES = [
        ('Tutoring', 'Turtoring'),
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