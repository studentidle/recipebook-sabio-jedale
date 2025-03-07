from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.recipe}'