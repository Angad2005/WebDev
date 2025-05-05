# models.py
from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    PRODUCT_CHOICES = [
        ('tuf', 'TUF'),
        ('zephyrus', 'Zephyrus'),
        ('zenbook', 'Zenbook'),
        ('strix', 'Strix'),
        ('vivobook', 'Vivobook'),
    ]

    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(
        max_length=20,
        choices=PRODUCT_CHOICES,
        default='tuf'
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(
        max_length=10,
        choices=SENTIMENT_CHOICES,
        default='neutral'
    )

    def __str__(self):
        return f"{self.user.username} - {self.product}"