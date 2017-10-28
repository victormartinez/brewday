from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from ..accounts.forms import UserLoginForm


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'core/login.html'


class UserLogoutView(LogoutView):
    def get_next_page(self):
        messages.success(self.request, 'You have logged out.')
        return super(UserLogoutView, self).get_next_page()


login = UserLoginView.as_view()
logout = UserLogoutView.as_view()
