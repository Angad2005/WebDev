from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Feedback(models.Model):
    PRODUCT_CHOICES = [
        ('tuf', 'TUF'),
        ('zephyrus', 'Zephyrus'),
        ('zenbook', 'Zenbook'),
        ('strix', 'Strix'),
        ('vivobook', 'Vivobook'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(
    max_length=20,
    choices=PRODUCT_CHOICES,
    default='tuf'  # or any default product name
)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product}"