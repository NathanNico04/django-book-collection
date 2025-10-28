# CC1 - Framework Web

## Membres du Groupe

- **Maximilien Goujon** <maximilien.goujon@etu.univ-orleans.fr>
- **Nathan Nicolessi** <nathan.nicolessi@etu.univ-orleans.fr>
- **Lisa Blavot** <lisa.blavot@etu.univ-orleans.fr>
- **Theo Cretel** <theo.cretel@etu.univ-orleans.fr>

## Configuration Docker

- `USERNAME=$(id -un) USERID=$(id -u) docker-compose up -d`
- `docker exec -ti fw1-cc-"changeme" whoami`

## Configuration Projet

- **Installation extension `python` dans le conteneur**
- **Installation extension `black formater` dans le conteneur**
- **Ctrl/Cmd + Shift + P | Python : Select Interpreter** _Python 3.12 ('django')_

## Précision au niveau de l'exécution du projet

- **C'est le premier utilisateur** qui est créé qui obtient les droits **des premières collections générées**
car dans le fichier **`models.py`** nous avons ajouté un attribut **`user`** qui est un **`ForeignKey`** vers **`User`** avec
pour valeur par défaut **`1`** qui est **l'id du premier utilisateur**.
- **Pour les autres utilisateurs**, il faudra **créer des collections** et **éléments** pour qu'ils puissent les voir,
ils ne peuvent pas ajouter d'éléments à des collections qui ne leur appartiennent pas. Ils ne les vois pas non plus dans la liste des collections.
lors de la création d'un élément.

## Question 1

- `django-admin startproject cc`
- `python manage.py startapp collec_management`
- `python manage.py runserver 0.0.0.0:8000 &`

## Question 2

- **Creation d'un templates about.html**
- **Ajout de**
  - `path("", include("collec_management.urls")),` _dans `cc/urls.py`_
  - `path("about/", views.about, name="about"),` _dans `collec_management/urls.py`_

## Question 3

- `python manage.py makemigrations`
- `python manage.py sqlmigrate collec_management 0001` _(simple vérification de la migration)_
- `python manage.py migrate`
- `python manage.py shell` _(pour faire un test d'ajout)_
  - `from collec_management.models import Collec`
  - `from datetime import date`
  - `c = Collec(title="Collection 1", description="Description 1", date=date(2024, 10, 27))` _format de la date (year, month, day)_
  - `c.save()`

## Question 4

- `mkdir -p collec_management/fixtures` _(création du dossier fixtures)_
- `touch collec_management/fixtures/examples.json` _(création du fichier examples.json)_
- `python manage.py loaddata examples` _(commande pour l'ajout des fixtures)_

## Question 5

- **Application des migrations avec les fixtures précédentes**
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- **Création d'une vue** _`collec_management/views.py`_
- **Création d'un template** _`collec_management/templates/collec_management/collec.html`_
- **Ajout de** `path("collection/<int:id>", views.collec, name="collections"),` **dans** _`collec_management/urls.py`_

## Question 6

- **Création d'une vue** _`collec_management/views.py`_
- **Création d'un template** _`collec_management/templates/collec_management/all_collections.html`_
- **Ajout de** ` path('all/', views.all_collec, name='all_collections'),` **dans** _`collec_management/urls.py`_

## Question 7

- `touch collec_management/forms.py` _(création du fichier forms.py)_
- **Création d'une vue** _`collec_management/views.py`_
- **Création d'un template** _`collec_management/templates/collec_management/new_collection.html`_
- **Ajout de** ` path('new/', views.new_collection, name='new_collec'),` **dans** _`collec_management/urls.py`_

## Question 8

- **Création d'une vue** _`collec_management/views.py`_
- **Création d'un template** _`collec_management/templates/collec_management/delete_collection.html`_
- **Ajout de** `path("delete/<int:collec_id>", views.delete_collection, name="delete_collection"),` **dans** _`collec_management/urls.py`_

## Question 9

- **Création d'une vue** _`collec_management/views.py`_
- **Création d'un template** _`collec_management/templates/collec_management/edit_collection.html`_
- **Ajout de** `path("change/<int:collec_id>", views.edit_collection, name="edit_collection"),` **dans** _`collec_management/urls.py`_

## Question 10

- **Intégration de Bootstrap `'django_bootstrap5',` dans le fichier `settings.py`**
- **Création d'une navbar `templates/collec_management/navbar.html`** _(template du menu qui sera utilisé par tous les autres templates)_
- **Création d'une page principale `templates/collec_management/index.html`** _(page d'accueil)_
- **Création d'une vue `'collec_management/views.py'`**
- **Ajout de `path("", views.index, name="index"),` dans _`collec_management/urls.py`_**

## Question 11

- **On dé-commente `path("admin/", admin.site.urls),` dans le fichier `cc/urls.py`**
- `python manage.py createsuperuser` : _Crée un super utilisateur._
  - **username :** `cc2`
  - **email :** `maximilien.goujon@etu.univ-orleans.fr`
  - **password :** `Framework1234`
- **Ajout de `admin.site.register(Collec)` dans le fichier `admin.py`**

## Question 12

- **Création d'un model `Element`** _`collec_management/views.py`_
- **Ajout d'une relation OneToMany dans le model `Element`**
- **`python manage.py makemigrations`**
- **`python manage.py migrate`**
- **Ajout de `admin.site.register(Element)` dans le fichier `admin.py`**

## Question 13

- **Création de 60 éléments (5x12 éléments) principalement faite par un script bash**
- **Ajout après vérification dans le fichier `fixtures/examples.json`**
- **`python manage.py loaddata examples`**

## Question 14

- **Création d'un formulaire pour l'ajout d'un `Element`** _`collec_management/forms.py`_
- **Création d'une vue pour l'ajout d'un `Element`** _`collec_management/views.py`_
- **Création d'un template pour l'ajout d'un `Element`** _`templates/collec_management/new_element.html`_
- **Ajout de** `path("element/add/", views.new_element, name="new_element"),` **dans** _`collec_management/urls.py`_

- **Création d'une vue pour la suppression d'un `Element`** _`collec_management/views.py`_
- **Création d'un template pour la suppression d'un `Element`** _`templates/collec_management/delete_element.html`_
- **Ajout de** `path("element/delete/<int:element_id>", views.delete_element, name="delete_element"),` **dans** _`collec_management/urls.py`_

## Question 15

- **Création d'une vue pour l'affichage d'un `Element`** _`collec_management/views.py`_
- **Création d'un template pour l'affichage d'un `Element`** _`templates/collec_management/element.html`_
- **Ajout de** `path("element/<int:element_id>", views.element, name="element"),` **dans** _`collec_management/urls.py`_

- **Création d'une vue pour la modification d'un `Element`** _`collec_management/views.py`_
- **Création d'un template pour la modification d'un `Element`** _`templates/collec_management/edit_element.html`_
- **Ajout de** `path("element/edit/<int:element_id>", views.edit_element, name="edit_element"),` **dans** _`collec_management/urls.py`_

# Question 16

- **Modification de la vue `collec()` pour ajouter l'affichage des éléments liés à la collection** _`collec_management/views.py`_
- **Modification du template `collection.html` pour afficher les éléments liés à la collection** _`templates/collec_management/collection.html`_

# Question 17

- **Création d'un utilisateur dans la page admin django** _(pas nécéssaire grâce au super utilisateur mais plus correct)_
- **Création d'un template pour le login de l'utilisateur** _`templates/registration/login.html`_
- **Ajout de `LOGOUT_REDIRECT_URL = 'index'` dans `cc/urls.py`**
- **Ajout de `path("accounts/", include("django.contrib.auth.urls")),` dans `cc/settings.py`**
- **Ajout de la possiblité de se connecter et de se déconnecter dans la navbar directement** _`templates/collec_management/navbar.html`_

# Question 18

- **Ajout de `from django.contrib.auth.decorators import login_required` dans `collec_management/views.py`**
- **Ajout du décorateur pour les fonctions nécessitant d'être authetifié `@login_required`**
- **Ajout de `user = models.ForeignKey(User, on_delete=models.CASCADE)` dans les models `Collec` et `Element`**
- **`python manage.py makemigrations`**
- **`python manage.py migrate`**
- **Ajout de `request.user` dans les fonctions nécessitant l'utilisateur connecté**
- **Modification des templates pour faire en sorte que seul l'utilisateur qui à créer ces collection puisse voir les détails et autres modification**
