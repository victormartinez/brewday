from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from src.recipes.models import Recipe
from .forms import NewRecipeForm


class MyRecipesView(LoginRequiredMixin, ListView):
    context_object_name = 'recipes'
    queryset = Recipe.objects.all()
    ordering = ('created',)
    template_name = 'recipes/my.html'


class NewRecipeView(LoginRequiredMixin, CreateView):
    form_class = NewRecipeForm
    success_url = reverse_lazy('recipes:new')
    template_name = 'recipes/new.html'


new_recipe = NewRecipeView.as_view()
my_recipes = MyRecipesView.as_view()
