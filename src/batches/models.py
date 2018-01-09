from django.db import models

from model_utils.models import TimeStampedModel

from src.accounts.models import User
from src.recipes.models import Recipe


class RecipeBatch(TimeStampedModel):
    recipe = models.ForeignKey(Recipe)
    user = models.ForeignKey(User)
    restarted = models.DateTimeField(null=True, blank=True)
    finished = models.DateTimeField(null=True, blank=True)
