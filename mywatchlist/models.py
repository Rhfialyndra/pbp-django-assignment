from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator ;

# Create your models here.


class MyWatchList(models.Model):
    title = models.CharField(max_length=69);
    release_date = models.CharField(max_length=10);
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]);
    description = models.TextField(max_length=500);
    watched = models.BooleanField(default=False);
    