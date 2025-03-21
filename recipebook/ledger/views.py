from django.shortcuts import render, HttpResponse
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required

def home(request):
    '''
        for viewing homepage of the website
    '''
    return render(request, 'home.html')

@login_required
def recipeList(request):
    '''
        for listing recipes
    '''
    recipe = Recipe.objects.all()
    context = {
        'recipes': recipe
    }
    return render(request, "recipeList.html", context)

@login_required
def recipe(request, id):
    '''
        for detailed view of the specific recipe and its ingredients
    '''
    recipe = Recipe.objects.get(id=id)
    recipeIngredients = RecipeIngredient.objects.filter(recipe=recipe)
    context = {
        'recipe_ingredients': recipeIngredients,
        'recipe': recipe,
    }
    return render(request, "recipe.html", context)
