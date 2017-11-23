from django.views.generic import TemplateView


class MyIngredientsView(TemplateView):
    template_name = 'ingredients/my.html'


class NewIngredientView(TemplateView):
    template_name = 'ingredients/new.html'


my_ingredients = MyIngredientsView.as_view()
new_ingredient = NewIngredientView.as_view()
