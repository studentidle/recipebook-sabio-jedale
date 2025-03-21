from django.urls import path
from . import views

urlpatterns = [
    path('recipe/list', views.recipeList, name='recipe-list'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('home', views.home, name='home'),
]

app_name = "ledger"