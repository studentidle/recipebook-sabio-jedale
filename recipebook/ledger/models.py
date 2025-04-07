from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
        accepts user, name and bio
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
    
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
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    
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

class RecipeImage(models.Model):
    '''
        accepts image and recipe
    '''
    image = models.ImageField(upload_to='images/', null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    
    def __str__(self):
        return f'{self.recipe}'