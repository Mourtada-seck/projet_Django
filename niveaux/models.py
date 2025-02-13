from django.db import models  # Suppression de l'import inutile d'AbstractUser

class Niveau(models.Model):
    nom = models.CharField(max_length=50, unique=True)  # Ajout de "unique=True" pour éviter les doublons

    def __str__(self):
        return self.nom
