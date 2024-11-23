from fnmatch import translate
from gettext import textdomain

from django.shortcuts import redirect, render, HttpResponse
from django.template.context_processors import request
from .models import produit
from django.views import View
from .forms import produitForm
from django.contrib import messages
#from translate import Translator

def index(request, *args, **kwargs):
    liste_produits = produit.objects.all()
    context = {
        'produits': liste_produits,
        'nom': 'produits de la boutique BN K N ',
    }

    return render(request, 'index.html',context)


#class CreateProduct(View):
 #   def get(self, request, *args, **kwargs):
  #      return render(request, 'produits/create_product.html')

   # def post(self, request, *args, **kwargs):
    #     try:

     #        nom = request.POST.get('nom')
      #       description = request.POST.get('description')
       #      prix = request.POST.get('prix')
#             image = request.FILES.get('image')

#             produit = produit.objects.create(nom=nom, description=description, prix=prix, image=image)

 #            if produit:
#                 return HttpResponse('produit enregistré avec succé')
#         except Exception as e:
#             return HttpResponse('erreur lors de l\'enregistrement du produit')

#def home( request):
 #   var = _("welcome")
 #   return render(request,'index.html',{'var':var})

"""
Etapes de translations
1 Definir les variables a traduires 
python manage.py makemessages -l la langue 
2 C'est de donner leurs equivalence dans les a traduire 
3 Compiler
python manage.py compilemessages

"""

class CreatProduct(View):
    def get(self, request, *args, **kwargs):
        form = produitForm()
        return render(request, 'produits/create_product.html', {'form':form } )

    def post(self, request, *args, **kwargs):
        form = produitForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'produit enregistré avec succé')
            return redirect('produits:index')
        else:
            messages.error(request, 'erreur lors de l\'enregistrement du produit')
            return render(request, 'produits/creat_product.html', {'form':form})




