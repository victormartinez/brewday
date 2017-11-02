from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView, UpdateView, FormView

from ..core.utils.mail import send_welcome_mail
from ..accounts.forms import UserLoginForm, UserRegistrationForm, EmailChangeForm, ProfileChangeForm

User = get_user_model()


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'core/login.html'


class UserLogoutView(LogoutView):
    def get_next_page(self):
        # messages.success(self.request, 'You have logged out.')
        return super(UserLogoutView, self).get_next_page()


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

    def get_success_url(self):
        send_welcome_mail(self.object)
        return super().get_success_url()


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    form_class = ProfileChangeForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        messages.success(self.request, 'Your Personal Info was changed successfully.')
        return super(UpdateProfileView, self).get_success_url()


class UpdateEmailView(LoginRequiredMixin, UpdateView):
    form_class = EmailChangeForm
    template_name = 'accounts/profile_email.html'
    success_url = reverse_lazy('accounts:profile_email')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Your email was changed successfully.')
        return super(UpdateEmailView, self).get_success_url()


class UpdatePasswordView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'accounts/profile_password.html'
    success_url = reverse_lazy('accounts:profile_password')

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Your password was changed successfully.')
        return super(UpdatePasswordView, self).get_success_url()


login = UserLoginView.as_view()
logout = UserLogoutView.as_view()
register = UserRegistrationView.as_view()
profile = UpdateProfileView.as_view()
profile_password = UpdatePasswordView.as_view()
profile_email = UpdateEmailView.as_view()
