from django.urls import path
from . import views

# recipes:recipes
app_name = 'recipes'

urlpatterns = [
    path('',  views.home, name="home"),  # home
    path('recipes/<id>/',  views.recipe, name="recipe"),
]
