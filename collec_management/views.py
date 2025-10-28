from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from collec_management.models import *
from collec_management.forms import *


# About page -> /about (question 2)
def about(request):
    return render(request, "collec_management/about.html")


# Collections views -> /collection/n | modification de cette fonction pour ajouter les éléments liée à la collection (question 16)
@login_required
def collec(request, collec_id):
    try:
        collec = Collec.objects.get(pk=collec_id)
        elements = Element.objects.filter(collection=collec)
        if collec.user.pk != request.user.pk:
            return redirect("all_collections")
    except Collec.DoesNotExist:
        raise Http404("Désolé, cette collection n'existe pas")
    return render(
        request,
        "collec_management/collection.html",
        {"collection": collec, "elements": elements},
    )


# Toute la colletions views -> /all (question 6)
def all_collec(request):
    collec = Collec.objects.all()
    return render(
        request, "collec_management/all_collections.html", {"collections": collec}
    )


# formulaire d'ajout de collection -> /new (question 7)
@login_required
def new_collection(request):
    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            new_collection = form.save(
                commit=False
            )  # On créer mais on ne sauvegarde pas encore afin d'ajouter la date actuelle
            new_collection.date = timezone.now().date()  # On ajoute la date actuelle
            new_collection.user = request.user  # On assigne l'utilisateur connecté
            new_collection.save()  # On sauvegarde
            return redirect("all_collections")
    else:
        form = CollectionForm()

    return render(request, "collec_management/new_collection.html", {"form": form})


# Supprimer une collection
@login_required
def delete_collection(request, collec_id):
    collec = get_object_or_404(Collec, pk=collec_id)
    if collec.user.pk != request.user.pk:
        return redirect("all_collections")
    if request.method == "POST":
        collec.delete()
        return redirect("all_collections")
    return render(
        request, "collec_management/delete_collection.html", {"collection": collec}
    )


# Modifier une collection -> /change/n (question 9)
@login_required
def edit_collection(request, collec_id):
    collec = get_object_or_404(Collec, pk=collec_id)
    if collec.user.pk != request.user.pk:
        return redirect("all_collections")
    if request.method == "POST":
        form = CollectionForm(request.POST, instance=collec)
        if form.is_valid():
            form.save()
            return redirect("all_collections")
    else:
        form = CollectionForm(
            instance=collec
        )  # sinon si c'est un get on remplit le formulaire avec les données deja existante

    return render(
        request,
        "collec_management/edit_collection.html",
        {"form": form, "collection": collec},
    )


def index(request):
    return render(request, "collec_management/index.html")


# vue d'ajout d'élément -> /element/add (question 13)
@login_required
def new_element(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            new_element = form.save(commit=False)
            new_element.date = timezone.now().date()
            if new_element.collection.user != request.user:
                return redirect("all_collections")
            new_element.user = request.user
            new_element.save()
            return redirect("collection", collec_id=new_element.collection.id)
    else:
        form = ElementForm(
            user=request.user
        )  # On passe le user en paramètre pour être sur d'afficher uniquement les collections que cet user a créé

    return render(request, "collec_management/new_element.html", {"form": form})


# vue de suppression d'un élément -> /element/delete/n (question 13)
@login_required
def delete_element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if element.user.pk != request.user.pk:
        return redirect("collection", collec_id=element.collection.id)
    if request.method == "POST":
        element.delete()
        return redirect("collection", collec_id=element.collection.id)
    return render(
        request, "collec_management/delete_element.html", {"element": element}
    )


# voir un élément -> /element/n (question 15)
@login_required
def element(request, element_id):
    try:
        element = Element.objects.get(pk=element_id)
        if element.user.pk != request.user.pk:
            return redirect("collection", collec_id=element.collection.id)
    except Element.DoesNotExist:
        raise Http404("Désolé, cet élément n'existe pas")
    return render(request, "collec_management/element.html", {"element": element})


# Modifier un élément -> /element/edit/n (question 15)
@login_required
def edit_element(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if element.user.pk != request.user.pk:
        return redirect("collection", collec_id=element.collection.id)
    if request.method == "POST":
        form = ElementForm(request.POST, instance=element)
        if form.is_valid():
            form.save()
            return redirect("element", element_id=element.id)
    else:
        form = ElementForm(
            instance=element
        )  # sinon si c'est un get on remplit le formulaire avec les données deja existante

    return render(
        request,
        "collec_management/edit_element.html",
        {"form": form, "element": element},
    )
