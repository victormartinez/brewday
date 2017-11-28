from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from src.ingredients.models import UserIngredient
from src.ingredients.forms import NewUserIngredientFormSet, NewUserIngredientForm


class UserIngredientsDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('ingredients:my')

    def get_queryset(self):
        return UserIngredient.objects.filter(user=self.request.user)


class MyIngredientsView(LoginRequiredMixin, ListView):
    context_object_name = 'ingredients'
    template_name = 'ingredients/my.html'

    def get_queryset(self):
        return UserIngredient.objects.filter(user=self.request.user).order_by('-quantity')


class NewIngredientView(LoginRequiredMixin, CreateView):
    form_class = NewUserIngredientForm
    success_url = reverse_lazy('ingredients:new')
    template_name = 'ingredients/new.html'

    def get_context_data(self, **kwargs):
        context = super(NewIngredientView, self).get_context_data(**kwargs)
        if 'formset' not in kwargs.keys():
            context['formset'] = NewUserIngredientFormSet(queryset=UserIngredient.objects.none())
        else:
            context['formset'] = kwargs['formset']
        return context

    def post(self, request, *args, **kwargs):
        self.object = None

        formset = NewUserIngredientFormSet(request.POST)
        if formset.is_valid():
            new_instances = formset.save(commit=False)
            for new_instance in new_instances:
                new_instance.user = request.user
                new_instance.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(formset=formset))


my_ingredients = MyIngredientsView.as_view()
new_ingredient = NewIngredientView.as_view()
delete_ingredient = UserIngredientsDeleteView.as_view()
