from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import InscriptionForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def home(request):
    return render(request, "pages/home.html")


def inscription_view(request):
    return render(request, "pages/inscription.html")

 

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print(f"Utilisateur connecté : {user.username}, Superuser: {user.is_superuser}")  # Debug

            # Vérifie si l'utilisateur est admin
            if user.is_superuser:  
                return redirect(reverse("admin_dashboard"))  # ✅ 
            else:
                return redirect(reverse("home"))  # ✅ 
        
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    
    return render(request, "pages/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")  # Redirige vers la page de connexion


# page inscription
def inscription_view(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash du mot de passe
            user.save()
            login(request, user)  # Connexion automatique après l'inscription
            messages.success(request, "Inscription réussie. Bienvenue !")
            return redirect("/")  # Redirection après l'inscription
    else:
        form = InscriptionForm()

    return render(request, "pages/inscription.html", {"form": form})



# page admin
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("home")  # Redirige si l'utilisateur n'est pas admin

    etudiants = User.objects.filter(is_superuser=False)  # On exclut les admins

    return render(request, "pages/admin_dashboard.html", {"etudiants": etudiants})



