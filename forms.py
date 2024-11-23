from django import forms

from .models import produit


class produitForm(forms.ModelForm):

    prix = forms.FloatField()

    class Meta:

        model = produit

        fields = [ 'nom', 'description', 'prix', 'image']

    def clean_prix(self):
        prix = self.cleaned_data.get('prix')

        if prix < 0 or prix == 0 or prix == None or prix == '':
            raise forms.ValidationError('le prix doit être supérieur à 0')

        return prix