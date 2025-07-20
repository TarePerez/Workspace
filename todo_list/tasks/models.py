from django.db import models

# Create your models here.

PRIORITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Incomplete')



    def __str__(self):
        return self.title
