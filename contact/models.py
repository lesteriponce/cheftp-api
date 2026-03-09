from django.db import models

class ContactRequest(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]

    full_name       = models.CharField(max_length=255)
    email           = models.EmailField()
    phone_number    = models.CharField(max_length=20)
    address         = models.CharField(max_length=500)
    date_requested  = models.DateTimeField()
    message         = models.TextField()
    status          = models.CharField(
                        max_length=10,
                        choices=STATUS_CHOICES,
                        default='new'
                      )
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email} ({self.status})"

    class Meta:
        ordering = ['-created_at']