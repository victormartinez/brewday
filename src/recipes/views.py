from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import NewRecipeForm


class MyRecipesView(LoginRequiredMixin, TemplateView):
    template_name = 'recipes/my.html'


class NewRecipeView(LoginRequiredMixin, CreateView):
    form_class = NewRecipeForm
    success_url = reverse_lazy('recipes:new')
    template_name = 'recipes/new.html'


new_recipe = NewRecipeView.as_view()
my_recipes = MyRecipesView.as_view()
