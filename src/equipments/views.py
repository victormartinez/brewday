from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from src.equipments.forms import NewUserEquipmentFormSet, NewUserEquipmentForm, create_user_equipments
from src.equipments.models import UserEquipment


class MyEquipmentsView(LoginRequiredMixin, ListView):
    template_name = 'equipments/my.html'

    def get_queryset(self):
        return UserEquipment.objects.filter(user=self.request.user).order_by('-quantity')


class NewEquipmentView(LoginRequiredMixin, CreateView):
    form_class = NewUserEquipmentForm
    success_url = reverse_lazy('equipments:my')
    template_name = 'equipments/new.html'

    def get_context_data(self, **kwargs):
        context = super(NewEquipmentView, self).get_context_data(**kwargs)
        if 'formset' not in kwargs.keys():
            context['formset'] = NewUserEquipmentFormSet(queryset=UserEquipment.objects.none())
        else:
            context['formset'] = kwargs['formset']
        return context

    def post(self, request, *args, **kwargs):
        formset = NewUserEquipmentFormSet(request.POST)
        if formset.is_valid():
            create_user_equipments(formset, request.user)
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(formset=formset))


class DeleteEquipmentView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('equipments:my')

    def get_queryset(self):
        return UserEquipment.objects.filter(user=self.request.user)


class EditEquipmentView(LoginRequiredMixin, UpdateView):
    template_name = 'equipments/edit.html'
    model = UserEquipment
    fields = ('quantity', )
    success_url = reverse_lazy('equipments:my')

    def get_queryset(self):
        return UserEquipment.objects.filter(user=self.request.user)


my_equipments = MyEquipmentsView.as_view()
delete_equipment = DeleteEquipmentView.as_view()
new_equipment = NewEquipmentView.as_view()
edit_equipment = EditEquipmentView.as_view()
