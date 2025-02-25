from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[('staff', 'Staff'), ('guardian', 'Guardian')], default='guardian')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

# Create your models here.
class Homework(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    class_id = models.CharField(max_length=20)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='homework') # Who created it


    def __str__(self):
        return self.title
    
class Student(models.Model):  # If you don't have this, adapt accordingly
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='students')
    class_id = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username