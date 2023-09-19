from django.forms import ModelForm
from main.models import Product

class NewCollectionForm(ModelForm):
    class Meta:
        model = Product
        fields = ["collection", "type", "amount", "year", "description"]