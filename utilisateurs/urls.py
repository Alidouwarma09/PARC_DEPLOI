from utilisateurs.views import Accueil_user, inscription_user, Connexion_user
from django.urls import path

app_name = 'utilisateur'

urlpatterns = [
    path('Accueil', Accueil_user, name='Accueil_user'),
    path('Inscription/', inscription_user, name='Inscription_user'),
    path('Connexion/', Connexion_user.as_view(), name='connexion_user'),
]
