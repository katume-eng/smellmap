from django.db import models

# Create your models here.

class User(models.Model):
    """
    Represents a user in the system.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class Smell(models.Model):
    """
    Represents a smell in the system.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    intensity = models.IntegerField(default=1)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='smells')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"