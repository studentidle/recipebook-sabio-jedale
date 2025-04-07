from django import forms
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    '''
        forms for creating recipe
    '''
    class Meta:
        model = Recipe
        fields = ['name']

class IngredientForm(forms.ModelForm):
    '''
        forms for creating ingredient
    '''
    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    '''
        forms for creating recipeIngredient
    '''
    class Meta:
        model = RecipeIngredient
        fields = ['recipe','ingredient', 'quantity']

class RecipeImageForm(forms.ModelForm):
    '''
        forms for uploading image
    '''
    class Meta:
        model = RecipeImage
        fields = ['image','description']