from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import User


class HomepageView(generic.ListView):
    template_name = 'homepage/homepage.html'

    # In case we define a comportment in the homepage linked with a DATABASE we have to set this function
    def get_queryset(self):
        """

        """
        return


# Vote contain paramaters that link with the question ID
def register(request):
    if request.method == 'GET':
        # récupère les données saisies par l'utilisateur
        prenom = request.GET['prenom']
        email = request.GET['email']
        password = request.GET['password']

        # Vérifie que l'émail n'exite pas.
        # hasher le mot de pass
        # ajoute un enregistrement dans la base de données
        p = User(prenom=prenom, email=email, password=password)
        p.save()

        # renvoyer un message à l'utilisateur
        return render(request, 'homepage/register.html',{'message':'Merci ' + prenom + ' de vous être enregistrer '})
    else:
        return render(request, 'homepage/register.html',{'message':'erreur'})


# Vote contain paramaters that link with the question ID
def login(request):
    if request.method == 'GET':
        # récupère les données saisies par l'utilisateur
        email = request.GET['email']
        # vérifier la validité du password
        password = request.GET['password']

        # ouvrir la base et rechercher l'email
        # User.objects.get(email=email)
        # User.objects.filter(email=email)
        if User.objects.filter(email=email):
            # renvoyer un message à l'utilisateur
            return render(request, 'homepage/profil.html',{'message': ''})
        else:
            return render(request, 'homepage/homepage.html',{'error_message':'Vous devez vous inscrire'})
    else:
        return render(request, 'homepage/register.html',{'error_message':'erreur de connexion'})
