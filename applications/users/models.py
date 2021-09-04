from django.contrib.auth.models import AbstractUser
from django.db import models

"""
se utilizo el modelo User de Django pero se cambio solo la parte del id para que lo tuviera como un atributo

"""

class MyUser(AbstractUser):
    id = models.AutoField(primary_key=True)
