from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from ..accounts.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm

User = get_user_model()


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'core/login.html'


class UserLogoutView(LogoutView):
    def get_next_page(self):
        messages.success(self.request, 'You have logged out.')
        return super(UserLogoutView, self).get_next_page()


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:update_user')

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/profile_password.html'
    success_url = reverse_lazy('accounts:update_user')

    def get_object(self, queryset=None):
        return self.request.user


login = UserLoginView.as_view()
logout = UserLogoutView.as_view()
register = UserRegistrationView.as_view()
profile = ProfileView.as_view()
profile_password = ProfilePasswordView.as_view()
