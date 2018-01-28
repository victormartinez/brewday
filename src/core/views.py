from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from src.equipments.models import UserEquipment
from src.ingredients.models import UserIngredient
from src.recipes.models import Recipe


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('core:app'))
        return super(IndexView, self).get(request, *args, **kwargs)


class AppView(LoginRequiredMixin, TemplateView):
    template_name = 'core/app_logged.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes_count'] = Recipe.objects.filter(owner=self.request.user).count()
        context['equipments_count'] = UserEquipment.objects.filter(user=self.request.user).count()
        context['ingredients_count'] = UserIngredient.objects.filter(user=self.request.user).count()
        context['recipes'] = self.get_recipes()
        return context

    def get_recipes(self):
        recipes_qs = Recipe.objects.filter(owner=None)
        search = self.request.GET.get('search')
        if search:
            recipes_qs = recipes_qs.filter(
                Q(title__icontains=search) |
                Q(steps__icontains=search) |
                Q(observations__icontains=search)
            )
        return recipes_qs


index = IndexView.as_view()
app = AppView.as_view()
