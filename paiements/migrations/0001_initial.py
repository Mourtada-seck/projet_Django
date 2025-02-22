# Generated by Django 5.1.5 on 2025-02-08 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode_paiement', models.CharField(choices=[('Orange Money', 'Orange Money'), ('Wave', 'Wave'), ('Espèces', 'Espèces')], max_length=20)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('reçu', models.FileField(blank=True, null=True, upload_to='reçus/')),
                ('inscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscriptions.inscription')),
            ],
        ),
    ]
