from django.urls import include, path
from .views import recipeList, recipe

urlpatterns = [
    path('recipe/list', recipeList, name='Recipe-list'),
    path('recipe/<int:id>', recipe, name='Recipe-name'),
]

app_name = "ledger"