import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from model_utils.models import TimeStampedModel

from .managers import CustomUserManager


def profile_image_upload_location(instance, filename):
    name = "avatar.{}".format(filename.split('.')[-1])
    return "{}/{}/{}/{}".format('media_cdn', 'profile_photos', instance.id, name)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    username = models.CharField(
        'username', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[a-zA-Z0-9_]+$'),
                'Enter a valid username',
                'invalid'
            )
        ], help_text='A short name will be used to unique identify you in the platform.'
    )

    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self)

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_superuser


class Profile(TimeStampedModel):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    photo = models.ImageField(
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field",
        upload_to=profile_image_upload_location
    )

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.surname)

    def __str__(self):
        return self.full_name
