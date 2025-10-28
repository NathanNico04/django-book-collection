from django.urls import path
from . import views

urlpatterns = [
    path(
        "about/", views.about, name="about"
    ),  # Vue pour le template about (question 2)
    # Urls pour les collections
    path("collection/<int:collec_id>", views.collec, name="collection"),
    path("all/", views.all_collec, name="all_collections"),
    path("new/", views.new_collection, name="new_collec"),
    path("delete/<int:collec_id>", views.delete_collection, name="delete_collection"),
    path("change/<int:collec_id>/", views.edit_collection, name="edit_collection"),
    path("", views.index, name="index"),
    # Urls pour les éléments
    path("element/add/", views.new_element, name="new_element"),
    path(
        "element/delete/<int:element_id>", views.delete_element, name="delete_element"
    ),
    path("element/<int:element_id>", views.element, name="element"),
    path("element/edit/<int:element_id>", views.edit_element, name="edit_element"),
]
