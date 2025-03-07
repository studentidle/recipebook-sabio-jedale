from django.db import models

class Ingredient(models.Model):
    '''
        accepts ingredient name
    '''
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'

class Recipe(models.Model):
    '''
        accepts receipe name
    '''
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'

class RecipeIngredient(models.Model):
    '''
        accepts ingredient, recipe and quantity
    '''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.recipe}'