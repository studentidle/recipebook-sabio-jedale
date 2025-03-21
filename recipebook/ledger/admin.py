from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile 

class IngredientAdmin(admin.ModelAdmin):
    '''
        show name, have search fields and filter
    '''
    model = Ingredient
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    '''
        show name, author and have search fields 
    '''
    model = Recipe
    list_display = ('name','author','createdOn','updatedOn',)
    list_filter = ('name','author',)
    search_fields =('name','author',)
    
class RecipeIngredientAdmin(admin.ModelAdmin):
    '''
        display receipe, ingredient and quantity also have filter
    '''
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity', )
    list_filter = ('recipe', 'ingredient', )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Profile)