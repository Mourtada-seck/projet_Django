from django.db import models  # ✅ Import de models
from utilisateurs.models import CustomUser  # ✅ Import du modèle utilisateur

class Notification(models.Model):
    destinataire = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification pour {self.destinataire} - {self.date_envoi}"
