# Generated by Django 4.2.7 on 2024-01-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0002_conducteur_disponibilite_vehicule_disponibilite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deplacement',
            name='statut',
            field=models.CharField(choices=[('Départ', 'Départ'), ('en cours', 'En cours...'), ('arrivée', 'Arrivée')], default='Départ', max_length=50),
        ),
    ]
