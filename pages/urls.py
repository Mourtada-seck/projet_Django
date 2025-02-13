from django.urls import path
from .views import home, login_view, inscription_view, logout_view, admin_dashboard

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("inscription/", inscription_view, name="inscription"),
    path("logout/", logout_view, name="logout"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    
]
