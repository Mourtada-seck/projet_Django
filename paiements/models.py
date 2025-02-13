from django.db import models
from inscriptions.models import Inscription  # 🔥 Import correct du modèle Inscription

class Paiement(models.Model):
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(
        max_length=20, 
        choices=[
            ('Orange Money', 'Orange Money'), 
            ('Wave', 'Wave'), 
            ('Espèces', 'Espèces')
        ]
    )
    date_paiement = models.DateTimeField(auto_now_add=True)
    reçu = models.FileField(upload_to='reçus/', blank=True, null=True)

    def __str__(self):
        return f"{self.inscription} - {self.montant} FCFA"
