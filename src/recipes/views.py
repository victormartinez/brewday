from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from src.batches.forms import NewRecipeBatchForm
from src.ingredients.forms import NewRecipeIngredientFormSet, EditRecipeIngredientFormSet
from src.ingredients.models import UserIngredient, RecipeIngredient
from src.recipes.models import Recipe
from .forms import NewRecipeForm


class MyRecipesView(LoginRequiredMixin, ListView):
    context_object_name = 'recipes'
    ordering = ('created',)
    template_name = 'recipes/my.html'

    def get_queryset(self):
        recipes_qs = Recipe.objects.filter(owner=self.request.user)
        search = self.request.GET.get('search')
        if search:
            recipes_qs = recipes_qs.filter(
                Q(title__icontains=search) |
                Q(steps__icontains=search) |
                Q(observations__icontains=search)
            )
        return recipes_qs


class NewRecipeView(LoginRequiredMixin, CreateView):
    form_class = NewRecipeForm
    success_url = reverse_lazy('recipes:my')
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

                messages.success(self.request, 'Your recipe was created successfully.')
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(formset=formset, form=form))


class ShowRecipeView(LoginRequiredMixin, DetailView):
    template_name = 'recipes/show.html'

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class EditRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = (
    'title', 'description', 'expected_production', 'owner', 'og', 'fg', 'ibu', 'srm', 'abv', 'steps', 'observations',)
    template_name = 'recipes/edit.html'
    success_url = reverse_lazy('recipes:my')

    def get_context_data(self, **kwargs):
        context = super(EditRecipeView, self).get_context_data(**kwargs)
        if 'formset' not in kwargs.keys():
            context['formset'] = EditRecipeIngredientFormSet(
                queryset=RecipeIngredient.objects.filter(
                    recipe__owner=self.request.user,
                    recipe_id=self.kwargs['pk']
                )
            )
        else:
            context['formset'] = kwargs['formset']

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = NewRecipeForm(request.POST)
        edit_formset = EditRecipeIngredientFormSet(request.POST)
        if edit_formset.is_valid() and form.is_valid():
            with transaction.atomic():
                recipe = Recipe.objects.filter(owner_id=self.request.user, id=self.kwargs['pk'])
                recipe.update(**form.cleaned_data)

                recipe_ingredients_qs = RecipeIngredient.objects.filter(recipe__owner=self.request.user,
                                                                        recipe_id=self.kwargs['pk'])
                recipe_ingredients_ids = list(recipe_ingredients_qs.values_list('id', flat=True))
                for edit_form in edit_formset.forms:
                    recipe_ingredient = recipe_ingredients_qs.filter(id=edit_form.instance.id)
                    if recipe_ingredient.exists():
                        # Update
                        data = edit_form.cleaned_data.copy()
                        del data['id']
                        recipe_ingredient.update(**data)

                        updated_id = edit_form.cleaned_data['id'].id
                        recipe_ingredients_ids.pop(recipe_ingredients_ids.index(updated_id))
                    else:
                        new_instance = edit_form.save(commit=False)
                        new_instance.recipe = self.object
                        new_instance.save()

                if len(recipe_ingredients_ids):
                    RecipeIngredient.objects.filter(recipe__owner=self.request.user,
                                                    id__in=recipe_ingredients_ids).delete()

                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(formset=edit_formset, form=form))

    def get_success_url(self):
        messages.success(self.request, 'Your recipe was updated successfully.')
        return super(EditRecipeView, self).get_success_url()

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user, id=self.kwargs['pk'])


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('recipes:my')

    def get_success_url(self):
        messages.success(self.request, 'The recipe was deleted.')
        return super(DeleteRecipeView, self).get_success_url()

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class NewBatchView(LoginRequiredMixin, CreateView):
    template_name = 'recipes/show.html'
    form_class = NewRecipeBatchForm

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user'] = self.request.user.pk
        request.POST['recipe'] = Recipe.objects.get(owner=self.request.user, id=self.kwargs['pk']).pk
        return super(NewBatchView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super(NewBatchView, self).get_context_data(**kwargs)
        context_data['recipe'] = Recipe.objects.get(owner=self.request.user, id=self.kwargs['pk'])
        return context_data

    def get_success_url(self):
        messages.success(self.request, 'Congrats! You have started a batch!')
        return reverse('recipes:show', kwargs={'pk': self.kwargs['pk']})


new_recipe = NewRecipeView.as_view()
my_recipes = MyRecipesView.as_view()
show_recipe = ShowRecipeView.as_view()
edit_recipe = EditRecipeView.as_view()
delete_recipe = DeleteRecipeView.as_view()
new_batch = NewBatchView.as_view()
