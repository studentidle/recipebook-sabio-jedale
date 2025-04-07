from django.shortcuts import render, redirect
from .models import Recipe, RecipeIngredient, RecipeImage, Profile
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm
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
    images = RecipeImage.objects.filter(recipe=recipe)
    context = {
        'recipe_ingredients': recipeIngredients,
        'recipe': recipe,
        'images': images,
    }
    return render(request, "recipe.html", context)

@login_required
def addRecipe(request):

    if request.method == 'POST':

        recipeForm = RecipeForm(request.POST)
        recipeIngredientForm = RecipeIngredientForm(request.POST)
        
        if recipeForm.is_valid(): 
                recipe = recipeForm.save(commit=False)
                profile = Profile.objects.get(user = request.user)
                recipeName = recipeForm.cleaned_data.get('name')

                if Recipe.objects.filter(name__iexact=recipeName, author=profile).exists():
                    recipeForm.add_error(None, 'Recipe already exists.')
                else:
                    recipe.name = recipeName
                    recipe.author = profile
                    recipe.save()
                    return redirect('ledger:addRecipe')
            
        if recipeIngredientForm.is_valid():

                recipeIngredient = recipeIngredientForm.save(commit=False)
                recipe = recipeIngredient.recipe

                recipeIngredient.save()
                recipe.save()
                return redirect('ledger:recipeList')

    else:
        recipeForm = RecipeForm()
        recipeIngredientForm = RecipeIngredientForm()

    context = {
        'recipe': recipeForm, 
        'recipeIngredient': recipeIngredientForm
    }
    
    return render(request, 'addRecipe.html', context)


