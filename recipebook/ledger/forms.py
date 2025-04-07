from django import forms
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']