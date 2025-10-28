from django import forms
from collec_management.models import *


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collec
        fields = ["title", "description"]


class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ["title", "description", "value", "quantity", "collection"]
        widgets = {
            "collection": forms.Select(attrs={"class": "form-control"}),
        }

    # Méthode vu après le TP9
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(ElementForm, self).__init__(*args, **kwargs)
        if user:
            # Limiter les collections affichées à celles créées par l'utilisateur connecté
            self.fields["collection"].queryset = Collec.objects.filter(user=user)
