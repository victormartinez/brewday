from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from src.ingredients.forms import NewRecipeIngredientFormSet
from src.ingredients.models import UserIngredient
from src.recipes.models import Recipe
from .forms import NewRecipeForm


class MyRecipesView(LoginRequiredMixin, ListView):
    context_object_name = 'recipes'
    ordering = ('created',)
    template_name = 'recipes/my.html'

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class NewRecipeView(LoginRequiredMixin, CreateView):
    form_class = NewRecipeForm
    success_url = reverse_lazy('recipes:new')
    template_name = 'recipes/new.html'

    def get_context_data(self, **kwargs):
        context = super(NewRecipeView, self).get_context_data(**kwargs)
        if 'formset' not in kwargs.keys():
            context['formset'] = NewRecipeIngredientFormSet(queryset=UserIngredient.objects.none())
        else:
            context['formset'] = kwargs['formset']

        return context

    def post(self, request, *args, **kwargs):
        self.object = None

        form = NewRecipeForm(request.POST)
        formset = NewRecipeIngredientFormSet(request.POST)
        if formset.is_valid() and form.is_valid():

            with transaction.atomic():
                recipe = form.save(commit=False)
                recipe.owner = request.user
                recipe.save()

                new_instances = formset.save(commit=False)
                for new_instance in new_instances:
                    new_instance.recipe = recipe
                    new_instance.save()

                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(formset=formset, form=form))


new_recipe = NewRecipeView.as_view()
my_recipes = MyRecipesView.as_view()
