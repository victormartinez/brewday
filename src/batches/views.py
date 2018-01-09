from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, UpdateView

from src.batches.models import RecipeBatch


class MyBatchesView(LoginRequiredMixin, ListView):
    template_name = 'batches/my.html'

    def get_queryset(self):
        return RecipeBatch.objects.filter(user=self.request.user).order_by('created')


class RestartBatchView(LoginRequiredMixin, UpdateView):
    model = RecipeBatch
    fields = ('restarted', 'finished',)

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['restarted'] = datetime.now()
        request.POST['finished'] = None
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'You have restarted a batch.')
        return reverse('batches:my')


class FinishBatchView(LoginRequiredMixin, UpdateView):
    model = RecipeBatch
    fields = ('finished',)

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['finished'] = datetime.now()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Congrats! You have finished your production. Enjoy your beer!')
        return reverse('batches:my')


my_batches = MyBatchesView.as_view()
finish_batch = FinishBatchView.as_view()
restart_batch = RestartBatchView.as_view()
