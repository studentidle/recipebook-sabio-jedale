from django.shortcuts import render, HttpResponse
from .models import Recipe, RecipeIngredient

def recipeList(request):
    recipe = Recipe.objects.all()
    
    ctx = {
        'recipes': recipe
    }
    
    return render(request, "recipeList.html", ctx)

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipeIngredients = RecipeIngredient.objects.filter(recipe=recipe)
    
    ctx = {
        'recipe_ingredients': recipeIngredients,
        'recipe': recipe,
    }
    
    return render(request, "recipe.html", ctx)
