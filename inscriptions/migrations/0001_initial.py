# Generated by Django 5.1.5 on 2025-02-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_naissance', models.DateField()),
                ('adresse', models.TextField()),
                ('numero_inscription', models.CharField(max_length=20, unique=True)),
                ('documents', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('en attente', 'En attente'), ('validé', 'Validé'), ('rejeté', 'Rejeté')], default='en attente', max_length=20)),
            ],
        ),
    ]
