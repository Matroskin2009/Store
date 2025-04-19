<<<<<<< HEAD
from django.contrib.auth.hashers import make_password, check_password
=======
>>>>>>> 6595669a3a4a35557f0114ef1d6dcb8b6b1911d8
from django.db import models

from django.db import models
from django import forms

class User(models.Model):
    username = models.CharField(max_length=15, blank=False, unique=True)
    password = models.CharField(max_length=158, blank=False)
    count = models.IntegerField(default=0, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    remember_me = forms.BooleanField(required=False)
<<<<<<< HEAD

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
=======
>>>>>>> 6595669a3a4a35557f0114ef1d6dcb8b6b1911d8
