from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetView
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.views.generic import CreateView, UpdateView, FormView

from src.accounts.models import UserPreference
from ..core.utils.mail import send_welcome_mail
from ..accounts.forms import UserLoginForm, UserRegistrationForm, EmailChangeForm, ProfileChangeForm

User = get_user_model()


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'core/login.html'

    def form_valid(self, form):
        if form.cleaned_data['keep_signed']:
            self.request.session.set_expiry(604800)  # 1 week
        else:
            self.request.session.set_expiry(0)
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(LogoutView):
    def get_next_page(self):
        messages.success(self.request, 'You have logged out.')
        return super(UserLogoutView, self).get_next_page()


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

    def form_valid(self, form):
        messages.success(self.request, 'Your account was created. Please, login.')
        return super(UserRegistrationView, self).form_valid(form)

    def get_success_url(self):
        send_welcome_mail(self.object)
        return super().get_success_url()


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    form_class = ProfileChangeForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Your Personal Info was changed successfully.')
        return super(UpdateProfileView, self).form_valid(form)


class UpdateEmailView(LoginRequiredMixin, UpdateView):
    form_class = EmailChangeForm
    template_name = 'accounts/profile_email.html'
    success_url = reverse_lazy('accounts:profile_email')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your email was changed successfully.')
        return super(UpdateEmailView, self).form_valid(form)


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
        messages.success(self.request, 'Your password was changed successfully.')
        return super(UpdatePasswordView, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


class UserForgotPasswordView(PasswordResetView):
    template_name = 'core/forgot_password.html'
    email_template_name = 'emails/password_reset_email.html'
    subject_template_name = 'emails/password_reset_subject.txt'
    success_url = reverse_lazy('core:forgot_password')
    from_email = settings.DEFAULT_FROM_EMAIL

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(
            self.request,
            'If your e-mail is registered you will receive instructions on how to redefine your password.'
        )
        return super(UserForgotPasswordView, self).form_valid(form)


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'core/reset_confirm_password.html'
    success_url = reverse_lazy('core:login')
    form_class = SetPasswordForm

    def form_valid(self, form):
        messages.success(
            self.request,
            'Password reset successfully. Login in your account.'
        )
        return super(UserPasswordResetConfirmView, self).form_valid(form)


class UserPreferencesView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/profile_preferences.html'
    model = UserPreference
    fields = ('notified_by_storage', 'volume_threshold', 'weight_threshold',)
    success_url = reverse_lazy('accounts:profile_preferences')

    def get_object(self, queryset=None):
        return UserPreference.objects.get(user=self.request.user)

    def get_queryset(self):
        return UserPreference.objects.filter(user=self.request.user)


login = UserLoginView.as_view()
logout = UserLogoutView.as_view()
register = UserRegistrationView.as_view()
profile = UpdateProfileView.as_view()
profile_password = UpdatePasswordView.as_view()
profile_email = UpdateEmailView.as_view()
forgot_password = UserForgotPasswordView.as_view()
reset_password = UserPasswordResetConfirmView.as_view()
profile_preferences = UserPreferencesView.as_view()
