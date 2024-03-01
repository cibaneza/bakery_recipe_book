from django import forms 
from .models import Product, Ingredient

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'yield_quantity']
        

        
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'description']
        

