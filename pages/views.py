from django.contrib.auth import get_user_model  
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm

# Récupère le modèle d'utilisateur personnalisé
CustomUser = get_user_model()

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
            print(f"✅ Connexion réussie : {user.username}, Superuser: {user.is_superuser}, Staff: {user.is_staff}")  # Debug

            # Redirection en fonction du rôle
            if user.is_superuser:  
                return redirect("/admin/")  # Redirige vers l'interface admin Django
            else:
                return redirect("home")  # Redirige les utilisateurs normaux
        
        else:
            messages.error(request, "❌ Nom d'utilisateur ou mot de passe incorrect.")
    
    return render(request, "pages/login.html")

def logout_view(request):
    logout(request)
    return redirect("/login/")  # Redirige vers la page de connexion

# Page inscription
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

# Page admin
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("home")  # Redirige si l'utilisateur n'est pas admin

    etudiants = CustomUser.objects.filter(is_superuser=False)  # On exclut les admins

    return render(request, "pages/admin_dashboard.html", {"etudiants": etudiants})
