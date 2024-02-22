from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from Model.models import Deplacement, Vehicule, Conducteur, Photo
from deplacement.forms import DeplacementForm



def enregistrer_deplacement(request):
    if request.method == 'POST':
        form = DeplacementForm(request.POST)
        if form.is_valid():

            deplacement = form.save(commit=False)
            deplacement.utilisateur = request.user

            # Obtenez l'instance du véhicule associé à ce déplacement (hypothétique)
            vehicule = deplacement.vehicule

            # Obtenez l'instance du conducteur associé à ce déplacement (hypothétique)
            conducteur= deplacement.conducteur

            # Mettez à jour la disponibilité du véhicule
            if vehicule:
                vehicule.disponibilite = False
                vehicule.save()

            #Mettez à jour l'aptitude du conducteur à avoir un véhicule
            if conducteur:
                conducteur.is_apt=False
                conducteur.save()


            deplacement.save()
            images = request.FILES.getlist('images')
            if len(images) <= 6:
                for uploaded_file in images:
                    photo = Photo.objects.create(deplacement=deplacement, images=uploaded_file)
            else:
                form.add_error('images', 'Vous ne pouvez sélectionner que 6 images.')



            messages.success(request, 'Déplacement enregistré avec succès !')
            return redirect('deplacement:enregistrer_deplacement')
    else:
        form = DeplacementForm()

    return render(request, 'enregistrer_deplacement.html', {'form': form})


def liste_deplacement(request):
    deplacement = Deplacement.objects.filter(depart=False, arrivee=False)

    paginator = Paginator(deplacement.order_by('date_mise_a_jour'), 3)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        deplacement = paginator.page(page)
    except EmptyPage:

        deplacement = paginator.page(paginator.num_pages())
    return render(request, 'afficher_deplacement.html', {'deplacements': deplacement})


def depart(request, pk):
    deplacement = get_object_or_404(Deplacement, pk=pk)
    deplacement.depart = True
    deplacement.statut = 'en cours'
    deplacement.save()  # Ligne corrigée
    return redirect('deplacement:liste_deplacement')


def liste_deplacement_en_cours(request):
    deplacement = Deplacement.objects.filter(depart=True, arrivee=False)
    paginator = Paginator(deplacement.order_by('date_mise_a_jour'), 3)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        deplacement = paginator.page(page)
    except EmptyPage:

        deplacement = paginator.page(paginator.num_pages())
    return render(request, 'afficher_deplacement_en_cours.html', {'deplacements': deplacement})


def arrivee(request, pk):
    deplacement = get_object_or_404(Deplacement, pk=pk)
    deplacement.arrivee = True
    deplacement.statut = 'arrivée'
    deplacement.save()  # Ligne corrigée
    return redirect('deplacement:liste_deplacement_en_cours')


def liste_deplacement_arrive(request):
    today = datetime.now()
    deplacement = Deplacement.objects.filter(depart=True, arrivee=True, date_arrivee__date=today)

    paginator = Paginator(deplacement.order_by('date_mise_a_jour'), 3)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        deplacement = paginator.page(page)
    except EmptyPage:

        deplacement = paginator.page(paginator.num_pages())
    return render(request, 'afficher_deplacement_arrive.html', {'deplacements': deplacement})
