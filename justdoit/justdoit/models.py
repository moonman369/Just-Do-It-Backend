from django.db import models
from django.utils.crypto import get_random_string
from .utils import uuid, uuid_task
from django.core.validators import EmailValidator, RegexValidator

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32, default=uuid)
    user_email = models.EmailField(validators=[EmailValidator])
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32, validators=[
        RegexValidator(regex='^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:"<>?`\-=[\]\\;\',./])', 
                       message='Password must contain at least one uppercase letter, one number, and one special character.')
    ])

    def __str__(self):
        return self.user_id


class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    ]

    task_id = models.CharField(primary_key=True, max_length=50, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return self.title