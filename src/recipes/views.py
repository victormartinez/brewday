from django.views.generic import TemplateView


class MyRecipesView(TemplateView):
    template_name = 'recipes/my.html'


class NewRecipeView(TemplateView):
    template_name = 'recipes/new.html'


new_recipe = NewRecipeView.as_view()
my_recipes = MyRecipesView.as_view()
