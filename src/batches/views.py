from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from src.batches.models import RecipeBatch


class MyBatchesView(LoginRequiredMixin, ListView):
    template_name = 'batches/my.html'

    def get_queryset(self):
        return RecipeBatch.objects.filter(user=self.request.user).order_by('created')


my_batches = MyBatchesView.as_view()
