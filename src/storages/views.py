from django.views.generic import TemplateView


class MyStorageView(TemplateView):
    template_name = 'storages/my.html'


class NewIngredientView(TemplateView):
    template_name = 'storages/new.html'


my_storage = MyStorageView.as_view()
new_ingredient = NewIngredientView.as_view()
