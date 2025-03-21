from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile 
from django.contrib.auth.models import User

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

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(admin.ModelAdmin):
	inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)