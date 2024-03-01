from django.urls import path

from deplacement.views import enregistrer_deplacement, depart, liste_deplacement, liste_deplacement_en_cours, arrivee, \
    liste_deplacement_arrive, modifier_deplacement, details_deplacement, enregistrer_etatArriver, details_arriver, \
    get_deplacements_data, get_deplacements_data2

app_name = 'deplacement'

urlpatterns = [
    path('enregistrer_deplacement/', enregistrer_deplacement, name='enregistrer_deplacement'),
    path('liste_deplacement/', liste_deplacement, name='liste_deplacement'),
    path('confirmer_depart/<int:pk>/', depart, name='depart'),
    path('liste_deplacement_en_cours/', liste_deplacement_en_cours, name='liste_deplacement_en_cours'),
    path('confirmer_arrive/<int:pk>/', arrivee, name='arrivee'),
    path('liste_deplacement_arrive/', liste_deplacement_arrive, name='liste_deplacement_arrive'),
    path('modifier_deplacement/<int:pk>/', modifier_deplacement, name='modifier_deplacement'),
    path('details_deplacement/<int:deplacement_id>/', details_deplacement, name='details_deplacement'),
    path('details_arriver/<int:etatarrive_id>/', details_arriver, name='details_arriver'),
    path('enregistrer_etatArriver/', enregistrer_etatArriver, name='enregistrer_etatArriver'),
    path('get_deplacements_data/', get_deplacements_data, name='get_deplacements_data'),
    path('get_deplacements_data2/', get_deplacements_data2, name='get_deplacements_data2'),


]