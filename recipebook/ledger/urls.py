from django.urls import path
from . import views

urlpatterns = [
    path('recipe/list', views.recipeList, name='recipeList'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('home', views.home, name='home'),
    path('recipe/add/', views.addRecipe, name='addRecipe'),
    path('recipe/add/ingredient', views.addIngredient, name='addIngredient'),
    path('recipe/<int:num>/add_image', views.addImage, name='addImage'),
]

app_name = "ledger"