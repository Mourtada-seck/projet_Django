from django.urls import path
from .views import home
from django.contrib.auth.views import LoginView  
from .views import home, inscription
from django.contrib.auth.views import LoginView
from .views import login_view

urlpatterns = [
    path('', home, name='home'),  # La page d'accueil sera accessible à "/"
    path('login/', LoginView.as_view(), name='login'),  # Page de connexion
]


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),  
    path('inscription/', inscription, name='inscription'),  
]


urlpatterns = [
    path("login/", login_view, name="login"),
]


