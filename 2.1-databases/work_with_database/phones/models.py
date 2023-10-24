from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255, unique=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

