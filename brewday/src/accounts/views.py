from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ..accounts.forms import UserLoginForm, UserRegistrationForm

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

login = UserLoginView.as_view()
logout = UserLogoutView.as_view()
register = UserRegistrationView.as_view()
