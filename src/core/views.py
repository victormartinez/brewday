from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('core:app'))
        return super(IndexView, self).get(request, *args, **kwargs)


class AppView(LoginRequiredMixin, TemplateView):
    template_name = 'core/app_logged.html'


index = IndexView.as_view()
app = AppView.as_view()
