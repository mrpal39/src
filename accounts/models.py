from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse



# Create your models here.
class OwnerProfile(AbstractUser):
    is_information_confirmed = models.BooleanField(default=False)
    phone = models.CharField("Telefone", max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse("user_profile", args=[self.id])

    def __str__(self):
        return self.username
