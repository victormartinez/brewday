from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.db import transaction

from ..accounts.models import Profile

User = get_user_model()


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']


class UserLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname']


class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', ]


class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    agree_terms = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=True,
        error_messages={'required': 'You need to accept the terms.'}
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': True})
        self.fields['username'].widget.attrs.update({'autofocus': False})

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'surname']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            with transaction.atomic():
                user.save()
                profile = Profile(
                    name=self.cleaned_data['name'],
                    surname=self.cleaned_data['surname'],
                    user=user
                )
                profile.save()
        return user
