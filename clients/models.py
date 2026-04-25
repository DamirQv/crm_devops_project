from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import EmailValidator

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    email = models.EmailField(validators=[EmailValidator()])
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name