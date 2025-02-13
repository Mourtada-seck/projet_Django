from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('agent', 'Agent d\'inscription'),
        ('etudiant', 'Étudiant'),
    ]
    
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='etudiant'
    )
    photo = models.ImageField(upload_to='photos_profil/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
