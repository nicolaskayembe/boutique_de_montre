from django.contrib import admin
from .models import produit

#admin.site.register(produit)

@admin.register(produit)
class produitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'description', 'image')