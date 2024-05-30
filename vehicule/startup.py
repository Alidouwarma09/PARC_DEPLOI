import time
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from Model.models import Vehicule

def envoyer_emails_assurance_vehicules():
    date_actuelle = datetime.now().date()
    une_semaine_plus_tard = date_actuelle + timedelta(days=3)

    vehicules_avec_assurance_expiree = Vehicule.objects.filter(date_expiration_assurance__lt=date_actuelle)
    vehicules_proches_expiration = Vehicule.objects.filter(
        date_expiration_assurance__gte=date_actuelle, date_expiration_assurance__lte=une_semaine_plus_tard
    ).exclude(id__in=vehicules_avec_assurance_expiree)

    if vehicules_avec_assurance_expiree:
        sujet_assurance_expiree = "Véhicules avec assurance déjà expirée"
        message_assurance_expiree = "Voici la liste des véhicules avec une assurance déjà expirée :\n\n"

        for vehicule in vehicules_avec_assurance_expiree:
            jours_depuis_expiration = (date_actuelle - vehicule.date_expiration_assurance).days
            message_assurance_expiree += f"- Véhicule {vehicule} : L'assurance est déjà expirée depuis {jours_depuis_expiration} jours\n"

        destinataire_assurance_expiree = "azertyazerty1ze@gmail.com"  # Remplacez par l'adresse email du destinataire

        try:
            send_mail(
                sujet_assurance_expiree,
                message_assurance_expiree,
                settings.EMAIL_HOST_USER,
                [destinataire_assurance_expiree],
                fail_silently=False,
            )
            print("Email pour véhicules avec assurance expirée envoyé avec succès")
        except Exception as e:
            print(f"Une erreur est survenue lors de l'envoi de l'email pour véhicules avec assurance expirée : {e}")

    if vehicules_proches_expiration:
        sujet_proches_expiration = "Véhicules avec assurance expirant bientôt"
        message_proches_expiration = "Voici la liste des véhicules avec une assurance expirant dans les 3 prochains jours :\n\n"

        for vehicule in vehicules_proches_expiration:
            jours_restants = (vehicule.date_expiration_assurance - date_actuelle).days
            message_proches_expiration += f"- Véhicule {vehicule} : {jours_restants} jours restants\n"

        destinataire_proches_expiration = "azertyazerty1ze@gmail.com"  # Remplacez par l'adresse email du destinataire

        try:
            send_mail(
                sujet_proches_expiration,
                message_proches_expiration,
                settings.EMAIL_HOST_USER,
                [destinataire_proches_expiration],
                fail_silently=False,
            )
            print("Email pour véhicules avec assurance expirant bientôt envoyé avec succès")
        except Exception as e:
            print(f"Une erreur est survenue lors de l'envoi de l'email pour véhicules avec assurance expirant bientôt : {e}")

    if not vehicules_avec_assurance_expiree and not vehicules_proches_expiration:
        print("Aucun véhicule avec assurance expirée ou expirant bientôt trouvé.")

def start_scheduler():
    target_hour = 11
    target_minute = 51
    while True:
        now = datetime.now()
        if now.hour == target_hour and now.minute == target_minute:
            envoyer_emails_assurance_vehicules()
            # Attendre 24 heures avant de vérifier à nouveau
            time.sleep(24 * 60 * 60)
        time.sleep(30)  # Vérifie toutes les 30 secondes
