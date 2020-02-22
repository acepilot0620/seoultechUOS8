from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField()
    student_number = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.user.username

#교수도 필요하면 추가할 것