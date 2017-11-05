from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class AppView(LoginRequiredMixin, TemplateView):
    template_name = 'core/app_logged.html'


index = IndexView.as_view()
app = AppView.as_view()
