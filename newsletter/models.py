from django.contrib.auth.models import User
from django.db import models


class Subscriber(models.Model):
    """ Model for newsletter subscribers """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='subscription', null=True, blank=True)
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
