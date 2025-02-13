from django.db import models
from utilisateurs.models import CustomUser  
from filieres.models import Filiere  
from filieres.models import Niveau  # Correction du module d'import

class Etudiant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Suppression des guillemets inutiles
    date_naissance = models.DateField()
    adresse = models.TextField()
    numero_inscription = models.CharField(max_length=20, unique=True)
    documents = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.numero_inscription}"
    
class Inscription(models.Model):
    STATUT_CHOICES = [
        ('en attente', 'En attente'),
        ('validé', 'Validé'),
        ('rejeté', 'Rejeté'),
    ]
    
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en attente')

    def __str__(self):
        return f"{self.etudiant} - {self.filiere} - {self.niveau}"
