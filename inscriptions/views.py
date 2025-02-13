from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'pages/home.html')  # Chemin vers le fichier template


def inscription(request):
    return render(request, 'pages/inscription.html')  


# page connexion
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirection après connexion
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, "pages/login.html")
