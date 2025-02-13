from django.contrib import admin
from django.contrib.admin.sites import AdminSite

admin.site.site_header = "Gestion des Inscriptions UCAB"
admin.site.site_title = "Tableau de Bord Admin"
admin.site.index_title = "Bienvenue sur le panneau d'administration"


class CustomAdminSite(AdminSite):
    site_header = "Gestion des Inscriptions UCAB"
    site_title = "Tableau de Bord Admin"
    index_title = "Bienvenue sur le panneau d'administration"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = '/static/css/custom_admin.css'  # Lien vers le CSS
        return context

admin.site = CustomAdminSite()

