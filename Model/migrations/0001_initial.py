# Generated by Django 4.2.7 on 2024-02-13 08:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('numero_permis_conduire', models.CharField(max_length=20, unique=True)),
                ('date_embauche', models.DateField(blank=True, null=True)),
                ('date_de_naissance', models.DateField(blank=True, null=True)),
                ('numero_telephone', models.CharField(max_length=15)),
                ('adresse', models.TextField(blank=True, null=True)),
                ('disponibilite', models.BooleanField(default=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('num_cni', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ImagesConducteur/')),
            ],
        ),
        migrations.CreateModel(
            name='Demande_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('en_cours', models.BooleanField(default=True)),
                ('accepter', models.BooleanField(default=False)),
                ('refuser', models.BooleanField(default=False)),
                ('conducteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.conducteur')),
            ],
        ),
        migrations.CreateModel(
            name='Demande_prolongement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree', models.CharField(max_length=250)),
                ('motif', models.CharField(max_length=250)),
                ('en_cours', models.BooleanField(default=True)),
                ('accepter', models.BooleanField(default=False)),
                ('refuser', models.BooleanField(default=False)),
                ('conducteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.conducteur')),
            ],
        ),
        migrations.CreateModel(
            name='Deplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateTimeField()),
                ('niveau_carburant', models.IntegerField()),
                ('duree_deplacement', models.CharField(max_length=250)),
                ('depart', models.BooleanField(default=False)),
                ('arrivee', models.BooleanField(default=False)),
                ('kilometrage_depart', models.IntegerField()),
                ('statut', models.CharField(choices=[('en cours', 'En cours...'), ('arrivée', 'Arrivée')], default='en cours', max_length=50)),
                ('conducteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.conducteur')),
                ('demande_prolongement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.demande_prolongement')),
            ],
        ),
        migrations.CreateModel(
            name='EtatArrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometrage_arrive', models.IntegerField()),
                ('niveau_carburant_a', models.IntegerField()),
                ('date_arrive', models.DateField()),
                ('deplacement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deplacement_etat', to='Model.deplacement')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_incident', models.TextField()),
                ('conducteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.conducteur')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateTimeField()),
                ('niveau_carburant', models.IntegerField()),
                ('duree_deplacement', models.CharField(max_length=250)),
                ('depart', models.BooleanField(default=False)),
                ('arrivee', models.BooleanField(default=False)),
                ('kilometrage_depart', models.IntegerField()),
                ('statut', models.CharField(choices=[('en cours', 'En cours...'), ('arrivée', 'Arrivée')], default='en cours', max_length=50)),
                ('demande_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.demande_location')),
                ('demande_prolongement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.demande_prolongement')),
            ],
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'admin'), ('gestionnaire', 'gestionnaire'), ('conducteur', 'conducteur'), ('client', 'client')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mon_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nom', models.CharField(max_length=250, verbose_name='nom')),
                ('prenom', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('conducteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.conducteur')),
                ('roles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.roles')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_immatriculation', models.CharField(max_length=250)),
                ('couleur', models.CharField(blank=True, max_length=250, null=True)),
                ('carte_grise', models.CharField(max_length=250)),
                ('date_mise_circulation', models.DateField(blank=True, null=True)),
                ('date_d_edition', models.DateField(blank=True, null=True)),
                ('type_commercial', models.CharField(blank=True, max_length=250, null=True)),
                ('carrosserie', models.CharField(blank=True, max_length=250, null=True)),
                ('place_assises', models.IntegerField(blank=True, null=True)),
                ('date_expiration_assurance', models.DateField()),
                ('date_videnge', models.DateField()),
                ('kilometrage', models.IntegerField()),
                ('energie', models.CharField(choices=[('essence', 'Essence'), ('diesel', 'Diesel'), ('electrique', 'Électrique'), ('hybride', 'Hybride'), ('hybride_rechargeable', 'Hybride Rechargeable'), ('gaz_naturel', 'Gaz Naturel'), ('hydrogene', 'Hydrogène')], max_length=250)),
                ('marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.marque')),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('demande_prolongement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.demande_prolongement')),
                ('deplacement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.deplacement')),
                ('etat_arrive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.etatarrive')),
                ('incident', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.incident')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.location')),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.vehicule')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.utilisateur'),
        ),
        migrations.AddField(
            model_name='incident',
            name='vehicule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.vehicule'),
        ),
        migrations.AddField(
            model_name='etatarrive',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.location'),
        ),
        migrations.AddField(
            model_name='etatarrive',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='utilisateur_etat', to='Model.utilisateur'),
        ),
        migrations.CreateModel(
            name='Entretien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entretien', models.DateField()),
                ('prix_entretient', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.utilisateur')),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.vehicule')),
            ],
        ),
        migrations.AddField(
            model_name='deplacement',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.utilisateur'),
        ),
        migrations.AddField(
            model_name='deplacement',
            name='vehicule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.vehicule'),
        ),
        migrations.AddField(
            model_name='demande_location',
            name='paniers',
            field=models.ManyToManyField(to='Model.vehicule'),
        ),
        migrations.CreateModel(
            name='Carburant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('essence', 'Essence'), ('diesel', 'Diesel'), ('electrique', 'Électrique'), ('hybride', 'Hybride'), ('hybride_rechargeable', 'Hybride Rechargeable'), ('gaz_naturel', 'Gaz Naturel'), ('hydrogene', 'Hydrogène')], max_length=250)),
                ('prix', models.IntegerField()),
                ('quantite', models.IntegerField()),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.utilisateur')),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Model.vehicule')),
            ],
        ),
    ]
