from django.views.generic import TemplateView


class NewRecipeView(TemplateView):
    template_name = 'recipes/new.html'


new_recipe = NewRecipeView.as_view()
