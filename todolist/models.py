from django.db import models
from django.contrib.auth import models as auth_models;
from datetime import *;

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE);
    date = models.DateField(default=datetime.now());
    title = models.CharField(max_length=50);
    description = models.TextField(max_length=1000);
