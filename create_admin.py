import os
import django

# Configurer les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parc_automobile.settings')
django.setup()

from Model.models import Utilisateur, Roles


def create_admin(nom, prenom, username, email, mot_de_passe, role_id):
    try:
        role = Roles.objects.get(id=role_id)
        utilisateur = Utilisateur.objects.create_admin(
            username=username,
            email=email,
            password=mot_de_passe,
            nom=nom,
            prenom=prenom,
            roles=role
        )
        utilisateur.save()
        print(f"Utilisateur {utilisateur.username} créé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")


if __name__ == '__main__':
    nom = 'Doe'
    prenom = 'John'
    username = 'admin'
    email = 'johndoe@gmail.com'
    mot_de_passe = '09102079Darius'
    role_id = 1

    create_admin(nom, prenom, username, email, mot_de_passe, role_id)
